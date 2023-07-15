<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    driver_name   = config['driver_name']
%>\
.. _about-section:

About
=====

The **${module_name}** module provides a Python API for ${driver_name}. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
${module_name} supports all the Operating Systems supported by ${driver_name}.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions.

