
import mock_helper
import nimodinst

from mock import ANY
from mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_library_patcher = patch('nimodinst.library.Library', autospec=True)
        self.patched_library = self.patched_library_patcher.start()
        self.patched_library_singleton_get = patch('nimodinst.session.library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()
        self.errors_patcher = patch('nimodinst.session.errors', spec_set=['handle_error', '_is_error'])
        self.patched_errors = self.errors_patcher.start()
        self.patched_errors._is_error.return_value = 0

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niModInst_OpenInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_OpenInstalledDevicesSession
        self.disallow_close = self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_CloseInstalledDevicesSession

        self.side_effects_helper['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1

    def teardown_method(self, method):
        self.errors_patcher.stop()
        self.patched_library_singleton_get.stop()
        self.patched_library_patcher.stop()

    def test_open(self):
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.disallow_close
        session = nimodinst.Session('')
        assert(session.handle == SESSION_NUM_FOR_TEST)
        self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
        self.patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niModInst_OpenInstalledDevicesSession.return_value, ignore_warnings=False)

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert(session.handle == SESSION_NUM_FOR_TEST)
            self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
            self.patched_errors.handle_error.assert_called_once_with(session, self.patched_library.niModInst_OpenInstalledDevicesSession.return_value, ignore_warnings=False)
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

    def test_get_attribute_for_loop(self):
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
            
    def test_get_int_attribute_private(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        int = 123
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = int
        with nimodinst.Session('') as session:
            attr_int = session._get_installed_device_attribute_vi_int32(SESSION_NUM_FOR_TEST, 0, 5)
            assert(attr_int == int)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 5, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.call_count == 1

    def test_get_int_attribute(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        int = 123
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = int
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            attr_int = session.chassis_number[0]
            assert(attr_int == int)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 11, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.call_count == 1

    def test_get_string_attribute_private(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetInstalledDeviceAttributeViString']['attributeValue'] = string
        with nimodinst.Session('') as session:
            attr_string = session._get_installed_device_attribute_vi_string(SESSION_NUM_FOR_TEST, 0, 5)
            assert(attr_string == string)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 5, 0, None), call(SESSION_NUM_FOR_TEST, 0, 5, 15, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViString.call_count == 2

    def test_get_string_attribute(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViString
        string = 'Testing is fun?'
        self.side_effects_helper['GetInstalledDeviceAttributeViString']['attributeValue'] = string
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            attr_string = session.device_model[0]
            assert(attr_string == string)
            from mock import call
            calls = [call(SESSION_NUM_FOR_TEST, 0, 1, 0, None), call(SESSION_NUM_FOR_TEST, 0, 1, 15, ANY)]
            self.patched_library.niModInst_GetInstalledDeviceAttributeViString.assert_has_calls(calls)
            assert self.patched_library.niModInst_GetInstalledDeviceAttributeViString.call_count == 2

    def best_int_attribute_error_on_non_existant_device(self):
        error_code = -1234
        error_string = 'Error'
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = 0
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = error_code

        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = error_code
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            device = len(session) + 1
            try:
                #session.chassis_number[device]
                session._get_installed_device_attribute_vi_int32(SESSION_NUM_FOR_TEST, 2, 11)
                from mock import call
                calls = [call(SESSION_NUM_FOR_TEST, 2, 11, ANY)]
                self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.assert_has_calls(calls)
                assert self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.call_count == 1
                assert False
            except nimodinst.Error as e:
                assert e.code == error_code
                assert e.description == error_string
