* Reorder cases in `get_ctype_variable_declaration_snippet` (no more 13.5 and such)
* `get_method_return_snippet` should leverage filter_parameters()
* Documentation
    * Doesn't show `_into` methods. Fix.
    * For nifgen.Session.write_waveform() it shows type as list of float
    * WriteWaveformDispatcher needs good docs, what about the types displayed?
    * Sometimes refers to private functions rather than public dispatchers.
    * Docstring does not add the suffix from metadata.
    * Documentation for `_into` methods says that the waveform is returned. It isn't.

