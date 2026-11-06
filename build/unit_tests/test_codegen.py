from build import codegen


def test_drivers_match_source_folders():
    src_drivers = {d.name for d in codegen.SRC_DIR.iterdir() if (d / 'metadata').is_dir()}

    assert set(codegen.DRIVERS) == src_drivers


def test_nifake_is_first_and_nimodinst_nitclk_are_last():
    names = list(codegen.DRIVERS)

    assert names[0] == 'nifake'
    assert names[-2:] == ['nimodinst', 'nitclk']


def test_grpc_supported_follows_proto_file():
    assert codegen.DRIVERS['nidmm'].grpc_supported
    assert codegen.DRIVERS['nidigital'].proto_file.name == 'nidigitalpattern.proto'
    assert not codegen.DRIVERS['nitclk'].grpc_supported


def test_py_files_to_generate_default_driver_with_grpc():
    files = codegen.py_files_to_generate(codegen.DRIVERS['nidmm'])

    assert 'session.py' in files
    assert 'unit_tests/_mock_helper.py' in files
    assert 'nidmm_pb2.py' in files
    assert 'nidevice_pb2_grpc.py' in files
    assert '_grpc_stub_interpreter.py' in files
    assert '_complextype.py' not in files


def test_py_files_to_generate_uses_proto_file_name():
    files = codegen.py_files_to_generate(codegen.DRIVERS['nidigital'])

    assert 'nidigitalpattern_pb2.py' in files
    assert 'nidigitalpattern_pb2_grpc.py' in files
    assert 'nidigital_pb2.py' not in files


def test_py_files_to_generate_extra_and_omitted_files():
    assert '_complextype.py' in codegen.py_files_to_generate(codegen.DRIVERS['nifake'])
    assert '_complextype.py' in codegen.py_files_to_generate(codegen.DRIVERS['nirfsa'])
    assert '_attributes.py' not in codegen.py_files_to_generate(codegen.DRIVERS['nise'])
    assert 'enums.py' in codegen.py_files_to_generate(codegen.DRIVERS['nise'])
    assert 'enums.py' not in codegen.py_files_to_generate(codegen.DRIVERS['nitclk'])
    assert '_attributes.py' in codegen.py_files_to_generate(codegen.DRIVERS['nitclk'])
    nimodinst_files = codegen.py_files_to_generate(codegen.DRIVERS['nimodinst'])
    assert 'enums.py' not in nimodinst_files
    assert '_attributes.py' not in nimodinst_files


def test_py_files_to_generate_without_grpc_has_no_pb2_files():
    files = codegen.py_files_to_generate(codegen.DRIVERS['nitclk'])

    assert not [f for f in files if 'pb2' in f or 'grpc' in f]


def test_doc_files_to_generate_names_are_driver_specific():
    files = dict(codegen.doc_files_to_generate(codegen.DRIVERS['nidmm']))

    assert files['about_nidmm.inc'] == 'about_driver.inc.mako'
    assert files['nidmm.rst'] == 'driver.rst.mako'
    assert files['grpc_session_options.rst'] == 'grpc_session_options.rst.mako'
    assert 'rep_caps.rst' not in files


def test_doc_files_to_generate_omitted_files():
    nitclk_files = dict(codegen.doc_files_to_generate(codegen.DRIVERS['nitclk']))

    assert 'enums.rst' not in nitclk_files
    assert 'rep_caps.rst' not in nitclk_files
    assert 'grpc_session_options.rst' not in nitclk_files
    assert 'rep_caps.rst' in dict(codegen.doc_files_to_generate(codegen.DRIVERS['niswitch']))


def test_find_template_prefers_driver_template():
    nitclk = codegen.DRIVERS['nitclk']

    assert codegen._find_template(nitclk, 'session.py.mako') == nitclk.src_dir / 'templates' / 'session.py.mako'
    assert codegen._find_template(nitclk, 'errors.py.mako') == codegen.TEMPLATE_DIR / 'errors.py.mako'
    assert codegen._find_template(codegen.DRIVERS['nidmm'], 'session.py.mako') == codegen.TEMPLATE_DIR / 'session.py.mako'


def test_custom_types_exist():
    for driver in codegen.DRIVERS.values():
        for custom_type in driver.custom_types:
            assert (driver.src_dir / 'custom_types' / custom_type).is_file()


