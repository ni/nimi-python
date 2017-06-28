
import nidmm
import nidmm.tests.mock_library

from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import create_autospec

@patch('nidmm.session.errors', spec_set=['_handle_error'])
@patch('nidmm.ctypes_library.nidmm_ctypes_library', autospec=True)
@patch('nidmm.session.library', spec_set=['get_library'])
def test_simple_read(patched_library, patched_ctypes_library, patched_errors):
    patched_errors._handle_error.return_value = 0

    patched_library.get_library.return_value = patched_ctypes_library

    nidmm.tests.mock_library.set_side_effects_and_return_values(patched_ctypes_library)

    with nidmm.Session("Dev1") as session:
        assert(session.vi == 42)
        vi = session.vi # We have to save the session number so we cal validate the close call
        patched_ctypes_library.niDMM_InitWithOptions.assert_called_once_with(b'Dev1', 0, False, b'', ANY)
        patched_errors._handle_error.assert_called_once_with(patched_ctypes_library, session.vi, patched_ctypes_library.niDMM_InitWithOptions.return_value)

        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        patched_ctypes_library.niDMM_ConfigureMeasurementDigits.assert_called_once_with(session.vi, nidmm.Function.DC_CURRENT.value, 1, 5.5)
        patched_errors._handle_error.assert_called_with(patched_ctypes_library, ANY, patched_ctypes_library.niDMM_InitWithOptions.return_value)
    patched_ctypes_library.niDMM_close.assert_called_once_with(vi)

