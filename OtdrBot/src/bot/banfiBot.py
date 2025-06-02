
import os
import time
import logging
from plot.plotSor  import  PlotSor
from config.config import Config
from webex_bot.webex_bot import WebexBot
from webexteamssdk import WebexTeamsAPI

class BanfiBot (object):
    def __init__(self):
        logging.info("init BanfiBot")
        self.plotSor = PlotSor()
        self.config = Config()

    def start(self):
        self.init_bot()
        # Get directory from environment variable
        watch_dir = os.environ.get('APP_SOR_FILES')
        if not watch_dir:
            logging.info("Environment variable APP_SOR_FILES is not set.")
            exit(1)
        else :
            self.main_loop(watch_dir)

    def init_bot(self):
        self.api = WebexTeamsAPI(access_token=self.config.get_token())           
        self. bot = WebexBot(teams_bot_token=self.config.get_token(),
                   #approved_domains=['cisco.com'],
                   bot_name=self.config.get_name(),
                   include_demo_commands=True,
                   proxies=self.config.get_proxies())
        

    def main_loop(self, watch_dir:str):
        try:
            logging.info("Starting bot")
            self.bot.run()
            logging.info("Stop bot")
        except Exception as e:
                logging.error(f"Bot error: {e}")

    def test_loop(self):
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
