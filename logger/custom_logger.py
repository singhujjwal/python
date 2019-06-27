import os
import logging.config

import yaml
import sys

base_dir = os.path.dirname(os.path.abspath(os.path.basename(__file__)))
if "win" in sys.platform:
    logger_pkg_path = os.path.dirname(base_dir) + "\logger"
else:
    logger_pkg_path = os.path.dirname(base_dir) + "/logger"
print(os.path.dirname(base_dir))
sys.path.insert(0, logger_pkg_path)
print(sys.path)
from logger import custom_logger

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    print ("ujjwal singh")
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        print ("path doesnt exists")
        logging.basicConfig(level=default_level)
		objects = importlib.import_module('gitlab.v%s.objects' %
                                          self._api_version)
