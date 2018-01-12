from nidmm import visatype


def _timedelta_converter(value, library_type, scaling):
    if str(type(value)).find("'datetime.timedelta'") != -1:
        scaled_value = value.total_seconds() * scaling
    else:
        scaled_value = value

    if not library_type == visatype.ViReal64:  # ctype integer types don't convert to int from float so we need to
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def timedelta_converter_seconds(value, library_type):
    return _timedelta_converter(value, library_type, 1)


def timedelta_converter_milliseconds(value, library_type):
    return _timedelta_converter(value, library_type, 1000)


def timedelta_converter_microseconds(value, library_type):
    return _timedelta_converter(value, library_type, 1000000)



