import logging
import os

def getLogger(name="builderProcess"):
        
    # Configure logging to write to a file
    log = logging.basicConfig(
        filename=f"{os.environ['APP_LOG_FILES']}/{name}.log",           # Log file name
        level=logging.INFO,           # Log level
        format='%(asctime)s - %(filename)s[%(module)s(%(lineno)s)]: %(levelname)s  %(message)s'  # Log format
    )
    return log