def test_nifake_has_no_docs_or_examples():
    nifake = codegen.DRIVERS['nifake']

    assert not nifake.has_docs
    assert codegen.example_files(nifake) == ()


def test_example_files_are_sorted_and_skip_bytecode():
    files = codegen.example_files(codegen.DRIVERS['nidmm'])

    assert files
    assert list(files) == sorted(files)
    assert all(f.suffix != '.pyc' and '__pycache__' not in f.parts for f in files)


def test_readme_parts_for_driver():
    parts = codegen.readme_parts(codegen.DRIVERS['nidmm'])

    assert [p.name for p in parts] == [
        'status_project.inc',
        'about_nidmm.inc',
        'status.inc',
        'installation.inc',
        'contributing.inc',
        'nidmm_usage.inc',
        'support.inc',
        'nidmm_documentation.inc',
        'license.inc',
    ]


def test_root_readme_parts_include_each_driver_status_in_order(monkeypatch, tmp_path):
    for name in ('nitclk', 'nidmm', 'niscope'):
        (tmp_path / name).mkdir()
        (tmp_path / name / 'status.inc').write_text('')
    (tmp_path / 'nise').mkdir()
    monkeypatch.setattr(codegen, 'DOCS_DIR', tmp_path)

    status_files = [p for p in codegen.root_readme_parts() if p.name == 'status.inc']

    assert [p.parent.name for p in status_files] == ['nidmm', 'niscope', 'nitclk']


def test_rewrite_pb2_imports():
    contents = b'import session_pb2 as s\nimport nidevice_pb2 as n\nimport nifake_pb2 as f\nimport nidevice_pb2_grpc\n# import nifake_pb2\n'

    assert codegen.rewrite_pb2_imports(contents, 'nifake') == (
        b'import session_pb2 as s\n'
        b'from . import nidevice_pb2 as n\n'
        b'from . import nifake_pb2 as f\n'
        b'from . import nidevice_pb2_grpc\n'
        b'# import nifake_pb2\n')


def test_concatenate_files_is_binary_exact(tmp_path):
    (tmp_path / 'a.inc').write_bytes(b'first\n')
    (tmp_path / 'b.inc').write_bytes(b'second\r\nthird')
    dest = tmp_path / 'out' / 'README.rst'

    codegen.concatenate_files([tmp_path / 'a.inc', tmp_path / 'b.inc'], dest)

    assert dest.read_bytes() == b'first\nsecond\r\nthird'


def test_clean_removes_generated_files_but_not_doc_subfolders(monkeypatch, tmp_path):
    root = tmp_path
    generated = root / 'generated'
    docs = root / 'docs'
    build = root / 'build'
    (generated / 'nidmm').mkdir(parents=True)
    (generated / 'nidmm' / 'setup.py').write_text('')
    (docs / 'nidmm' / 'subfolder').mkdir(parents=True)
    (docs / 'nidmm' / 'index.rst').write_text('')
    (docs / 'nidmm' / '.readthedocs.yaml').write_text('')
    (docs / 'nidcpower').mkdir()
    (docs / 'nidcpower' / 'index.rst').write_text('')
    (build / '__pycache__').mkdir(parents=True)
    (build / '__pycache__' / 'x.pyc').write_text('')
    (root / 'README.rst').write_text('')
    (root / '.coverage').write_text('')
    for name, value in (('ROOT_DIR', root), ('GENERATED_DIR', generated), ('DOCS_DIR', docs), ('BUILD_HELPER_DIR', build)):
        monkeypatch.setattr(codegen, name, value)

    codegen.clean([codegen.DRIVERS['nidmm']])

    assert generated.is_dir()
    assert not list(generated.iterdir())
    assert [p.name for p in (docs / 'nidmm').iterdir()] == ['subfolder']
    assert (docs / 'nidcpower' / 'index.rst').exists()
    assert not (build / '__pycache__').exists()
    assert not (root / 'README.rst').exists()
    assert not (root / '.coverage').exists()


def test_parse_args_defaults_to_all_drivers():
    args = codegen.parse_args(['generate'])

    assert args.command == 'generate'
    assert args.drivers is None


def test_parse_args_repeated_driver():
    args = codegen.parse_args(['installers', '--driver', 'nidmm', '--driver', 'nitclk', '-v'])

    assert args.command == 'installers'
    assert args.drivers == ['nidmm', 'nitclk']
    assert args.verbose == 1
