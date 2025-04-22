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

__version__ = config['module_version']


