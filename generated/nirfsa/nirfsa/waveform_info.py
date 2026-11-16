import ctypes
import nirfsa._visatype


# This class is an internal ctypes implementation detail that corresponds to
# niRFSA_wfmInfo in the C API
class struct_niRFSA_wfmInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('absolute_initial_x', nirfsa._visatype.ViReal64),
        ('relative_initial_x', nirfsa._visatype.ViReal64),
        ('x_increment', nirfsa._visatype.ViReal64),
        ('actual_samples', nirfsa._visatype.ViInt64),
        ('offset', nirfsa._visatype.ViReal64),
        ('gain', nirfsa._visatype.ViReal64),
        ('reserved1', nirfsa._visatype.ViReal64),
        ('reserved2', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2


class WaveformInfo:
    """Python-friendly wrapper for niRFSA waveform info."""

    def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0,
                 x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0,
                 reserved1=0.0, reserved2=0.0):
        if data is not None:
            self.absolute_initial_x = data.absolute_initial_x
            self.relative_initial_x = data.relative_initial_x
            self.x_increment = data.x_increment
            self.actual_samples = data.actual_samples
            self.offset = data.offset
            self.gain = data.gain
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
        else:
            self.absolute_initial_x = absolute_initial_x
            self.relative_initial_x = relative_initial_x
            self.x_increment = x_increment
            self.actual_samples = actual_samples
            self.offset = offset
            self.gain = gain
            self.reserved1 = reserved1
            self.reserved2 = reserved2

    def _create_copy(self, target_class):
        try:
            return target_class(
                absolute_initial_x=self.absolute_initial_x,
                relative_initial_x=self.relative_initial_x,
                x_increment=self.x_increment,
                actual_samples=self.actual_samples,
                offset=self.offset,
                gain=self.gain,
                reserved1=self.reserved1,
                reserved2=self.reserved2,
            )
        except TypeError:
            return target_class(data=self)

    def __repr__(self):
        return "{}.{}(absolute_initial_x={}, relative_initial_x={}, x_increment={}, actual_samples={}, offset={}, gain={}, reserved1={}, reserved2={})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.absolute_initial_x,
            self.relative_initial_x,
            self.x_increment,
            self.actual_samples,
            self.offset,
            self.gain,
            self.reserved1,
            self.reserved2,
        )

    def __str__(self):
        return self.__repr__()


def _populate_samples_info(waveform_infos, sample_data):
    '''Chunk up flat array of sample_data and copy each chunk into individual WaveformInfo instance

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        sample_data (Iterable of float): Waveform sample data
    '''
    if hasattr(sample_data, 'ndim') and sample_data.ndim == 2:
        # 2D case (multi-record fetch): sample_data[i] is a 1D view of row i.
        # Slice to exact actual_samples to handle rows wider than actual_samples (e.g. int16).
        for i in range(len(waveform_infos)):
            actual_samples = waveform_infos[i].actual_samples
            waveform_infos[i].samples = sample_data[i, :actual_samples]

