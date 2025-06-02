from webex_bot.models.command import Command
from webexteamssdk.models.cards import (Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Image, HorizontalAlignment)
from webex_bot.formatting import quote_danger, quote_info
import logging, time
from webex_bot.models.response import response_from_adaptive_card

class CommandImage(Command):

    def __init__(self):
        command = "sor"
        super().__init__(
            command_keyword=command,
            help_message=f"{command}: Return the plot image of the giving SOR file.",
            #chained_commands=[ImageCb()]
        )
    
    def execute(self, message, attachment_actions, activity):    
        image = Image(url="/data/Docker/CiscoBanfi/JPG/Mik_Node-S-D01-RX-20250528-075531.jpg")
        text1 = TextBlock("Working on it....", weight=FontWeight.BOLDER, wrap=True, size=FontSize.DEFAULT,
                          horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
        text2 = TextBlock("I am busy working on your request. Please continue to look busy while I do your work.",
                          wrap=True, color=Colors.DARK)
        card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=[image], width=2)]),
                  ColumnSet(columns=[Column(items=[text1, text2])]),
                  ])

        return response_from_adaptive_card(card)


class ImageCb(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="echo_callback",
            delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return quote_info(attachment_actions.inputs.get("message_typed"))

