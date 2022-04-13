import array
import niscope.waveform_info


def test_populate_samples_info():
    waveform_infos = []
    for i in range(1, 4):
        waveform_infos.append(niscope.waveform_info.WaveformInfo())
        waveform_infos[-1]._actual_samples = i

    sample_data = array.array("d", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    niscope.waveform_info._populate_samples_info(waveform_infos, sample_data, 3)

    expected = [
        array.array("d", [0]),
        array.array("d", [3, 4]),
        array.array("d", [6, 7, 8]),
    ]
    for i in range(len(waveform_infos)):
        assert waveform_infos[i]._actual_samples is None
        assert waveform_infos[i].samples == expected[i]


def test_populate_channel_and_record_info():
    waveform_infos = []
    for i in range(6):
        waveform_infos.append(niscope.waveform_info.WaveformInfo())

    channels = ["Dev1/4", "Dev2/2"]
    records = [0, 1, 2]
    niscope.waveform_info._populate_channel_and_record_info(
        waveform_infos, channels, records
    )

    expected_channels = ["Dev1/4", "Dev2/2"] * len(records)
    expected_records = [0, 0, 1, 1, 2, 2]

    for i in range(len(waveform_infos)):
        assert waveform_infos[i].channel == expected_channels[i]
        assert waveform_infos[i].record == expected_records[i]
