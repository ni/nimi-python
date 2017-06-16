
import nidmm
import nidmm.tests.mock_library

from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import create_autospec

import ctypes

@patch('nidmm.session.errors', spec_set=['_handle_error'])
@patch('nidmm.session.library', spec_set=['get_library'])
def test_init(patched_library, patched_errors):
    MockLibrary = create_autospec(nidmm.tests.mock_library.mock_library, instance=True)

    nidmm.tests.mock_library.set_side_effects_and_return_values(MockLibrary)

    patched_library.get_library.return_value = MockLibrary

    with nidmm.Session("Dev1") as session:
        assert(session.session_handle.value == 42)
        MockLibrary.niDMM_InitWithOptions.assert_called_once_with(b'Dev1', 0, False, b'', ANY)
#        patched_errors._handle_error.assert_called_once_with(MockLibrary, ANY, MockLibrary.niDMM_InitWithOptions.return_value)
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        MockLibrary.niDMM_ConfigureMeasurementDigits.assert_called_once_with(ctypes.c_ulong(42), nidmm.Function.DC_CURRENT.value, 1, 5.5)
    MockLibrary.niDMM_close.assert_called_once_with(ctypes.c_ulong(42))


