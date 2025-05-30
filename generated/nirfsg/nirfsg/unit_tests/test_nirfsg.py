import nirfsg

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

SESSION_NUM_FOR_TEST = 42


class TestSession:

    class PatchedLibraryInterpreter(nirfsg._library_interpreter.LibraryInterpreter):
        def __init__(self, encoding):
            for f in dir(self):
                if not f.startswith("_") and f not in {'get_session_handle', 'set_session_handle'}:
                    setattr(self, f, MagicMock(spec_set=getattr(self, f), side_effect=_mock_helper.MockFunctionCallError(f)))

    def setup_method(self, method):
        self.patched_library_interpreter = self.PatchedLibraryInterpreter(None)
        self.patched_library_interpreter_ctor = patch('nirfsg.session._library_interpreter.LibraryInterpreter', return_value=self.patched_library_interpreter)
        self.patched_library_interpreter_ctor.start()

        # We don't actually call into the nitclk DLL, but we do need to mock the function since it is called
        self.tclk_patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=None)
        self.tclk_patched_library_singleton_get.start()

        def interpreter_init(*args, **kwargs):
            self.patched_library_interpreter._close_on_exit = True
            return SESSION_NUM_FOR_TEST

        self.patched_library_interpreter.init_with_options.side_effect = interpreter_init
        self.patched_library_interpreter.close.side_effect = [None]

        # Mock lock/unlock
        self.patched_library_interpreter.lock.side_effect = lambda *args: None
        self.patched_library_interpreter.unlock.side_effect = lambda *args: None

    def teardown_method(self, method):
        self.patched_library_interpreter_ctor.stop()

    def test_attribute_get_for_repeated_capability_custom_object(self):
        string = 'markerterminal'
        self.patched_library_interpreter.get_attribute_vi_string.side_effect = [string]
        with nirfsg.Session('dev1', id_query=False, reset_device=False) as session:
            value = session.markers['0'].marker_event_terminal_name  # noqa: F841
        # Verify that the repeated capability string is '0'
        self.patched_library_interpreter.get_attribute_vi_string.assert_called_once_with('marker0', 1150115)

    def test_invalid_attribute_set_for_repeated_capability_custom_object(self):
        with nirfsg.Session('dev1', id_query=False, reset_device=False) as session:
            try:
                session.deembedding_port['port0'].amplitude_settling = 2
            except AttributeError:
                pass
