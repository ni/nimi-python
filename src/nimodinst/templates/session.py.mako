# This file was generated
<%
    import helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes
%>\

import ctypes
from ${module_name} import errors
from ${module_name} import library
from ${module_name} import enums


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return _get_installed_device_attribute_vi_int32(self.channel, self.attribute_id)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_installed_device_attribute_vi_string(self.channel, self.attribute_id)


class Session(object):
    '''${config['session_description']}'''

% for attribute in attributes:
    ${attribute.lower()} = Attribute${attributes[attribute]['type']}(${attributes[attribute]['id']})
% endfor

    def __init__(self, driver):
        self.vi = 0
        self.item_count = 0
        self.library = library.get_library()
        get_session = ctypes.c_ulong(0)
        get_item_count = ctypes.c_ulong(0)
        error_code = self.library.${c_function_prefix}OpenInstalledDevicesSession(driver, ctypes.pointer(get_session), ctypes.pointer(get_item_count))
        self.vi = get_session.value
        self.item_count = get_item_count.value
        errors._handle_error(self.library, self.session, error_code)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.session_handle.value != 0):
            error_code = self.library.${c_function_prefix}close(self.session_handle)
            if(error_code < 0):
                # TODO(marcoskirsch): This will occur when session is "stolen". Maybe don't even bother with printing?
                print("Failed to close session.")
            self.session_handle = ctypes.c_ulong(0)


    ''' These are code-generated '''

    #TODO (marcoskirsch): attribute methods will be like "_set_attribute_vi_boolean", should be _set_attribute_ViBoolean. Open issue about it.
<%
    functions = template_parameters['metadata'].functions
    functions = helper.extract_codegen_functions(functions)
    functions = helper.add_all_metadata(functions)
%>\
% for f in functions:
<%
    input_parameters = helper.extract_input_parameters(f['parameters'])
    output_parameters = helper.extract_output_parameters(f['parameters'])
    enum_input_parameters = helper.extract_enum_parameters(input_parameters)
%>
    def ${f['python_name']}(${helper.get_method_parameters_snippet(input_parameters)}):
% for parameter in enum_input_parameters:
        ${helper.get_enum_type_check_snippet(parameter)}
% endfor
% for output_parameter in output_parameters:
        ${output_parameter['ctypes_variable_name']} = ${output_parameter['ctypes_type']}(0)
% endfor
        error_code = self.library.${c_function_prefix}${f['name']}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors._handle_error(self.library, self.session_handle, error_code)
        ${helper.get_method_return_snippet(output_parameters)}
% endfor


    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):
        error_code = self.library.${c_function_prefix}GetInstalledDeviceAttributeViString(self.vi, index, attribute_id, 0, None)
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if(errors._is_error(error_code)): raise errors.Error(self.library, self.session_handle, error_code)
        buffer_size = error_code
        value = ctypes.create_string_buffer(buffer_size)
        error_code = self.library.${c_function_prefix}GetInstalledDeviceAttributeViString(self.vi, index, attribute_id, buffer_size, value)
        errors._handle_error(self.library, self.session_handle, error_code)
        return value.value.decode("ascii")
