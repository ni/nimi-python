<%
    import build.helper as helper
    from packaging.version import Version

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    v = Version(config['module_version'])
    if v.pre is not None or v.dev is not None:
        # If the version is a prerelease or a dev release we do not put a version to pin to in the installation instructions
        # This is confusing when seen in master because the version doesn't exist yet
        version_pin = ''
    else:
        version_pin = '~=' + config['module_version']
%>\

.. _${module_name}_installation-section:

Installation
------------

As a prerequisite to using the ${module_name} module, you must install the ${driver_name} runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **${driver_name}**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install ${module_name}${version_pin}


