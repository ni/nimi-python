
import nidmm
import nidmm.tests.mock_library

from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import create_autospec

@patch('nidmm.session.errors', spec_set=['_handle_error'])
@patch('nidmm.ctypes_library.nidmm_ctypes_library', autospec=True)
def test_simple_read(patched_ctypes_library, patched_errors):
    patched_errors._handle_error.return_value = 0
    nidmm.tests.mock_library.set_side_effects_and_return_values(patched_ctypes_library)
    with nidmm.Session("Dev1") as session:
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)

