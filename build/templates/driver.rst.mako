<%
    '''This is a template for the module-specific .rst'''

    config        = template_parameters['metadata'].config
    module_name   = config['module_name']
    doc_header    = f"{module_name} module"
%>\
${doc_header}
${"=" * len(doc_header)}

.. include:: installation.inc

% if module_name == "niscope":
.. include:: ../_static/niscope_usage_docs_links.inc
% endif

.. include:: ../_static/${module_name}_usage.inc

.. include:: toc.inc

