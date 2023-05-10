<%
    config        = template_parameters['metadata'].config
    doc_header    = f"{config['driver_name']} Python API Documentation"
    module_name   = config['module_name']
    driver_name   = config['driver_name']
%>\

${doc_header}
${"=" * len(doc_header)}

.. include:: ../_static/about.inc

.. include:: ../_static/installation.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. include:: ../_static/documentation.inc

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.


.. include:: ../_static/license.inc

.. toctree::
   :maxdepth: 3

   ${module_name}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
