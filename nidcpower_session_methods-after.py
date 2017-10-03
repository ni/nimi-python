    def __init__(self, session):
    def __enter__(self):
    def __exit__(self, exc_type, exc_value, traceback):
    def __init__(self, repeated_capability):
    def __setattr__(self, key, value):
    def get_error_description(self, error_code):
    def configure_aperture_time(self, aperture_time, units):
    def fetch_multiple(self, timeout, count):
    def _get_attribute_vi_boolean(self, attribute_id):
    def _get_attribute_vi_int32(self, attribute_id):
    def _get_attribute_vi_int64(self, attribute_id):
    def _get_attribute_vi_real64(self, attribute_id):
    def _get_attribute_vi_string(self, attribute_id):
    def measure(self, measurement_type):
    def measure_multiple(self):
    def query_in_compliance(self):
    def query_max_current_limit(self, voltage_level):
    def query_max_voltage_level(self, current_limit):
    def query_min_current_limit(self, voltage_level):
    def query_output_state(self, output_state):
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
    def set_sequence(self, values, source_delays, size):
    def __init__(self, vi, repeated_capability):
    def __init__(self, resource_name, channels, reset, option_string):
    def __enter__(self):
    def __exit__(self, exc_type, exc_value, traceback):
    def __getitem__(self, repeated_capability):
    def initiate(self):
    def close(self):
    def _abort(self):
    def commit(self):
    def configure_digital_edge_measure_trigger(self, input_terminal, edge):
    def configure_digital_edge_pulse_trigger(self, input_terminal, edge):
    def configure_digital_edge_sequence_advance_trigger(self, input_terminal, edge):
    def configure_digital_edge_source_trigger(self, input_terminal, edge):
    def configure_digital_edge_start_trigger(self, input_terminal, edge):
    def create_advanced_sequence(self, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):
    def create_advanced_sequence_step(self, set_as_active_step):
    def delete_advanced_sequence(self, sequence_name):
    def disable(self):
    def export_signal(self, signal, signal_identifier, output_terminal):
    def _get_error(self):
    def get_self_cal_last_date_and_time(self):
    def get_self_cal_last_temp(self):
    def _initialize_with_channels(self, resource_name, channels, reset, option_string):
    def _initiate(self):
    def read_current_temperature(self):
    def reset_device(self):
    def reset_with_defaults(self):
    def send_software_edge_trigger(self, trigger):
    def wait_for_event(self, event_id, timeout):
    def _close(self):
    def reset(self):
    def revision_query(self):
    def self_test(self):
