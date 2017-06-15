
import nidmm
import nidmm.tests.mock_library

from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch

@patch('nidmm.session.errors', spec_set=['_handle_error'])
@patch('nidmm.session.library', spec_set=['get_library'])
def test_simple_read(patched_library, patched_errors):
    MockLibrary = Mock(spec=nidmm.tests.mock_library.mock_library)
    patched_library.get_library.return_value = MockLibrary
    with nidmm.Session("Dev1") as session:
        MockLibrary.niDMM_InitWithOptions.assert_called_once_with(b'Dev1', 0, False, b'', ANY)
        patched_errors._handle_error.assert_called_once_with(MockLibrary, ANY, MockLibrary.niDMM_InitWithOptions.return_value)
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        #MockLibrary.niDMM_ConfigureMeasurementDigits.assert_called_once_with(42, nidmm.Function.DC_CURRENT.val, 1, 5.5)
        MockLibrary.niDMM_ConfigureMeasurementDigits.assert_called_once()
    #MockLibrary.niDMM_close.assert_called_once_with(42)
    #MockLibrary.niDMM_close.assert_called_once()
