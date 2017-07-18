# This file was generated
<%
import build.helper as helper

attributes = template_parameters['metadata'].attributes
attribute_docs = template_parameters['metadata'].attribute_docs
%>\

% for attribute in sorted(attributes):
% if str(attributes[attribute]['id']) in attribute_docs:

'''
${attribute_docs[str(attributes[attribute]['id'])]}
'''
${attribute.lower()} = None
% endif
% endfor

