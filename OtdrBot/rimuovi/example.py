import os

from echo import EchoCommand
from webex_bot.webex_bot import WebexBot
from webexteamssdk import WebexTeamsAPI

# (Optional) Proxy configuration
# Supports https or wss proxy, wss prioritized.
proxies = {
    'https': 'http://proxy.esl.example.com:80',
    'wss': 'socks5://proxy.esl.example.com:1080'
}



'''
Space name: TEstBanfi
Space ID: b69a0c50-3fa8-11f0-b7d6-5d17b726561b
Space URI: webexteams://im?space=b69a0c50-3fa8-11f0-b7d6-5d17b726561b
Space URI (markdown): [TEstBanfi](webexteams://im?space=b69a0c50-3fa8-11f0-b7d6-5d17b726561b)
Participant count: 2
External participant count: 0
Conversation type: group

Space name: TEstBanfi
Space ID: b69a0c50-3fa8-11f0-b7d6-5d17b726561b
Space URI: webexteams://im?space=b69a0c50-3fa8-11f0-b7d6-5d17b726561b
Space URI (markdown): [TEstBanfi](webexteams://im?space=b69a0c50-3fa8-11f0-b7d6-5d17b726561b)
Participant count: 2
External participant count: 0
Conversation type: group


'''
# Create a Bot Object
bot = WebexBot(teams_bot_token="M2IwNDU0OWItYTg1ZC00YjQyLTkwMDMtODQyZDMyYzA1M2U2NmQ1MjdlOTktNWFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
               bot_name="MikExperiment",
               approved_rooms=['Y2lzY29zcGFyazovL3VzL1JPT00vYjY5YTBjNTAtM2ZhOC0xMWYwLWI3ZDYtNWQxN2I3MjY1NjFi'],
               include_demo_commands=True)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

api = WebexTeamsAPI(access_token="M2IwNDU0OWItYTg1ZC00YjQyLTkwMDMtODQyZDMyYzA1M2U2NmQ1MjdlOTktNWFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f")   
rooms = api.rooms.list()
for u in rooms:
            ids = u.title
            print(f'Bot has in in rooms: {u}')

# Call `run` for the bot to wait for incoming messages.
bot.run()