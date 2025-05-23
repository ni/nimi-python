# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    # TODO (ni-jfitzger): delete this override once ConfigureLCRCompensation is in nidcpower.proto. See https://github.com/ni/nimi-python/issues/1920
    'ConfigureLCRCompensation': {
        'included_in_proto': False,
    },
    # TODO (ni-jfitzger): delete this override once GetLCRCompensationData is in nidcpower.proto. See https://github.com/ni/nimi-python/issues/1920
    'GetLCRCompensationData': {
        'included_in_proto': False,
    },
}

functions_additional_create_advanced_sequence = {
    'FancyCreateAdvancedSequence': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'create_advanced_sequence',
        'method_templates': [
            { 'session_filename': 'fancy_advanced_sequence', 'library_interpreter_filename': 'none', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'SequenceName',
                'type': 'ViString',
                'documentation': {
                    'description': 'Specifies the name of the sequence to create.'
                },
            },
            {
                'direction': 'in',
                'name': 'PropertyNames',
                'type': 'ViString[]',
                'documentation': {
                    'description': 'Specifies the names of the properties you reconfigure per step in the advanced sequence. For more information about properties that can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing, search ni.com for Supported Properties by Device.',
                },
            },
            {
                'direction': 'in',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean',
                'default_value': True,
                'documentation': { 'description': 'Specifies that this current sequence is active.', },
            },
        ],
        'documentation':
        {
            'description': '\nCreates an empty advanced sequence. Call the\nniDCPower_CreateAdvancedSequenceStepWithChannels function to add steps to the\nactive advanced sequence.\n\nYou can create multiple advanced sequences in a session.\n\n**Support for this function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nNI-DCPower programming states.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceStepWithChannels\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
    },
}
