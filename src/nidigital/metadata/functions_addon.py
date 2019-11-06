# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'FetchCaptureWaveformU32': {
        'codegen_method': 'library-only',  # We have a "fancy" wrapper for this so and we cannot use the generated python method, so only generate into the library
    },
}

functions_additional_fetch_capture_waveform = {
    'FancyFetchCaptureWaveform': {
        'python_name': 'fetch_capture_waveform',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_capture_waveform',
            }
        ],
       'documentation': {
            'description': '\nReturns a list of named tuples (Waveform) that <FILL IN THE BLANK HERE>\n\nFields in Waveform:\n\n- **site** (int)\n- **data** (array.array of int)\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'python_type': 'float or datetime.timedelta',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **site** (int)\n- **data** (array.array of int)\n'
                },
                'name': 'waveform',
                'python_type': 'Waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViUInt32[]'
            },
        ],
    },
}
