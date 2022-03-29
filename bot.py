# bot.py

import datetime
import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == '!weather':

        utc = datetime.datetime.utcnow()
        format = utc.strftime("%y%m%d")
        link = utc.strftime("%Y/%m/%d")

        time = ['0000', '0600', '1200', '1800']
        lastUrl = ""
        for h in time:
            utcString = format+h
            response = requests.get(f'https://www.zamg.ac.at/fix/wetter/bodenkarte/{link}/BK_BodAna_Sat_{utcString}.png')

            if response.status_code == 200:
                lastUrl = f'https://www.zamg.ac.at/fix/wetter/bodenkarte/{link}/BK_BodAna_Sat_{utcString}.png'
            elif response.status_code == 404:
                print('Not Found.')

        await message.channel.send(lastUrl)

client.run(TOKEN)
