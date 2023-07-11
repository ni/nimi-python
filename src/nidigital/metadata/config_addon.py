# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.6.dev0',
    'latest_runtime_version_tested_against': '2023 Q2',
    'initial_release_year': '2019',
    'custom_types': [
        {
            'ctypes_type': '',
            'file_name': 'history_ram_cycle_information',
            'python_name': 'HistoryRAMCycleInformation'
        }
    ],
    'repeated_capabilities': [
        {
            'attr_for_docs_example': 'vil',
            'attr_type_for_docs_example': 'property',
            'prefix': '',
            'python_name': 'channels',
            'value_for_docs_example': 2,
        },
        {
            'attr_for_docs_example': 'vil',
            'attr_type_for_docs_example': 'property',
            'indices_for_docs_example': ["PinA", "PinB", "CPin"],
            'prefix': '',
            'python_name': 'pins',
            'value_for_docs_example': 2,
        },
        {
            'attr_for_docs_example': 'timing_absolute_delay',
            'attr_type_for_docs_example': 'property',
            'indices_for_docs_example': ["Dev1", "Dev2", "3rdDevice"],
            'prefix': '',
            'python_name': 'instruments',
            'value_for_docs_example': 5e-09,
        },
        {
            'attr_for_docs_example': 'exported_pattern_opcode_event_output_terminal',
            'attr_type_for_docs_example': 'property',
            'prefix': 'patternOpcodeEvent',
            'python_name': 'pattern_opcode_events',
            'value_for_docs_example': '/Dev1/PXI_Trig0',
        },
        {
            'attr_for_docs_example': 'conditional_jump_trigger_type',
            'attr_type_for_docs_example': 'property',
            'prefix': 'conditionalJumpTrigger',
            'python_name': 'conditional_jump_triggers',
            'value_for_docs_example': 'nidigital.TriggerType.DIGITAL_EDGE',
            'value_type_for_docs_example': 'enum',
        },
        {
            'attr_for_docs_example': 'disable_sites',
            'attr_type_for_docs_example': 'method',
            'prefix': 'site',
            'python_name': 'sites',
            'value_for_docs_example': None,
        },
        {
            'attr_for_docs_example': 'exported_rio_event_output_terminal',
            'attr_type_for_docs_example': 'property',
            'prefix': 'RIOEvent',
            'python_name': 'rio_events',
            'value_for_docs_example': '/Dev1/PXI_Trig0',
        },
        {
            'attr_for_docs_example': 'rio_trigger_type',
            'attr_type_for_docs_example': 'property',
            'prefix': 'RIOTrigger',
            'python_name': 'rio_triggers',
            'value_for_docs_example': 'nidigital.TriggerType.DIGITAL_EDGE',
            'value_type_for_docs_example': 'enum',
        }
    ],
}
