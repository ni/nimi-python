
import nidmm

def test_simple_read():
    with nidmm.Session("Dev1", mocking=True) as session:
        session.configure_measurement_digits(nidmm.Function.DC_CURRENT, 1, 5.5)

