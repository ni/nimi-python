from metadata.config import config
from metadata.functions import functions
from metadata.functions_addon import functions_addon
from metadata.attributes import attributes
from metadata.enums import enums

def merge_dicts(into, outof):
    for item in outof:
        if type(outof[item]) is dict:
            assert type(into[item]) is dict
            merge_dicts(into[item], outof[item])
        else:
            into[item] = outof[item]

merge_dicts(functions, functions_addon)

__version__ = config['module_version']
