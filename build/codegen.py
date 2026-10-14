"""Generate the driver bindings, documentation and installers.

Run from anywhere with ``python -m build.codegen {generate,clean,installers}``. Everything is
regenerated on every run; no attempt is made to skip work that is already up to date.
"""

import argparse
from dataclasses import dataclass
import logging
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

from build import configure_logging
from build import generate_template
from build.utilities import load_build

ROOT_DIR = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT_DIR / 'build'
TEMPLATE_DIR = BUILD_DIR / 'templates'
GENERATED_DIR = ROOT_DIR / 'generated'
DOCS_DIR = ROOT_DIR / 'docs'
STATIC_DOCS_DIR = DOCS_DIR / '_static'
SRC_DIR = ROOT_DIR / 'src'
SHARED_PROTOS_DIR = SRC_DIR / 'shared_protos'
NI_APIS_PROTOS_DIR = ROOT_DIR / 'third_party' / 'ni-apis' / 'ni' / 'grpcdevice' / 'v1'

DEFAULT_PY_FILES_TO_GENERATE = (
    '_attributes.py',
    'enums.py',
    '_library.py',
    '_library_interpreter.py',
    '_library_singleton.py',
    'session.py',
    'errors.py',
    'unit_tests/_mock_helper.py',
    'unit_tests/_matchers.py',
    '__init__.py',
    '_converters.py',
    'VERSION',
)

GRPC_PY_FILES_TO_GENERATE = (
    '_grpc_stub_interpreter.py',
    'grpc_session_options.py',
)

DEFAULT_PY_FILES_TO_COPY = (
    '_visatype.py',
)

# Documentation files that are generated for every driver, as (file name, template name).
# {driver} is replaced by the driver name.
DEFAULT_DOC_FILES_TO_GENERATE = (
    ('about_{driver}.inc', 'about_driver.inc.mako'),
    ('index.rst', 'index.rst.mako'),
    ('{driver}.rst', 'driver.rst.mako'),
    ('enums.rst', 'enums.rst.mako'),
    ('examples.rst', 'examples.rst.mako'),
    ('installation.inc', 'installation.inc.mako'),
    ('status.inc', 'status.inc.mako'),
    ('class.rst', 'class.rst.mako'),
    ('toc.inc', 'toc.inc.mako'),
    ('errors.rst', 'errors.rst.mako'),
    ('rep_caps.rst', 'rep_caps.rst.mako'),
)

GRPC_DOC_FILES_TO_GENERATE = (
    ('grpc_session_options.rst', 'grpc_session_options.rst.mako'),
)

SPHINX_FILES_TO_GENERATE = (
    ('conf.py', 'conf.py.mako'),
    ('.readthedocs.yaml', '.readthedocs.yaml.mako'),
)


@dataclass(frozen=True)
class Driver:
    """How a driver differs from the default set of generated files."""
    name: str
    extra_py_files: tuple = ()
    omit_py_files: tuple = ()
    omit_doc_files: tuple = ()
    custom_types: tuple = ()
    has_docs: bool = True
    proto_file_name: str = None

    @property
    def src_dir(self):
        return SRC_DIR / self.name

    @property
    def metadata_dir(self):
        return self.src_dir / 'metadata'

    @property
    def output_dir(self):
        return GENERATED_DIR / self.name

    @property
    def module_dir(self):
        return self.output_dir / self.name

    @property
    def docs_dir(self):
        return DOCS_DIR / self.name

    @property
    def proto_file(self):
        return self.metadata_dir / (self.proto_file_name or f'{self.name}.proto')

    @property
    def grpc_supported(self):
        return self.proto_file.exists()


