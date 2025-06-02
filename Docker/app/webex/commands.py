from webex_bot.models.command import Command
from webex_bot.formatting import quote_info
from webexteamssdk import WebexTeamsAPI
import logging, time
import threading

class CommandImage(Command):

    def __init__(self, api: WebexTeamsAPI):
        command = "sor"
        super().__init__(
            command_keyword=command,
            help_message=f"{command}: Return the plot image of the giving SOR file.",
        )
        self.api = api
    
    def execute(self, message, attachment_actions, activity):    
        logging.info(f"message: {message}")
        logging.info(f"activity: {activity}")
        self.thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()
        self.thread.start()
        return quote_info("Processing SOR")

    def run(self):
        time.sleep(2)         
        self.api.messages.create(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vYjY5YTBjNTAtM2ZhOC0xMWYwLWI3ZDYtNWQxN2I3MjY1NjFi",
                                  files=['/app/host/JPG//Mik_Node-S-D01-TX-20250528-091512.jpg'])      



