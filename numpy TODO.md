* Implement numpy.array as input parameter (i.e. write_waveform)
* Implement all niscope fetch functions
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Create "disaptching" methods for niscope.fetch, nifgen.create / write
* Add numpy flavor of nidmm fetch_waveform, in addition to regular list flavor
* Add NI-FAKE tests for these things
* "into" methods should make the size parameter default to None, which means: get the size from the numpy.array and use that.
* Reorder cases in get_ctype_variable_declaration_snippet (no more 13.5 and such)
* Refactor get_ctype_variable_declaration_snippet
* get_method_return_snippet should leverage filter_parameters()
* Documentation doesn't show "_into" methods. Not clear how to best do this.
* session_numpy_method.py.mako is not a very descriptive name, rename once we add the template for creating waveforms.
* __str__() for matcher classes would be nice.
