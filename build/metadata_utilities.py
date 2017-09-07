# Useful functions for use in the metadata modules

import re

def merge_dicts(into, outof):
    '''merge_dicts

    Recursively merges the two passed in dictionaries.
    '''
    for item in sorted(outof):
        if type(outof[item]) is dict:
            if item in into:
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
            into[item] = outof[item]

