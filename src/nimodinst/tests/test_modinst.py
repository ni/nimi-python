
import mock_helper
import nimodinst

from mock import ANY
from mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession(object):
    def setup_method(self, method):
        self.patched_ctypes_library_patcher = patch('nimodinst.ctypes_library.NimodinstCtypesLibrary', autospec=True)
        self.patched_ctypes_library = self.patched_ctypes_library_patcher.start()
        self.patched_get_library_patcher = patch('nimodinst.session.library.get_library', return_value=self.patched_ctypes_library)
        self.patched_get_library_patcher.start()
        self.errors_patcher = patch('nimodinst.session.errors', spec_set=['_handle_error', '_is_error'])
        self.patched_errors = self.errors_patcher.start()
        self.patched_errors._is_error.return_value = 0

        self.side_effects_helper = mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_ctypes_library)
        self.patched_ctypes_library.niModInst_OpenInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_OpenInstalledDevicesSession
        self.disallow_close = self.patched_ctypes_library.niModInst_CloseInstalledDevicesSession.side_effect
        self.patched_ctypes_library.niModInst_CloseInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_CloseInstalledDevicesSession

        self.side_effects_helper['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
        self.side_effects_helper['OpenInstalledDevicesSession']['item_count'] = 1

    def teardown_method(self, method):
        self.errors_patcher.stop()
        self.patched_get_library_patcher.stop()
        self.patched_ctypes_library_patcher.stop()

    def test_open(self):
        self.patched_ctypes_library.niModInst_CloseInstalledDevicesSession.side_effect = self.disallow_close
        session = nimodinst.Session('')
        assert(session.handle == SESSION_NUM_FOR_TEST)
        self.patched_ctypes_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
        self.patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niModInst_OpenInstalledDevicesSession.return_value)

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_ctypes_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert(session.handle == SESSION_NUM_FOR_TEST)
            self.patched_ctypes_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
            self.patched_errors._handle_error.assert_called_once_with(session, self.patched_ctypes_library.niModInst_OpenInstalledDevicesSession.return_value)
        self.patched_ctypes_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

    def test_cannot_add_properties_to_session(self):
        with nimodinst.Session('') as session:
            try:
                session.nonexistent_property = 5
                assert False
            except TypeError as e:
                print(e)
                pass
            try:
                value = session.nonexistent_property  # noqa: F841
                assert False
            except AttributeError as e:
                print(e)
                pass

    def test_iterating(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['item_count'] = 2
        with nimodinst.Session('') as session:
            assert len(session) == 2
            for d in session:
                pass
