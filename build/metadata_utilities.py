# Useful functions for use in the metadata modules

import re
def merge_dicts(into, outof):
    '''Recursively merge one dictionary into another

    Args:
        into (dict) - Dictionary that will be a combination of into and outof when complete
        outof (dict) - Dictionary that should be merged into into
    '''
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


