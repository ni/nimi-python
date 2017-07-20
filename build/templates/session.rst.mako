<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    attributes = template_parameters['metadata'].attributes
    attribute_docs = helper.normalize_string_type(template_parameters['metadata'].attribute_docs)
%>\
${helper.get_rst_header_snippet(driver_name + ' Session', '=')}

${config['session_description']}

${helper.get_rst_header_snippet('Attributes', '-')}

% for attr in sorted(attributes):
%   if str(attributes[attr]['id']) in attribute_docs:
${helper.get_rst_header_snippet(attr, '~')}

${attribute_docs[str(attributes[attr]['id'])]['longDescription']}

%   endif
% endfor
