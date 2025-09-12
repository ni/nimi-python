# src/nirfsg/templates/session.py/test_write_arb_waveform.py.mako

import numpy
import pytest
from nirfsg.session import Session

class TestWriteArbWaveformSystem:

    def setup_method(self):
        # Replace with actual device name or use a mock if needed
        self.session = Session('FakeDevice')

    def teardown_method(self):
        self.session.close()

    def test_write_arb_waveform_complex128(self):
        arr = numpy.full((10,), 1.0 + 2.0j, dtype=numpy.complex128)
        # Should dispatch to _write_arb_waveform_complex_f64
        self.session.write_arb_waveform('wf1', arr, False)

    def test_write_arb_waveform_complex64(self):
        arr = numpy.full((10,), 1.0 + 2.0j, dtype=numpy.complex64)
        # Should dispatch to _write_arb_waveform_complex_f32
        self.session.write_arb_waveform('wf2', arr, False)

    def test_write_arb_waveform_int16(self):
        arr = numpy.full((10,), 42, dtype=numpy.int16)
        # Should dispatch to _write_arb_waveform_complex_i16
        self.session.write_arb_waveform('wf3', arr)

    def test_write_arb_waveform_unsupported_dtype(self):
        arr = numpy.full((10,), 42, dtype=numpy.float32)
        with pytest.raises(TypeError):
            self.session.write_arb_waveform('wf4', arr)

    def test_write_arb_waveform_non_numpy(self):
        arr = [1.0 + 2.0j] * 10
        with pytest.raises(TypeError):
            self.session.write_arb_waveform('wf5', arr)