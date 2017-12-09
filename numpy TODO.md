* Implement numpy.array as input parameter (i.e. write_waveform)
* Implement all niscope fetch functions
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Create "disaptching" methods for niscope.fetch, nifgen.create / write
* Add numpy flavor of nidmm fetch_waveform, in addition to regular list flavor
* Add NI-FAKE tests for these things
* Support generation of both default and numpy flavors of a method
* Documentation for "into" methods uses wrong name and parameter list.
* "into" methods should make the size parameter default to None, which means: get the size from the numpy.array and use that.
* Reorder cases in get_ctype_variable_declaration_snippet (no more 13.5 and such)
* Refactor get_ctype_variable_declaration_snippet
* Unit test for foo_into() with wrong types, wrong order.
* get_method_return_snippet should leverage filter_parameters()