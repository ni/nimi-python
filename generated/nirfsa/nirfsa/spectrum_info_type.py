import ctypes
import nirfsa._visatype


# This class is an internal ctypes implementation detail that corresponds to
# niRFSA_spectrumInfo in the C API
class struct_niRFSA_spectrumInfo(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        ('initial_frequency', nirfsa._visatype.ViReal64),
        ('frequency_increment', nirfsa._visatype.ViReal64),
        ('number_of_spectral_lines', nirfsa._visatype.ViInt32),
        ('reserved1', nirfsa._visatype.ViReal64),
        ('reserved2', nirfsa._visatype.ViReal64),
        ('reserved3', nirfsa._visatype.ViReal64),
        ('reserved4', nirfsa._visatype.ViReal64),
        ('reserved5', nirfsa._visatype.ViReal64),
    ]

    def __init__(self, data=None, initial_frequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved1=0.0, reserved2=0.0,
                 reserved3=0.0, reserved4=0.0, reserved5=0.0):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.initial_frequency = data.initial_frequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self.reserved3 = data.reserved3
            self.reserved4 = data.reserved4
            self.reserved5 = data.reserved5
        else:
            self.initial_frequency = initial_frequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            self.reserved3 = reserved3
            self.reserved4 = reserved4
            self.reserved5 = reserved5


class SpectrumInfo:
    """Python-friendly wrapper for niRFSA spectrum info."""

    def __init__(self, data=None, initial_frequency=0.0, frequency_increment=0.0,
                 number_of_spectral_lines=0, reserved1=0.0, reserved2=0.0,
                 reserved3=0.0, reserved4=0.0, reserved5=0.0):
        if data is not None:
            self.initial_frequency = data.initial_frequency
            self.frequency_increment = data.frequency_increment
            self.number_of_spectral_lines = data.number_of_spectral_lines
            self.reserved1 = data.reserved1
            self.reserved2 = data.reserved2
            self.reserved3 = data.reserved3
            self.reserved4 = data.reserved4
            self.reserved5 = data.reserved5
        else:
            self.initial_frequency = initial_frequency
            self.frequency_increment = frequency_increment
            self.number_of_spectral_lines = number_of_spectral_lines
            self.reserved1 = reserved1
            self.reserved2 = reserved2
            self.reserved3 = reserved3
            self.reserved4 = reserved4
            self.reserved5 = reserved5

    def _create_copy(self, target_class):
        try:
            return target_class(
                initial_frequency=self.initial_frequency,
                frequency_increment=self.frequency_increment,
                number_of_spectral_lines=self.number_of_spectral_lines,
                reserved1=self.reserved1,
                reserved2=self.reserved2,
                reserved3=self.reserved3,
                reserved4=self.reserved4,
                reserved5=self.reserved5,
            )
        except TypeError:
            return target_class(data=self)

    def __repr__(self):
        return "{}.{}(initial_frequency={}, frequency_increment={}, number_of_spectral_lines={}, reserved1={}, reserved2={}, reserved3={}, reserved4={}, reserved5={})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.initial_frequency,
            self.frequency_increment,
            self.number_of_spectral_lines,
            self.reserved1,
            self.reserved2,
            self.reserved3,
            self.reserved4,
            self.reserved5,
        )

    def __str__(self):
        return self.__repr__()


def _populate_samples_info(spectrum_info, sample_data):
    '''Chunk up flat array of sample_data and copy each chunk into individual SpectrumInfo instance

    Args:
        spectrum_info (SpectrumInfo): SpectrumInfo class instance

        sample_data (Iterable of float): Spectrum sample data
    '''
    start = 0
    end = start + spectrum_info.number_of_spectral_lines
    spectrum_info.samples = sample_data[start:end]
