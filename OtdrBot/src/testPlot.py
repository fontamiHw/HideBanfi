import matplotlib.pyplot as plt
import json
import os
import time
import logging
from plot.plotSor  import  PlotSor



# Configure logging to write to a file
logging.basicConfig(
    filename=f"{os.environ['APP_LOG_FILES']}/CiscoBanfi.log",           # Log file name
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(filename)s[%(module)s(%(lineno)s)]: %(levelname)s  %(message)s'  # Log format
)

plotSor = PlotSor()
# Get directory from environment variable
watch_dir = os.environ.get('APP_SOR_FILES')
if not watch_dir:
    logging.info("Environment variable APP_SOR_FILES is not set.")
    exit(1)

while True:
    try :
        logging.info(f"Watching directory: {watch_dir}")

        # Get initial set of files
        seen_files = set(os.listdir(watch_dir))

        while True:
            current_files = set(os.listdir(watch_dir))
            new_files = current_files - seen_files
            for filename in new_files:
                logging.info(f"Processing file: {filename}")
                plotSor.create_image_of(filename)
            seen_files = current_files
            time.sleep(1) 
    except Exception as e:
        logging.error(f"error: {e}")

