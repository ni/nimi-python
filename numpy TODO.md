* Add support for numpy.ndarray as input parameter (i.e. write_waveform)
* Generate `_into` flavors of all niscope fetch functions:
    * ~~FetchBinary8~~
    * FetchBinary16
    * FetchBinary32
    * Fetch (double)
* Generate `_into` flavors of all niscope read functions:
* Generate numpy flavors of all nifgen read/write waveform functions
    * create_waveform_f64(self, waveform_data_array)
    * create_waveform_i16(self, waveform_data_array)
    * define_user_standard_waveform(self, waveform_data_array)
    * write_binary16_waveform(self, waveform_handle, data)
    * write_named_waveform_f64(self, waveform_name, data)
    * write_named_waveform_i16(self, waveform_name, data)
    * write_waveform(self, waveform_handle, data)
* Create "dispatching" methods for:
    * niscope.fetch
    * nifgen.create
    * nifgen.write
* Add `_into` flavor of nidmm fetch_waveform, in addition to regular list flavor
* `_into` methods should make the size parameter default to None, which means: get the size from the numpy.array and use that.
* Reorder cases in `get_ctype_variable_declaration_snippet` (no more 13.5 and such)
* `get_method_return_snippet` should leverage filter_parameters()
* Documentation doesn't show `_into` methods. Fix.
* `session_numpy_method.py.mako` is not a very descriptive name, rename once we add the template for creating waveforms.
* __str__() for matcher classes would be nice.
