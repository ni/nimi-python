from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums

import re
def merge_dicts(into, outof):
    for item in sorted(outof):
        if type(outof[item]) is dict:
            if item in into and type(into[item] is list):
                merge_dicts(into[item], outof[item])
            elif item in into:
                merge_dicts(into[item], outof[item])
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:
                # Handle regex in addon
                for item2 in into:
                    if re.search(item, item2):
                        assert type(into[item2]) is dict
                        merge_dicts(into[item2], outof[item])
        else:
            if item in into:
                into[item] = outof[item]
            else:
                for item2 in sorted(into):
                    if re.search(item, item2):
                        into[item2] = outof[item]

from metadata.functions_addon import functions_codegen_method
from metadata.functions_addon import functions_enums
from metadata.functions_addon import functions_params_types
from metadata.functions_addon import functions_buffer_info

merge_dicts(functions, functions_codegen_method)
merge_dicts(functions, functions_enums)
merge_dicts(functions, functions_params_types)
merge_dicts(functions, functions_buffer_info)

__version__ = config['module_version']

config['functions'] = functions
config['attributes'] = attributes
config['enums'] = enums

