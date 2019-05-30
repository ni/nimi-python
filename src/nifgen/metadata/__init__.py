from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

if 'note' not in config['functions']['_init_function']['parameters'][3]:
    config['functions']['_init_function']['parameters'][3]['note'] = []
if not isinstance(config['functions']['_init_function']['parameters'][3]['note'], list):
    config['functions']['_init_function']['parameters'][3]['note'] = [config['functions']['_init_function']['parameters'][3]['note']]

config['functions']['_init_function']['parameters'][3]['note'].append(
'''
+--------------+----------------------------------------------------------------------------------------------------------+
| Device       | options driver_setup syntax                                                                              |
+==============+==========================================================================================================+
| NI PXI-5404  | { 'driver_setup': { 'Model': '5404', 'BoardType': 'PXI' } }                                              |
+--------------+----------------------------------------------------------------------------------------------------------+
| NI PCI-5411  | { 'driver_setup': { 'Model': '5411', 'BoardType': 'PCI', 'MemorySize': '8000000' } }                     |
+--------------+----------------------------------------------------------------------------------------------------------+
| NI PXIe-5450 | { 'driver_setup': { 'Model': '5450', 'Channels': '0-1', 'BoardType': 'PXIe', 'MemorySize': '8000000' } } |
+--------------+----------------------------------------------------------------------------------------------------------+
''')

__version__ = config['module_version']


