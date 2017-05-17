<%
functions     = templateParameters['functions']
attributes    = templateParameters['attributes']
config        = templateParameters['config']
types         = templateParameters['types']
%>
#!/usr/bin/python

# This file was generated

class AttributeInfo:
    '''Information about NI-DMM attributes'''
    data = {
% for key in attributes:
        '${key}': { 'id': ${attributes[key]['id']}, 'type': ${attributes[key]['type']}, 'enum': ${attributes[key]['enum']}, 'access': '${attributes[key]['access']}' },
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
        }[self.getInfo(name)['type']


