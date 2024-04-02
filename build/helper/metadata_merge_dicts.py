# Useful functions for use in the metadata modules

import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=80)


def merge_helper(metadata, metadata_type, config, use_re):
    metadata_module = f'metadata.{metadata_type}_addon'
    if 'modules' in config and metadata_module in config['modules']:
        for m in dir(config['modules'][metadata_module]):
            if m.startswith(f'{metadata_type}_additional_'):
                # We need to explicitly copy new entries
                outof = config['modules'][metadata_module].__getattribute__(m)
                for a in outof:
                    metadata[a] = outof[a]
            elif m.startswith(f'{metadata_type}_'):
                merge_dicts(metadata, config['modules'][metadata_module].__getattribute__(m), use_re, m)

    # Delete any entries that are empty
    # Have to do this in two steps. Otherwise the dictionary changes size and errors
    to_delete = []
    for m in metadata:
        if type(m) is dict and len(metadata[m]) == 0:
            to_delete.append(m)
    for m in to_delete:
        metadata.pop(m, None)

    return metadata


def merge_dicts(into, outof, use_re, dict_name):
    '''merge_dicts

    Recursively merges the contents of dictionary 'outof' into dictionary 'into'.
    'into' may contain lists as values.
    'outof' may contain regular expressions as keys, in which case values are
    merged with all key matches in into.
    '''
    for item in sorted(outof):
        # If we're not using regex's then this is an easy check
        if not use_re and item not in into and dict_name is not None:
            raise KeyError(f'Key {item} from {dict_name} is not in the destination')
        # If we are using regex's we need to seach all keys to see if any match
        if use_re and dict_name is not None:
            key_exists = False
            for item2 in into:
                if re.search(item, item2):
                    key_exists = True
            if not key_exists:
                raise KeyError(f'Key {item} from {dict_name} is not in the destination')

        if type(outof[item]) is dict:
            if item in into:
                merge_dicts(into[item], outof[item], use_re, None)
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:
                # attributes keys are integers so they do not need the regex check (and
                # in fact will error)
                if type(item) is str:
                    # Handle regex in addon
                    for item2 in into:
                        if use_re is True and re.search(item, item2):
                            assert type(into[item2]) is dict
                            merge_dicts(into[item2], outof[item], use_re, None)
        else:
            into[item] = outof[item]

