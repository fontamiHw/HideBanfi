import matplotlib.pyplot as plt
import json
import os
import time
import logging



# Configure logging to write to a file
logging.basicConfig(
    filename=f"{os.environ['APP_LOG_FILES']}/CiscoBanfi.log",           # Log file name
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(filename)s[%(module)s(%(lineno)s)]: %(levelname)s  %(message)s'  # Log format
)


def create_image_of(filename:str):
    data = {}
    file_sor = os.environ.get('APP_SOR_FILES') + "/" + filename
    file_jpg = os.environ.get('APP_JPG_FILES') + "/" + filename.replace(".json", ".jpg")
    logging.info(f"converting {file_sor} into {file_jpg}")
    # Load data from JSON file
    with open(file_sor, 'r') as f:
        data = json.load(f)

    logging.info(len(data['points']))

    # Extract frequency and power values
    frequencies = [point["km"] for point in data["points"]]
    powers = [point["loss"] for point in data["points"]]
    ml_elements = [point.get("otdr_events", "") for point in data["points"]]

    # Create the plot
    plt.figure()
    plt.plot(frequencies, powers)

    # Add labels and title
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (dB)')
    plt.title('Frequency vs Power')

    # Annotate points with non-empty 'ml' labels
    for i, ml in enumerate(ml_elements):
        if ml:
            plt.annotate(ml, (frequencies[i], powers[i]))

    # Save the plot as a JPEG file
    plt.savefig(file_jpg, format='jpeg')
    # Set the size of the plot
    plt.gcf().set_size_inches(10, 6)
    # Set the size of the window
    manager = plt.get_current_fig_manager()
    logging.info(manager.canvas.get_width_height())
    #manager.window.state('zoomed')
    manager.resize(1000, 200)
    logging.info(manager.canvas.get_width_height())
    # Show the plot
    #plt.show() 


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
                create_image_of(filename)
            seen_files = current_files
            time.sleep(1) 
    except Exception as e:
        logging.error(f"error: {e}")