# In alphabetical order except put nifake first and nimodinst/nitclk last
# - nifake first to get the most code generator coverage
# - nimodinst last so that the version from nimodinst is used for any global versions (docs/conf.py)
DRIVERS = {d.name: d for d in (
    Driver(
        'nifake',
        extra_py_files=('_complextype.py',),
        custom_types=('custom_struct.py', 'custom_struct_typedef.py', 'custom_struct_nested_typedef.py'),
        has_docs=False),
    Driver(
        'nidcpower',
        custom_types=('lcr_load_compensation_spot.py', 'lcr_measurement.py')),
    Driver(
        'nidigital',
        custom_types=('history_ram_cycle_information.py',),
        proto_file_name='nidigitalpattern.proto'),
    Driver(
        'nidmm',
        omit_doc_files=('rep_caps.rst',)),
    Driver('nifgen'),
    Driver(
        'nirfsa',
        extra_py_files=('_complextype.py',),
        custom_types=('coefficient_info_type.py', 'waveform_info.py', 'spectrum_info_type.py')),
    Driver(
        'nirfsg',
        extra_py_files=('_complextype.py',)),
    Driver(
        'niscope',
        custom_types=('waveform_info.py', 'measurement_stats.py')),
    Driver('niswitch'),
    Driver(
        'nise',
        omit_py_files=('_attributes.py',),
        omit_doc_files=('rep_caps.rst',)),
    Driver(
        'nimodinst',
        omit_py_files=('enums.py', '_attributes.py'),
        omit_doc_files=('rep_caps.rst', 'enums.rst')),
    Driver(
        'nitclk',
        omit_py_files=('enums.py',),
        omit_doc_files=('rep_caps.rst', 'enums.rst')),
)}


def _trace(action, path):
    path = Path(path)
    try:
        path = path.relative_to(ROOT_DIR)
    except ValueError:
        pass
    print(f'{action:>15}: {path}')


def _find_template(driver, template_name):
    """Use the driver's own template if it has one, otherwise the shared one."""
    driver_template = driver.src_dir / 'templates' / template_name
    if driver_template.exists():
        return driver_template
    return TEMPLATE_DIR / template_name


def py_files_to_generate(driver):
    files = DEFAULT_PY_FILES_TO_GENERATE + driver.extra_py_files
    if driver.grpc_supported:
        stem = driver.proto_file.stem
        files += GRPC_PY_FILES_TO_GENERATE + (f'{stem}_pb2.py', f'{stem}_pb2_grpc.py', 'nidevice_pb2.py', 'nidevice_pb2_grpc.py')
    return tuple(f for f in files if f not in driver.omit_py_files)


def doc_files_to_generate(driver):
    """Returns (file name, template name) pairs."""
    files = DEFAULT_DOC_FILES_TO_GENERATE
    if driver.grpc_supported:
        files += GRPC_DOC_FILES_TO_GENERATE
    return tuple(
        (name.format(driver=driver.name), template)
        for name, template in files
        if name not in driver.omit_doc_files)


def unit_test_files_to_copy(driver):
    return tuple(sorted((driver.src_dir / 'unit_tests').glob('*.py')))


def example_files(driver):
    examples_dir = driver.src_dir / 'examples'
    if not examples_dir.is_dir():
        return ()
    return tuple(
        f for f in sorted(examples_dir.rglob('*'))
        if f.is_file() and '__pycache__' not in f.parts and f.suffix != '.pyc')


def readme_parts(driver):
    """Files that are concatenated to create the driver's README.rst."""
    return (
        STATIC_DOCS_DIR / 'status_project.inc',
        driver.docs_dir / f'about_{driver.name}.inc',
        driver.docs_dir / 'status.inc',
        driver.docs_dir / 'installation.inc',
        STATIC_DOCS_DIR / 'contributing.inc',
        STATIC_DOCS_DIR / f'{driver.name}_usage.inc',
        STATIC_DOCS_DIR / 'support.inc',
        STATIC_DOCS_DIR / f'{driver.name}_documentation.inc',
        STATIC_DOCS_DIR / 'license.inc',
    )


def root_readme_parts():
    driver_status_files = tuple(sorted(DOCS_DIR.glob('*/status.inc')))
    return (
        STATIC_DOCS_DIR / 'status_project.inc',
        STATIC_DOCS_DIR / 'about.inc',
        *driver_status_files,
        STATIC_DOCS_DIR / 'installation.inc',
        STATIC_DOCS_DIR / 'contributing.inc',
        STATIC_DOCS_DIR / 'nidmm_usage.inc',
        STATIC_DOCS_DIR / 'support.inc',
        STATIC_DOCS_DIR / 'documentation.inc',
        STATIC_DOCS_DIR / 'license.inc',
    )


