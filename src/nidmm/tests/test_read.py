
import nidmm
from unittest.mock import patch

#@patch('nidmm.library', autospec=True)
def test_simple_read():
    with nidmm.Session("Dev1", mocking=True) as session:
        patch.object(session.library, autospec=True)
        session.Initialize()
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)
        session.read()

