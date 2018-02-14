from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon

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
The 'driver_setup' key is set using the driver setup dictionary - the device model number and
board type. When you specify the driver setup key, NI-DCPower ignores the resource name parameter. If
you do not specify the driver setup string, NI-DCPower simulates the device specified in the
resource name parameter. If you specify neither the driver setup string nor the resource name parameter,
NI-DCPower simulates an NI PXI-4110 by default. 
''')

__version__ = config['module_version']


