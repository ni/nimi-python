* Add 'numpy_variable_name' to metadata and use it in
    * get_numpy_array_declaration_snippet
    * get_ctype_variable_declaration_snippet
    * _get_output_param_return_snippet
* Implement numpy.array as input parameter (i.e. write_waveform)
* Implement all niscope fetch functions
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Modify session_numpy_method.py.mako to be in the form fetch_into.
* Create "disaptching" methods for niscope.fetch, nifgen.create / write
* Add numpy flavor of nidmm fetch_waveform, in addition to regular list flavor
* Add NI-FAKE tests for these things
* Support generation of both default and numpy flavors of a method


