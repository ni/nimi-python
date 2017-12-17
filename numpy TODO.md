* Generate `_into` flavors of all niscope fetch functions:
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Create "dispatching" methods for:
    * niscope.fetch
* `_into` methods should make the size parameter default to None, which means: get the size from the numpy.array and use that.
* Reorder cases in `get_ctype_variable_declaration_snippet` (no more 13.5 and such)
* `get_method_return_snippet` should leverage filter_parameters()
* Documentation
    * Doesn't show `_into` methods. Fix.
    * For nifgen.Session.write_waveform() it shows type as list of float
    * WriteWaveformDispatcher needs good docs, what about the types displayed?
    * Sometimes refers to private functions rather than public dispatchers.
    * Docstring does not add the suffix from metadata.
    * Documentation for `_into` methods says that the waveform is returned. It isn't.
* Only import numpy once. See https://github.com/ni/nimi-python/pull/690#pullrequestreview-83949244
