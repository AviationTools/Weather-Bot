import os
import discord
import requests
import datetime

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!weather":
        print("handling !weather")

        utc = datetime.datetime.utcnow()
        plain_date = utc.strftime("%y%m%d")
        link_date = utc.strftime("%Y/%m/%d")

        times = ["0000", "0600", "1200", "1800"]
        last_url = None
        for time in times:
            response = requests.get(f"https://www.zamg.ac.at/fix/wetter/bodenkarte/{link_date}/BK_BodAna_Sat_{plain_date}{time}.png")

            if response.status_code == 200:
                last_url = f"https://www.zamg.ac.at/fix/wetter/bodenkarte/{link_date}/BK_BodAna_Sat_{plain_date}{time}.png"
            elif response.status_code == 404:
                print("not found weather map for ", time)
                break

        if last_url:
            print("found weather map ", last_url)
            await message.channel.send(last_url)
        else:
            await message.channel.send("Could not fetch last weather map.")

print("starting weather bot")
client.run(TOKEN)
