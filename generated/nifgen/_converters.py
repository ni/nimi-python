from nifgen import visatype


def _convert_timedelta(value, library_type, scaling):
    scaled_value = value.total_seconds() * scaling

    if not library_type == visatype.ViReal64 and not library_type == visatype.ViReal32:  # ctype integer types don't convert to int from float so we need to
        scaled_value = int(scaled_value + 0.5)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_timedelta_to_microseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000000)



