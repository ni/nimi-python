
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

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    def test_open(self):
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.disallow_close
        session = nimodinst.Session('')
        assert(session.handle == SESSION_NUM_FOR_TEST)
        self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert(session.handle == SESSION_NUM_FOR_TEST)
            self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_cannot_add_properties_to_session(self):
        with nimodinst.Session('') as session:
            try:
                session.nonexistent_property = 5
                assert False
            except TypeError as e:
                pass
            try:
                value = session.nonexistent_property  # noqa: F841
                assert False
            except AttributeError as e:
                pass

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

    def best_get_attribute_for_loop(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        int = 123
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = int
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.chassis_number
                assert(attr_int == int)
                from mock import call
                calls = [call(SESSION_NUM_FOR_TEST, 0, 11, ANY)]
                self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.assert_has_calls(calls)
                assert self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.call_count == 1

    def test_get_int_attribute(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        int = 123
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = int
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            attr_int = session.chassis_number[0]
            attr_int = session._get_installed_device_attribute_vi_int32(SESSION_NUM_FOR_TEST, 0, 11)
            assert(attr_int == int)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 11, ANY), call(SESSION_NUM_FOR_TEST, 0, 11, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.call_count == 2

    def test_get_string_attribute(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetInstalledDeviceAttributeViString']['attributeValue'] = string
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            attr_string = session.device_model[0]
            attr_string = session._get_installed_device_attribute_vi_string(SESSION_NUM_FOR_TEST, 0, 1)
            assert(attr_string == string)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 1, 0, None), call(SESSION_NUM_FOR_TEST, 0, 1, 15, ANY), call(SESSION_NUM_FOR_TEST, 0, 1, 0, None), call(SESSION_NUM_FOR_TEST, 0, 1, 15, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViString.call_count == 4

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
                session.chassis_number[0]
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
                session.chassis_number[0]
                assert len(w) == 1
                assert issubclass(w[0].category, nimodinst.NimodinstWarning)
                assert error_string in str(w[0].message)

    def test_get_extended_error_info(self):
        error_string = 'Error'
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            result = session._get_extended_error_info()
            assert result == error_string