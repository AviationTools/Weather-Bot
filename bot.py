import os
import discord
import requests
import datetime

from PIL import Image
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

@client.event
async def on_message(message):
    async with message.channel.typing():

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


        if message.content == "!satellite":
            images = []
            utc = datetime.datetime.utcnow()
            plain_date = utc.strftime("%y%m%d")
            print(plain_date)
            times = ["0000", "0030", "0100", "0130", "0200", "0230", "0300", "0330", "0400", "0430", "0500", "0530", "0600", "0630", "0700", "0730", "0800", "0830", "0900", "0930", "1000", "1030", "1100", "1130", "1200", "1200", "1230", "1300", "1330", "1400", "1430", "1500", "1530", "1600", "1630", "01700", "1730", "1800", "1830", "1900", "1930", "2000", "2030", "2100", "2130", "2200", "2230", "2300", "2330", "2400"]
            
            for time in times:
                response = requests.get(f"https://www.zamg.ac.at/dyn/pictures/Hsatimg/H{plain_date}{time}.gif", stream=True)
                
                if response.status_code == 200:
                    img = Image.open(response.raw)
                    images.append(img)
                elif response.status_code == 404:
                    print("not found weather map for ", time)
            
            images[0].save('satellite.gif', save_all=True, append_images=images[1:], loop=0, duration=200)
            await message.channel.send(file=discord.File('satellite.gif'))
            os.remove("satellite.gif") 


        if message.content == "!world":
            images = []
            utc = datetime.datetime.utcnow()
            plain_date = utc.strftime("%Y%m%d")
            print(plain_date)
            times = ["0000", "0030", "0100", "0130", "0200", "0230", "0300", "0330", "0400", "0430", "0500", "0530", "0600", "0630", "0700", "0730", "0800", "0830", "0900", "0930", "1000", "1030", "1100", "1130", "1200", "1200", "1230", "1300", "1330", "1400", "1430", "1500", "1530", "1600", "1630", "01700", "1730", "1800", "1830", "1900", "1930", "2000", "2030", "2100", "2130", "2200", "2230", "2300", "2330", "2400"]
            
            for time in times:
                response = requests.get(f"https://www.zamg.ac.at/zamgWeb/wetter/weltsatbilder/worldsatimg/WCM/SAT_WCM_{plain_date}{time}.gif", stream=True)
                
                if response.status_code == 200:
                    img = Image.open(response.raw)
                    images.append(img)
                elif response.status_code == 404:
                    print("not found weather map for ", time)
            
            images[0].save('world.gif', save_all=True, append_images=images[1:], loop=0, duration=200)
            await message.channel.send(file=discord.File('world.gif'))
            os.remove("world.gif")


        if message.content == "!sigwx":
            print("handling !weather")

            utc = datetime.datetime.utcnow()
            plain_date = utc.strftime("%y%m%d")
            link_date = utc.strftime("%Y/%m/%d")

            times = ["0000", "0600", "1200", "1800"]
            last_url = None
            for time in times:
                response = requests.get(f"http://brunnur.vedur.is/flugkort/PGDE14_EGRR_{time}.PNG")

                if response.status_code == 200:
                    last_url = f"http://brunnur.vedur.is/flugkort/PGDE14_EGRR_{time}.PNG"
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
