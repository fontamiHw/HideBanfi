
import os
import time
import logging
from plot.plotSor  import  PlotSor
from config.config import Config
from webex_bot.webex_bot import WebexBot
from webexteamssdk import WebexTeamsAPI
from webex.commands import CommandImage

class BanfiBot (object):
    def __init__(self):
        logging.info("init BanfiBot")
        
        self.config = Config()
        self.api = WebexTeamsAPI(access_token=self.config.get_token())           
        self.bot = WebexBot(teams_bot_token=self.config.get_token(),
                   #approved_domains=['cisco.com'],
                   approved_rooms=['b69a0c50-3fa8-11f0-b7d6-5d17b726561b'],
                   bot_name=self.config.get_name(),
                   include_demo_commands=True,
                   proxies=self.config.get_proxies())

    def start(self):
        # Get directory from environment variable

        rooms = self.api.rooms.list()
        for u in rooms:
            ids = u.title
            logging.info(f'Bot has in in rooms: {u}')
        watch_dir = os.environ.get('APP_SOR_FILES')
        if not watch_dir:
            logging.info("Environment variable APP_SOR_FILES is not set.")
            exit(1)
        else :
            self.add_commands()
            self.main_loop(watch_dir)

        
    def add_commands(self):
        self.bot.add_command(CommandImage(self.api, PlotSor()))
   

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
