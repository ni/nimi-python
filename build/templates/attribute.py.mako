# This file was generated
<%
import build.helper as helper

attributes = template_parameters['metadata'].attributes
attribute_docs = template_parameters['metadata'].attribute_docs
module_name = template_parameters['metadata'].config['module_name']
%>\
% for attribute in sorted(attributes):
% if str(attributes[attribute]['id']) in attribute_docs:

${attribute.lower()} = None
'''
${attribute_docs[str(attributes[attribute]['id'])]}
'''
% endif
% endfor

