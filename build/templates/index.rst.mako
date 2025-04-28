<%
    config        = template_parameters['metadata'].config
    doc_header    = f"{config['driver_name']} Python API Documentation"
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    mi_drivers = ['nidcpower', 'nidigital', 'nidmm', 'nifgen', 'nimodinst', 'niscope', 'niswitch', 'nise', 'nitclk']
    read_the_docs_note = (
        "Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier."
    )
%>\

${doc_header}
${"=" * len(doc_header)}

.. include:: about_${module_name}.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   ${module_name}

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

% if module_name in mi_drivers:
${read_the_docs_note}
% endif

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
