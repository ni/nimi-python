import ctypes
import mock_helper
import nimodinst
import warnings

from mock import ANY
from mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_library_patcher = patch('nimodinst.library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nimodinst.session.library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niModInst_OpenInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_OpenInstalledDevicesSession
        self.disallow_close = self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_CloseInstalledDevicesSession

        self.side_effects_helper['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1

        self.iteration_device_looping = 0
        self.num_int_devices_looping = 3
        self.int_vals_device_looping = [123, 456, 789]
        self.num_string_devices_looping = 4
        self.string_vals_device_looping = ["Life", "liberty", "and", "happiness"]

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViString_looping(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if attribute_value_buffer_size == 0:
            return (len(self.string_vals_device_looping[self.iteration_device_looping]))
        t = nimodinst.ctypes_types.ViString_ctype(self.string_vals_device_looping[self.iteration_device_looping].encode('ascii'))
        attribute_value.value = ctypes.cast(t, nimodinst.ctypes_types.ViString_ctype).value
        self.iteration_device_looping += 1
        return 0

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViInt32_looping(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        attribute_value.contents.value = self.int_vals_device_looping[self.iteration_device_looping]
        self.iteration_device_looping += 1
        return 0

    # API Tests
    def test_open(self):
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.disallow_close
        session = nimodinst.Session('')
        assert(session._handle == SESSION_NUM_FOR_TEST)
        self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert(session._handle == SESSION_NUM_FOR_TEST)
            self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_iterating_for(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        with nimodinst.Session('') as session:
            assert len(session) == 2
            for d in session:
                pass

    def test_iterating_next(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        with nimodinst.Session('') as session:
            assert len(session) == 2
            d1 = session.next()
            d2 = session.next()
            assert d1 != d2

    def test_get_extended_error_info(self):
        error_string = 'Error'
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            result = session._get_extended_error_info()
            assert result == error_string

    def test_get_error_description_fails(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = -1
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        with nimodinst.Session('') as session:
            try:
                session[0].chassis_number
            except nimodinst.Error as e:
                assert e.code == -1  # we want the original error code from getting the attribute.
                assert e.description == "Failed to retrieve error description."

    def test_get_attribute_session(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            attr_int = session[0].chassis_number
            assert(attr_int == val)

    def test_get_attribute_vi_int32_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session[index].chassis_number
            index += 1
            assert(attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1])  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session[index].device_name
            index += 1
            assert(attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1])  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_session_no_index(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            try:
                session.chassis_number
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'chassis_number'"

    def test_get_attribute_vi_int32_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.chassis_number
                assert(attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1])  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.device_name
                assert(attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1])  # Have to subtract once since it was already incremented in the callback function

    # Error Tests
    def test_cannot_add_properties_to_session(self):
        with nimodinst.Session('') as session:
            try:
                session.nonexistent_property = 5
                assert False
            except TypeError as e:
                assert str(e).find(' is a frozen class') != -1
            try:
                session.nonexistent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'nonexistent_property'"

    def test_cannot_add_properties_to_device(self):
        with nimodinst.Session('') as session:
            try:
                session[0].nonexistent_property = 5
                assert False
            except TypeError as e:
                assert str(e) == 'nonexistent_property is not writable'
            try:
                session[0].nonexistent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'Device' object has no attribute 'nonexistent_property'"

    def test_vi_int32_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session[0].chassis_number = 5
                assert False
            except TypeError as e:
                assert str(e) == 'chassis_number is not writable'

    def test_vi_string_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session[0].device_name = "Not Possible"
                assert False
            except TypeError as e:
                assert str(e) == 'device_name is not writable'

    def test_int_attribute_error(self):
        error_code = -1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = error_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            try:
                session[0].chassis_number
                assert False
            except nimodinst.Error as e:
                assert e.code == error_code
                assert e.description == error_string

    def test_int_attribute_warning(self):
        warning_code = 1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = warning_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            with warnings.catch_warnings(record=True) as w:
                session[0].chassis_number
                assert len(w) == 1
                assert issubclass(w[0].category, nimodinst.NimodinstWarning)
                assert error_string in str(w[0].message)

