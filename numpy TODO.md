* Generate `_into` flavors of all niscope fetch functions:
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Generate `_into` flavors of all niscope read functions
* Generate numpy flavor for define_user_standard_waveform(self, waveform_data_array) <- OPTIONAL
* Create "dispatching" methods for:
    * niscope.fetch
* Add `_into` flavor of nidmm fetch_waveform, in addition to regular list flavor
* `_into` methods should make the size parameter default to None, which means: get the size from the numpy.array and use that.
* Reorder cases in `get_ctype_variable_declaration_snippet` (no more 13.5 and such)
* `get_method_return_snippet` should leverage filter_parameters()
* Documentation
    * Doesn't show `_into` methods. Fix.
    * For nifgen.Session.write() it shows type as list of float
    * WriteWaveformDispatcher needs good docs, what about the types displayed?
    * Sometimes refers to private functions rather than public dispatchers.
* __str__() for matcher classes would be nice.
* "Dispatcher" functions generate code in Library but it's bogus and dead and confusing. We should skip doing that.

