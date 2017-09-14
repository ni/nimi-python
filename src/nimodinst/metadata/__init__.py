from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums

import build.helper as helper

# Update generated functions data with hand maintained data
from metadata.functions_addon import functions_codegen_method
from metadata.functions_addon import functions_params_types
from metadata.functions_addon import functions_buffer_info
from metadata.functions_addon import functions_is_error_handling

helper.merge_dicts(functions, functions_codegen_method)
helper.merge_dicts(functions, functions_params_types)
helper.merge_dicts(functions, functions_buffer_info)
helper.merge_dicts(functions, functions_is_error_handling)

helper.add_all_metadata(functions, config)

__version__ = config['module_version']

config['functions'] = functions
config['attributes'] = attributes
config['enums'] = enums

