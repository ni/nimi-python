from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums

__version__ = config['module_version']

config['functions'] = functions
config['attributes'] = attributes
config['enums'] = enums

