# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = config['attributes']
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.extract_codegen_functions(functions)
    functions = helper.add_all_metadata(functions)
%>\

import ctypes
from ${module_name} import ctypes_types
from ${module_name} import errors
from ${module_name} import library_singleton
from ${module_name} import python_types


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._owner.handle, self._index, self._attribute_id)

    def __setitem__(self, index):
        raise TypeError('%r is read only' % self)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_int32(self._owner.handle, self._index, self._attribute_id), format_spec)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._owner.handle, self._index, self._attribute_id)

    def __setitem__(self, index):
        raise TypeError('%r is read only' % self)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_string(self._owner.handle, self._index, self._attribute_id), format_spec)


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
        if self._is_frozen and name not in ['_is_frozen', 'index']:
            raise TypeError("%s is not writable" % name)
        object.__setattr__(self, name, value)


class Session(object):
    '''${config['session_description']}'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self.handle = 0
        self.item_count = 0
        self.current_item = 0
        self.library = library_singleton.get()
        self.handle, self.item_count = self._open_installed_devices_session(driver)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def __getitem__(self, index):
        return Device(self, index)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # TODO(texasaggie97) Rewrite to use code generated method, if possible.
        buffer_size = self.library.${c_function_prefix}GetExtendedErrorInfo(0, None)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes_types.ViStatus_ctype(error_code)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.${c_function_prefix}GetExtendedErrorInfo(buffer_size, error_message)

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return error_message.value.decode("ascii")

    # Iterator functions
    def __len__(self):
        return self.item_count

    def __iter__(self):
        self.current_item = 0
        return self

    def get_next(self):
        if self.current_item + 1 > self.item_count:
            raise StopIteration
        else:
            result = Device(self, self.current_item)
            self.current_item += 1
            return result

    def next(self):
        return self.get_next()

    def __next__(self):
        return self.get_next()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.handle != 0):
            self._close_installed_devices_session(self.handle)
            self.handle = 0

    ''' These are code-generated '''
% for func_name in sorted(functions):
<%
    f = functions[func_name]
    parameters = f['parameters']
    input_parameters = helper.extract_input_parameters(parameters)
    output_parameters = helper.extract_output_parameters(parameters)
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
    ivi_dance_parameter = helper.extract_ivi_dance_parameter(parameters)
    ivi_dance_size_parameter = helper.find_size_parameter(ivi_dance_parameter, parameters)
%>
    def ${f['python_name']}(${helper.get_method_parameters_snippet(parameters, skip_session_handle = True, skip_output_parameters = True, skip_ivi_dance_size_parameter = True)}):
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter)}
% endfor
% for output_parameter in output_parameters:
        ${helper.get_ctype_variable_declaration_snippet(output_parameter, parameters)}
% endfor
% if ivi_dance_parameter is None:
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'], session_name='handle')})
        errors.handle_error(self, error_code, ignore_warnings=False)
        ${helper.get_method_return_snippet(f['parameters'])}
% else:
        ${ivi_dance_size_parameter['python_name']} = 0
        ${ivi_dance_parameter['ctypes_variable_name']} = ctypes.cast(ctypes.create_string_buffer(${ivi_dance_size_parameter['python_name']}), ctypes_types.${ivi_dance_parameter['ctypes_type']})
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'], session_name='handle')})
        errors.handle_error(self, error_code, ignore_warnings=True)
        ${ivi_dance_size_parameter['python_name']} = error_code
        ${ivi_dance_parameter['ctypes_variable_name']} = ctypes.cast(ctypes.create_string_buffer(${ivi_dance_size_parameter['python_name']}), ctypes_types.${ivi_dance_parameter['ctypes_type']})
        error_code = self.library.${c_function_prefix}${func_name}(${helper.get_library_call_parameter_snippet(f['parameters'], session_name='handle')})
        errors.handle_error(self, error_code, ignore_warnings=False)
        ${helper.get_method_return_snippet(f['parameters'])}
% endif
% endfor

