# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = helper.filter_codegen_attributes(config['attributes'])
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.filter_codegen_functions(functions)
%>\

import ctypes
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import visatype


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id)


class Device(object):

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, owner, index):
        self._index = index
% for attribute in helper.sorted_attrs(attributes):
        self.${attributes[attribute]['name'].lower()} = Attribute${attributes[attribute]['type']}(owner, ${attribute}, index=index)
%   if 'documentation' in attributes[attribute]:
        '''
        ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
        '''
%   endif
% endfor
        self._is_frozen = True

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index']:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class Session(object):
    '''${config['session_class_description']}'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._${config['session_handle_parameter_name']} = 0
        self._item_count = 0
        self._current_item = 0
        self._encoding = 'windows-1251'
        self._library = library_singleton.get()
        self._${config['session_handle_parameter_name']}, self._item_count = self._open_installed_devices_session(driver)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __getitem__(self, index):
        return Device(self, index)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into self._library rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = visatype.ViInt32()
        error_info_ctype = None
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return "Failed to retrieve error description."
        error_info_buffer_size_ctype = visatype.ViInt32(error_code)
        error_info_ctype = ctypes.create_string_buffer(error_info_buffer_size_ctype.value)
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        self._current_item = 0
        return self

    def get_next(self):
        if self._current_item + 1 > self._item_count:
            raise StopIteration
        else:
            result = Device(self, self._current_item)
            self._current_item += 1
            return result

    def next(self):
        return self.get_next()

    def __next__(self):
        return self.get_next()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self._${config['session_handle_parameter_name']} != 0):
            self._close_installed_devices_session()
            self._${config['session_handle_parameter_name']} = 0

    ''' These are code-generated '''
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endfor
% endfor
% for handcoded_method in config['handcoded_methods']:
<%include file="${'/session.py' + handcoded_method['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config" />\
% endfor