def rewrite_pb2_imports(contents, proto_stem):
    """Make the generated modules import each other as part of the driver package."""
    for stem in ('nidevice', proto_stem):
        contents = re.sub(rb'^import ' + stem.encode() + rb'_pb2', b'from . import ' + stem.encode() + rb'_pb2', contents, flags=re.MULTILINE)
    return contents


def _load_metadata(driver):
    # Every template must start from freshly loaded metadata because loading it modifies it in place.
    for name in [n for n in sys.modules if n == 'metadata' or n.startswith('metadata.')]:
        del sys.modules[name]
    return load_build(str(driver.metadata_dir))


def render_template(driver, template, dest_file):
    _trace('Generating', dest_file)
    Path(dest_file).parent.mkdir(parents=True, exist_ok=True)
    template_params = {
        'metadata': _load_metadata(driver),
        'include_grpc_support': driver.grpc_supported,
    }
    generate_template(str(template), template_params, str(dest_file))


def copy_file(source, dest_file):
    _trace('Copying', dest_file)
    Path(dest_file).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest_file)


def concatenate_files(sources, dest_file):
    _trace('Creating', dest_file)
    Path(dest_file).parent.mkdir(parents=True, exist_ok=True)
    with open(dest_file, 'wb') as dest:
        for source in sources:
            dest.write(Path(source).read_bytes())


def generate_pb2_files(driver):
    stem = driver.proto_file.stem
    proto_dirs = (driver.metadata_dir, SHARED_PROTOS_DIR, NI_APIS_PROTOS_DIR)
    for proto_stem in (stem, 'nidevice'):
        _trace('Generating', driver.module_dir / f'{proto_stem}_pb2.py and {proto_stem}_pb2_grpc.py')
        command = [sys.executable, '-m', 'grpc_tools.protoc']
        command += [f'-I={d}' for d in proto_dirs]
        command += [f'--python_out={driver.module_dir}', f'--grpc_python_out={driver.module_dir}', f'{proto_stem}.proto']
        subprocess.run(command, cwd=ROOT_DIR, check=True)
    for suffix in ('_pb2.py', '_pb2_grpc.py'):
        for proto_stem in (stem, 'nidevice'):
            pb2_file = driver.module_dir / f'{proto_stem}{suffix}'
            pb2_file.write_bytes(rewrite_pb2_imports(pb2_file.read_bytes(), stem))


def zip_examples(driver):
    files = example_files(driver)
    if not files:
        return
    examples_dir = driver.src_dir / 'examples'
    zip_path = GENERATED_DIR / 'examples' / f'{driver.name}_examples.zip'
    _trace('Zipping', zip_path)
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        for f in files:
            zip_file.write(f, f.relative_to(examples_dir).as_posix())


def generate_driver(driver):
    print()
    print(f'Making {driver.name}')

    for file_name in py_files_to_generate(driver):
        if file_name.endswith(('_pb2.py', '_pb2_grpc.py')):
            continue
        dest = driver.module_dir / file_name
        render_template(driver, _find_template(driver, Path(file_name).name + '.mako'), dest)
    if driver.grpc_supported:
        generate_pb2_files(driver)

    for file_name in DEFAULT_PY_FILES_TO_COPY:
        copy_file(TEMPLATE_DIR / file_name, driver.module_dir / file_name)
    for file_name in driver.custom_types:
        copy_file(driver.src_dir / 'custom_types' / file_name, driver.module_dir / file_name)
    for source in unit_test_files_to_copy(driver):
        copy_file(source, driver.module_dir / 'unit_tests' / source.name)

    render_template(driver, TEMPLATE_DIR / 'setup.py.mako', driver.output_dir / 'setup.py')
    render_template(driver, TEMPLATE_DIR / 'tox-system_tests.ini.mako', driver.output_dir / 'tox-system_tests.ini')

    if driver.has_docs:
        for file_name, template_name in doc_files_to_generate(driver):
            render_template(driver, _find_template(driver, template_name), driver.docs_dir / file_name)
        for file_name, template_name in SPHINX_FILES_TO_GENERATE:
            render_template(driver, _find_template(driver, template_name), driver.docs_dir / file_name)

    # We can't build the actual readme for nifake since not all the files are created.
    # A placeholder is needed for inclusion into the wheel that will never be used.
    if driver.has_docs:
        concatenate_files(readme_parts(driver), driver.output_dir / 'README.rst')
    else:
        copy_file(ROOT_DIR / 'LICENSE', driver.output_dir / 'README.rst')

    zip_examples(driver)


