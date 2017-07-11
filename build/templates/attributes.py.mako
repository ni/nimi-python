<%
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
module_name = config['module_name']
%>
#!/usr/bin/python

# This file was generated

from ${module_name} import python_types
from ${module_name} import enums

class AttributeInfo:
    '''Information about NI-DMM attributes'''
    data = {
% for key in attributes:
<%
enumName = 'None' if attributes[key]['enum'] is None else 'enums.' + attributes[key]['enum']
%>\
        '${key}': { 'id': ${attributes[key]['id']}, 'type': python_types.${attributes[key]['type']}, 'enum': ${enumName}, 'access': '${attributes[key]['access']}' },
% endfor
    }


    def getInfo(self, name):
        if name in data:
            return data[name]
        else:
            raise Exception("Attribute " + name + " not found")


    def getID(self, name):
        return self.getInfo(name)['id']


    def getType(self, name):
        return {
            'ViBoolean': c_ushort,
            'ViInt32': c_long,
            'ViString': c_char_p,
            'ViReal64': c_double,
        }[self.getInfo(name)['type']]


