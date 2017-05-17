

attributes = []
config = {
   'library_windows': {'32': 'nidmm_32.dll', '64': 'nidmm_64.dll'},
   'library_linux': {'32': 'nidmm_32.so', '64': 'nidmm_64.so'},
}

functions = [
   {
      'name': 'niDMM_init',
      'ret_type': 'ViStatus',
      'params': [
         {'name': 'resourceName',
          'type': 'ViRsrc',
          'direction': 'in'},
         {'name': 'IDQuery',
          'type': 'ViBoolean',
          'direction': 'in'},
         {'name': 'reset',
          'type': 'ViBoolean',
          'direction': 'in'},
         {'name': 'newVi',
          'type': 'ViSession',
          'direction': 'out'},
      ]
   },
   {
      'name': 'niDMM_close',
      'ret_type': 'ViStatus',
      'params': [
         {'name': 'vi',
          'type': 'ViSession',
          'direction': 'in'},
      ]
   },
   {
      'name': 'niDMM_InitExtCal',
      'ret_type': 'ViStatus',
      'params': [
         {'name': 'resourceName',
          'type': 'ViRsrc',
          'direction': 'in'},
         {'name': 'password',
          'type': 'ViChar',
          'direction': 'in'},
         {'name': 'newVi',
          'type': 'ViSession',
          'direction': 'out'},
      ]
   },
   {
      'name': 'niDMM_CloseExtCal',
      'ret_type': 'ViStatus',
      'params': [
         {'name': 'vi',
          'type': 'ViSession',
          'direction': 'in'},
         {'name': 'action',
          'type': 'ViInt32',
          'direction': 'in'},
      ]
   },
   {
      'name': 'niDMM_ConfigureMeasurementDigits',
      'ret_type': 'ViStatus',
      'params': [
         {'name': 'vi',
          'type': 'ViSession',
          'direction': 'in'},
         {'name': 'measFunction',
          'type': 'ViInt32',
          'direction': 'in'},
         {'name': 'range',
          'type': 'ViReal64',
          'direction': 'in'},
         {'name': 'resolutionDigits',
          'type': 'ViReal64',
          'direction': 'in'},
      ]
   },
]


