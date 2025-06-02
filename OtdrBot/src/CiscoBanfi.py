import os
import logging
from bot.banfiBot import BanfiBot

# Configure logging to write to a file
logging.basicConfig(
    # Log file name
    filename=f"{os.environ['APP_LOG_FILES']}/CiscoBanfi.log",           
    level=logging.INFO,           # Log level
    format='%(asctime)s - %(filename)s[%(module)s(%(lineno)s)]: %(levelname)s  %(message)s'  # Log format
)

def main():
    print(f"{os.environ['APP_LOG_FILES']}/CiscoBanfi.log")

    bot = BanfiBot()
    bot.start()

                    
if __name__ == "__main__":
    main()