def generate(drivers, include_root_readme):
    # The templates and metadata processing use paths relative to the root of the repository.
    os.chdir(ROOT_DIR)
    GENERATED_DIR.mkdir(exist_ok=True)
    for driver in drivers:
        generate_driver(driver)
    if include_root_readme:
        print()
        print('Making Global Files')
        concatenate_files(root_readme_parts(), ROOT_DIR / 'README.rst')


def clean(drivers):
    print('Cleaning...')
    shutil.rmtree(GENERATED_DIR, ignore_errors=True)
    for pycache_dir in BUILD_DIR.rglob('__pycache__'):
        shutil.rmtree(pycache_dir, ignore_errors=True)
    for pyc_file in BUILD_DIR.rglob('*.pyc'):
        pyc_file.unlink()
    for driver in drivers:
        if driver.docs_dir.is_dir():
            for doc_file in driver.docs_dir.iterdir():
                if doc_file.is_file():
                    doc_file.unlink()
    (ROOT_DIR / '.coverage').unlink(missing_ok=True)
    (ROOT_DIR / 'README.rst').unlink(missing_ok=True)
    # Keep the generated directory available for CI builds
    GENERATED_DIR.mkdir(exist_ok=True)


def installers(drivers, verbose):
    for driver in drivers:
        print()
        print(f'Making {driver.name} installers')
        log_file = driver.output_dir / 'log' / 'sdist_wheel.log'
        log_file.parent.mkdir(parents=True, exist_ok=True)
        _trace('Creating sdist and wheel', driver.output_dir / 'dist')
        result = subprocess.run(
            [sys.executable, '-m', 'build'],
            cwd=driver.output_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log_file.write_bytes(result.stdout)
        if verbose or result.returncode != 0:
            sys.stdout.write(result.stdout.decode(errors='replace'))
        if result.returncode != 0:
            sys.exit(f'Building the installers for {driver.name} failed. See {log_file}')


def parse_args(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='Verbose output')
    common.add_argument(
        '--log-file', default=None,
        help='Send logging to listed file instead of stdout')

    drivers_parent = argparse.ArgumentParser(add_help=False)
    drivers_parent.add_argument(
        '--driver', action='append', choices=list(DRIVERS), dest='drivers', metavar='DRIVER',
        help=f'Driver to process. Can be repeated. Default is all drivers: {", ".join(DRIVERS)}')

    parser = argparse.ArgumentParser(prog='build.codegen', description=__doc__.splitlines()[0])
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser(
        'generate', parents=[common, drivers_parent],
        help='Generate bindings, documentation and READMEs. The root README.rst is only generated for all drivers.')
    subparsers.add_parser(
        'clean', parents=[common, drivers_parent],
        help='Delete generated files')
    subparsers.add_parser(
        'installers', parents=[common, drivers_parent],
        help='Build the sdist and wheel for each driver from generated/<driver>. Run generate first.')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.log_file)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.log_file)
    else:
        configure_logging(logging.WARNING, args.log_file)

    drivers = [DRIVERS[name] for name in args.drivers] if args.drivers else list(DRIVERS.values())
    if args.command == 'generate':
        generate(drivers, include_root_readme=not args.drivers)
    elif args.command == 'clean':
        clean(drivers)
    elif args.command == 'installers':
        installers(drivers, args.verbose > 0)


if __name__ == '__main__':
    main()
