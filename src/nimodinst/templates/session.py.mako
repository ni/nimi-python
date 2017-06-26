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
from ${module_name} import ctypes_types


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id):
        self._owner = owner
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id):
        self._owner = owner
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(index, self._attribute_id)


class Session(object):
    '''${config['session_description']}'''

    def __init__(self, driver):
% for attribute in attributes:
        self.${attribute.lower()} = Attribute${attributes[attribute]['type']}(self, ${attributes[attribute]['id']})
% endfor

        self.vi = 0
        self.item_count = 0
        self.library = library.get_library()
        get_session = ctypes_types.ViSession_ctype(0)
        get_item_count = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.${c_function_prefix}OpenInstalledDevicesSession(driver.encode('ascii'), ctypes.pointer(get_session), ctypes.pointer(get_item_count))
        self.vi = get_session.value
        self.item_count = get_item_count.value
        errors._handle_error(self.library, self.vi, error_code.value)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_installed_devices_session()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.vi != 0):
            error_code = self.library.${c_function_prefix}close(self.vi)
            if(error_code.value < 0):
                # TODO(marcoskirsch): This will occur when session is "stolen". Maybe don't even bother with printing?
                print("Failed to close session.")
            self.vi = 0


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
        ${output_parameter['ctypes_variable_name']} = ctypes_types.${output_parameter['ctypes_type']}(0)
% endfor
        error_code = self.library.${c_function_prefix}${f['name']}(${helper.get_library_call_parameter_snippet(f['parameters'])})
        errors._handle_error(self.library, self.vi, error_code.value)
        ${helper.get_method_return_snippet(output_parameters)}
% endfor


    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):
        error_code = self.library.${c_function_prefix}GetInstalledDeviceAttributeViString(self.vi, index, attribute_id, 0, None)
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if(errors._is_error(error_code.value)): raise errors.Error(self.library, self.vi, error_code.value)
        buffer_size = error_code
        value = ctypes.create_string_buffer(buffer_size.value)
        error_code = self.library.${c_function_prefix}GetInstalledDeviceAttributeViString(self.vi, index, attribute_id, buffer_size.value, value)
        errors._handle_error(self.library, self.vi, error_code.value)
        return value.value.decode("ascii")
