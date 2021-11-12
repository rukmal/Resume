import logging
import os
import sys

# Setting logging level to 'DEBUG' for the debugger
logging.getLogger().setLevel(logging.INFO)

try:
    import precis
except ModuleNotFoundError:
    sys.path.insert(0, os.path.abspath('../precis/'))
    # os.chdir(os.path.abspath('../'))
    import precis
