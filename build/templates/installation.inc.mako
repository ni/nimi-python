<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\

.. _${module_name}_installation-section:

Installation
------------

As a prerequisite to using the ${module_name} module, you must install the ${driver_name} runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **${driver_name}**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install ${module_name}~=${config['module_version']}

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install ${module_name}


