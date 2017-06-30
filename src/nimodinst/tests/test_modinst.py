
import nimodinst
import nimodinst.tests.mock_helper as mock_helper

from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import create_autospec
from unittest.mock import DEFAULT

SESSION_NUM_FOR_TEST = 42

@patch('nimodinst.session.errors', spec_set=['_handle_error'])
@patch('nimodinst.ctypes_library.nimodinst_ctypes_library', autospec=True)
@patch('nimodinst.session.library', spec_set=['get_library'])
def test_simple_read(patched_library, patched_ctypes_library, patched_errors):
    patched_errors._handle_error.return_value = 0

    patched_library.get_library.return_value = patched_ctypes_library

    nimodinst_side_effects = mock_helper.side_effects_helper()
    nimodinst_side_effects.set_side_effects_and_return_values(patched_ctypes_library)

    patched_ctypes_library.niModInst_OpenInstalledDevicesSession.side_effect = nimodinst_side_effects.niModInst_OpenInstalledDevicesSession
    patched_ctypes_library.niModInst_CloseInstalledDevicesSession.side_effect = nimodinst_side_effects.niModInst_CloseInstalledDevicesSession

    nimodinst_side_effects['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
    nimodinst_side_effects['OpenInstalledDevicesSession']['item_count'] = 1

    with nimodinst.Session("") as session:
        assert(session.handle == SESSION_NUM_FOR_TEST)
        patched_ctypes_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(b'', ANY, ANY)
        patched_errors._handle_error.assert_called_once_with(session, patched_ctypes_library.niModInst_OpenInstalledDevicesSession.return_value)

    patched_ctypes_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(SESSION_NUM_FOR_TEST)

