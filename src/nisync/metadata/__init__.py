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
Supported Combinations:

+-------+---------------------+
| Model | Board Type          |
+=======+=====================+
| 4065  | PXI, PCI, PCIe, USB |
+-------+---------------------+
| 4070  | PXI, PCI            |
+-------+---------------------+
| 4071  | PXI                 |
+-------+---------------------+
| 4072  | PXI                 |
+-------+---------------------+
| 4080  | PXIe                |
+-------+---------------------+
| 4081  | PXIe                |
+-------+---------------------+
| 4082  | PXIe                |
+-------+---------------------+

If the Instrument Descriptor parameter and the Driver Setup property are not specified, an
NI PXI-4070 is simulated by default. If the Driver Setup string is not provided, and the
Instrument Descriptor parameter specifies a valid device, the device of the Instrument
Descriptor property is simulated. If the Driver Setup string is specified, the Instrument
Descriptor property is ignored.
''')
__version__ = config['module_version']


