# -*- coding: utf-8 -*-
# This file is generated from NI-Sync API metadata version 20.0.0d0
attributes = {
    1150000: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the interface (board) number of this NI PXI-665x.  If there are multiple instances of the NI PXI-665x, each will have a unique interface number.'
        },
        'lv_property': '',
        'name': 'INTF_NUM',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150001: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the serial number of this NI PXI-665x interface.'
        },
        'lv_property': '',
        'name': 'SERIAL_NUM',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150100: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI0 terminal.'
        },
        'lv_property': '',
        'name': 'PFI0_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150101: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI1 terminal.'
        },
        'lv_property': '',
        'name': 'PFI1_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150102: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI2 terminal.'
        },
        'lv_property': '',
        'name': 'PFI2_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150103: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI3 terminal.'
        },
        'lv_property': '',
        'name': 'PFI3_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150104: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI4 terminal.'
        },
        'lv_property': '',
        'name': 'PFI4_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the voltage threshold for PFI5 terminal.'
        },
        'lv_property': '',
        'name': 'PFI5_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150106: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the tuning voltage for the OCXO/TCXO.  The OCXO/TCXO frequency can be varied over a small range.  The output frequency is adjusted using this tuning voltage.'
        },
        'lv_property': '',
        'name': 'OSCILLATOR_VOLTAGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150107: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the PXI_Clk10 Phase Adjust Voltage.  When using the PLL to lock PXI_CLK10 to an external reference clock, the phase between the clocks can be adjusted.  The time between rising edges of PXI_CLK10 and the input clock is minimized using this constant.'
        },
        'lv_property': '',
        'name': 'CLK10_PHASE_ADJUST',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150108: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the DDS VCXO Voltage.'
        },
        'lv_property': '',
        'name': 'DDS_VCXO_VOLTAGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150109: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the DDS Phase Adjust Voltage.'
        },
        'lv_property': '',
        'name': 'DDS_PHASE_ADJUST',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150110: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI0 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI0_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150111: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI1 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI1_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150112: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI2 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI2_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150113: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI3 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI3_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150114: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI4 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI4_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150115: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI5 terminal should be terminated with 1kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI5_1KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150116: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI0 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI0_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150117: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI1 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI1_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150118: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI2 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI2_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150119: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI3 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI3_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150120: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI4 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI4_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150121: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the PFI5 terminal should be terminated with 10kOhm impedance.'
        },
        'lv_property': '',
        'name': 'PFI5_10KOHM_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150200: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the synchronization clock source for the front zone (PFI and PFI_LVDS) terminals.'
        },
        'lv_property': '',
        'name': 'FRONT_SYNC_CLK_SRC',
        'resettable': True,
        'type': 'ViString'
    },
    1150201: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the synchronization clock source for the rear zone (PXI_Trig, PXI_Star, and PXIe_DStarB) terminals.'
        },
        'lv_property': '',
        'name': 'REAR_SYNC_CLK_SRC',
        'resettable': True,
        'type': 'ViString'
    },
    1150202: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the value for the first clock divisor'
        },
        'lv_property': '',
        'name': 'SYNC_CLK_DIV1',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150203: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the value for the second clock divisor'
        },
        'lv_property': '',
        'name': 'SYNC_CLK_DIV2',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150204: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the PXI_Trig terminal to use to reset the synchronization clock dividers.'
        },
        'lv_property': '',
        'name': 'SYNC_CLK_RST_PXITRIG_NUM',
        'resettable': True,
        'type': 'ViString'
    },
    1150205: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the frequency reference (in MHz) for PFI0'
        },
        'lv_property': '',
        'name': 'SYNC_CLK_PFI0_FREQ',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies whether or not the DDS clock dividers should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' attribute.\n"
        },
        'lv_property': '',
        'name': 'SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150207: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies whether or not the PFI0 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' attribute.\n"
        },
        'lv_property': '',
        'name': 'SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150208: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies whether or not the PXI_Clk10 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' attribute.\n"
        },
        'lv_property': '',
        'name': 'SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150300: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns a bitmap containing the PXI_Star terminal states.  Each bit represents the state of a PXI_STAR terminal.  Bit 0 corresponds to PXI_STAR0, bit 1 corresponds to PXI_STAR1, etc.  Bits 13 and above are not defined.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PXISTAR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150301: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns a bitmap containing the PXI_Trig terminal states.  Each bit represents the state of a PXI_TRIG terminal.  Bit 0 corresponds to PXI_TRIG0, bit 1 corresponds to PXI_TRIG1, etc.  Bits 8 and above are not defined.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PXITRIG',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150302: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns a bitmap containing the current PFI terminal states.  Each bit represents the state of a PFI terminal.  Bit 0 corresponds to PFI0, but 1 corresponds to PFI1, etc.  Bits 6 and above are not defined.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PFI',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150303: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A bitmap containing the current PXIe_DStarC terminal states. Each bit represents the state of a PXIe_DStarC terminal. Bit 0 corresponds to PXIe_DStarC0, bit 1 corresponds to PXIe_DStarC1, etc.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PXIEDSTARC',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150304: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A bitmap containing the current PFI_LVDS terminal states. Each bit represents the state of a PFI_LVDS terminal. Bit 0 corresponds to PFI_LVDS0, bit 1 corresponds to PFI_LVDS1, and bit 2 corresponds to PFI_LVDS2.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PFILVDS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150306: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the logical state of the PXIe_DStarB peripheral terminal.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PXIEDSTARBPERIPHERAL',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150307: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the logical state of the PXI_Star peripheral terminal.  This value is only valid when the board is in a peripheral slot.'
        },
        'lv_property': '',
        'name': 'TERMINAL_STATE_PXISTARPERIPHERAL',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150400: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the frequency (in Hertz) that the DDS should generate.'
        },
        'lv_property': '',
        'name': 'DDS_FREQ',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150401: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the signal source to be used when updating the DDS frequency.  The default is to update the frequency immediately, i.e. as soon as the frequency is set.  Alternatively, the DDS frequency can be committed to the DDS with an update pulse that arrives on a PXI_Trig terminal.'
        },
        'lv_property': '',
        'name': 'DDS_UPDATE_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150402: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the initial delay (in seconds) that the DDS should wait before it begins generating a specified frequency.  This attribute must be set prior to setting the DDS frequency, and it must be set using the same NI-Sync instrument driver session that sets the DDS frequency.'
        },
        'lv_property': '',
        'name': 'DDS_INITIAL_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150500: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the frequency that the PLL should lock to.  The PLL can be used to lock to frequencies between 1 MHz and 100 MHz, in multiples of 1 MHz.'
        },
        'lv_property': '',
        'name': 'CLKIN_PLL_FREQ',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150501: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether or not the connection between ClkIn and PXI_Clk10 should use the PLL circuit.  If this Boolean value is set to True, the PLL will be used to lock to the frequency at ClkIn when connecting to PXI_Clk10.  You must set this property before connecting the clock to PXI_Clk10_In.'
        },
        'lv_property': '',
        'name': 'CLKIN_USE_PLL',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150502: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns whether or not the PXI_Clk10 PLL is currently locked to a signal at the ClkIn terminal.'
        },
        'lv_property': '',
        'name': 'CLKIN_PLL_LOCKED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150503: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Setting this attribute to True increases the ClkOut amplitude.'
        },
        'lv_property': '',
        'name': 'CLKOUT_GAIN_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150504: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns whether or not the PXI_Clk10 signal is present on the PXI backplane.'
        },
        'lv_property': '',
        'name': 'PXICLK10_PRESENT',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150505: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Setting this attribute to True disables the ClkIn attenuation.'
        },
        'lv_property': '',
        'name': 'CLKIN_ATTENUATION_DISABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150600: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the state of the User LED.  Setting this Boolean value to True will turn on the User LED, and setting it to False will turn off the User LED.'
        },
        'lv_property': '',
        'name': 'USER_LED_STATE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150800: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A Boolean that specifies whether the configured time reference is currently providing a valid time signal.'
        },
        'lv_property': '',
        'name': 'TIMEREF_PRESENT',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150802: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A double that specifies the calculated offset, in seconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.'
        },
        'lv_property': '',
        'name': 'TIMEREF_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150804: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'A double that specifies a manual correction, in seconds, to apply to the time reference. Use this property to  calibrate the time reference manually to achieve better synchronization with the configured time reference.'
        },
        'lv_property': '',
        'name': 'TIMEREF_CORRECTION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150805: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'An integer that specifies the offset, in seconds, of the UTC timescale from the current time reference.'
        },
        'lv_property': '',
        'name': 'TIMEREF_UTC_OFFSET',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150806: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'A boolean that specifies whether the UTC offset of the current time reference is valid.'
        },
        'lv_property': '',
        'name': 'TIMEREF_UTC_OFFSET_VALID',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150807: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'An integer that is incremented when a synchronization message is received from the current time reference.   and the 1588 clock is a master.',
            'note': 'that synchronization messages are not received if the time reference is set to free running or if set to 1588'
        },
        'lv_property': '',
        'name': 'TIMEREF_LAST_SYNC_ID',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150808: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A double that specifies the calculated offset, in nanoseconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.'
        },
        'lv_property': '',
        'name': 'TIMEREF_OFFSET_NS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150809: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A string that represents the synchronization protocol being used by the selected time reference.'
        },
        'lv_property': '',
        'name': 'TIMEREF_SELECTED_TYPE',
        'resettable': True,
        'type': 'ViString'
    },
    1150810: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A string that represents the synchronization protocol being used by the time reference associated with this session.'
        },
        'lv_property': '',
        'name': 'TIMEREF_TYPE',
        'resettable': True,
        'type': 'ViString'
    },
    1150811: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A string that represents the name of the selected time reference.'
        },
        'lv_property': '',
        'name': 'TIMEREF_SELECTED_NAME',
        'resettable': True,
        'type': 'ViString'
    },
    1150812: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'A boolean that specifies whether the time reference associated with this session is enabled.'
        },
        'lv_property': '',
        'name': 'TIMEREF_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150813: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A boolean that represents whether the time reference associated with this session is the selected time reference.'
        },
        'lv_property': '',
        'name': 'TIMEREF_IS_SELECTED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150900: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'A Boolean that specifies whether the GPS antenna is properly connected.'
        },
        'lv_property': '',
        'name': 'GPS_ANTENNA_CONNECTED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150901: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'A Boolean that specifies whether GPS attempts to recalculate the current position at every system reboot. If not  configured to recalculate position, GPS permanently stores the current location. GPS never performs a self survey  until this flag is set.'
        },
        'lv_property': '',
        'name': 'GPS_RECALCULATE_POSITION',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150902: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'An integer that specifies the number of GPS satellites currently being tracked. A minimum of four satellites must be  visible for the onboard GPS receiver to perform a self survey. If using GPS as a Time Reference, four or more  satellites must be visible throughout timing measurements for the most accurate results.'
        },
        'lv_property': '',
        'name': 'GPS_SATELLITES_AVAILABLE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150903: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'An integer that specifies the percentage of the GPS self survey that has been completed. The onboard GPS receiver  performs position fixes during the self survey. The individual position fixes are accumulated and averaged over  the course of the self survey. The GPS Time Reference and location information are most accurate after the self  survey has completed and least accurate at the beginning of a self survey. If using GPS as a Time Reference, wait  until the self survey is complete prior to beginning timing measurements for the most accurate results. The onboard  GPS receiver requires at least four visible satellites to perform a self survey.'
        },
        'lv_property': '',
        'name': 'GPS_SELF_SURVEY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150904: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'A Boolean that specifies whether GPS is using mobile mode.  Enabling mobile mode allows the user to move the GPS  antenna and continuously calculate the current position and velocity.  If mobile mode is disabled, the antenna  must remain in a fixed position while the computer is on.  Timing accuracy is significantly improved with mobile  mode disabled.'
        },
        'lv_property': '',
        'name': 'GPS_MOBILE_MODE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150905: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'An integer enumeration that specifies the status of GPS.  This attribute can be queried to determine if GPS is in a  valid state before the application continues with other operations dependent on GPS. This attribute can also be used  to troubleshoot various GPS errors.'
        },
        'enum': 'GpsStatus',
        'lv_property': '',
        'name': 'GPS_STATUS',
        'resettable': True,
        'type': 'ViInt32'
    }
}
