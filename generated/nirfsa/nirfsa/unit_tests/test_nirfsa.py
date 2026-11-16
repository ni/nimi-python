import nirfsa.waveform_info
import numpy


def test_populate_samples_info():
    waveform_infos = []
    for i in range(1, 4):
        waveform_infos.append(nirfsa.waveform_info.WaveformInfo())
        waveform_infos[-1].actual_samples = i

    # 2D case (multi-record fetch): each row may be wider than actual_samples.
    sample_data = numpy.array([
        [0, 0, 0],
        [3, 4, 0],
        [6, 7, 8],
    ], dtype=numpy.float64)
    nirfsa.waveform_info._populate_samples_info(waveform_infos, sample_data)

    expected = [
        [0],
        [3, 4],
        [6, 7, 8],
    ]
    for i in range(len(waveform_infos)):
        assert list(waveform_infos[i].samples) == expected[i]
