<%
functions     = templateParameters['functions']
attributes    = templateParameters['attributes']
config        = templateParameters['config']
types         = templateParameters['types']
%>
#!/usr/bin/python

# This file was generated


from ctypes import *
import platform

def getLibraryName():
   is_64bits = sys.maxsize > 2**32

% if 'library_linux' in config:
   if platform.system() == "Linux":
      if is_64bits:
         return "${config['library_linux']['64']}"
      else:
         return "${config['library_linux']['32']}"
%endif
% if 'library_mac' in config:
   if platform.system() == "Darwin":
      if is_64bits:
         return "${config['library_mac']['64']}"
      else:
         return "${config['library_mac']['32']}"
% endif

   if is_64bits:
      return "${config['library_windows']['64']}"
   else:
      return "${config['library_windows']['32']}"



def getLibrary()
   library = CDLL(getLibraryName())

   """ Specify required argument types (function prototypes) and Return types.
       https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
       https://docs.python.org/3/library/ctypes.html#return-types
       This provides some automatic conversion and error checking when calling NI-DMM functions.
       Strictly speaking, this is not necessary if/when we code-generate the calling code.
       It may have some performance impact as well.
   """

% for f in functions:
<%
   param_types = ""
   for p in f['params']:
      if len(param_types) > 0:
         param_types += ", "
      if p['direction'] == 'out':
         param_types += "POINTER(" + types[p['type']] + ")"
      else:
         param_types += types[p['type']]
%>
   library.${f['name']}.restype = ${types[f['ret_type']]}
   library.${f['name']}.argtypes = [${param_types}]
% endfor

   return library
