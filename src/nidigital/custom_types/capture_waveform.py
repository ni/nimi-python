import collections.abc


class CaptureWaveform(collections.abc.Sequence):
    '''Used by fetch_capture_waveform() to return the capture waveform data'''
    def __init__(self, capture_waveform_data):
        self._capture_waveform_data = capture_waveform_data

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self._capture_waveform_data.tolist())

    def __len__(self):
        return len(self._capture_waveform_data)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return CaptureWaveform(self._capture_waveform_data[key])
        return self._capture_waveform_data[key]
