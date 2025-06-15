from webex_bot.models.command import Command
from webex_bot.formatting import quote_info
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.models.immutable import Message
from plot.plotSor  import  PlotSor
import logging, time
import threading

class MessageData(object):

    def __init__(self, roomId:str, message:str):
        logging.info(f"received message: {message} for roomId: {roomId}")
        message = message.replace(".sor", ".json")
        logging.info(f"converted message: '{message}' !!!!!!!!!!!!!!!!!!!!!!!!!")
        self.message = message
        self.roomId = roomId

    def getMessage(self) :
        # ['/app/host/JPG//Mik_Node-S-D01-TX-20250528-091512.jpg']
        ret=[]
        ret.append(self.message.strip())
        return ret
    
    def getRoomId(self) -> str:
        return self.roomId
    
class CommandImage(Command):

    def __init__(self, api: WebexTeamsAPI, plotSor = PlotSor):
        command = "sor"
        super().__init__(
            command_keyword=command,
            help_message=f"{command}: Return the plot image of the giving SOR file.",
        )
        self.api = api
        self.plot_sor = plotSor
    
    def execute(self, message, attachment_actions:Message, activity):    
        self.thread = threading.Thread(target=self.run, args=(MessageData(attachment_actions.roomId, message),))
        self.stop_event = threading.Event()
        self.thread.start()
        return quote_info("Processing SOR")

    def run(self, message_data: MessageData):
        time.sleep(2) 
        files=message_data.getMessage()
        jpg_file2 = []
        for file in files:
            logging.info(f"processing file: '{file}' !!!!!!!!!!!!!!!!!!!!!")
            jpg_file2.append(self.plot_sor.create_image_of(file))
            roomId=message_data.getRoomId()
            self.api.messages.create(roomId=roomId, files=jpg_file2)      



