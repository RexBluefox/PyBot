from webserver import keep_alive
from discord.utils import get
import googletrans
from googletrans import Translator

import os
import discord
import requests
#import youtube_dl
import base64
import json
import datetime


class Client(discord.client.Client):
  trollmode = "disable"

    # Einloggen
  async def on_ready(self):  
      #MessageContent = "Message by " + str(message.author) + ": " + str(message.content)
    
      print("I'm ready Boss!")
      await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers | +help for help!"))
      

    #Troll Mode
  

    # When Message is posted
  async def on_message(self, message):
        #print("Message by " + str(message.author) + ": " + str(message.content))
        # Rules
        if message.author == client.user:
            return
        if str(message.author) == "LolRiTTeRBot#0238":
          return
        if message.channel.id == 835207809049559070:
          return
        if str(message.author) == "KAMI Blue 2.03.02-840d3ad5c#0000":
          return
        print("Message by " + str(message.author) + " in " + str(message.guild) + ": " + str(message.content))

        #Modules
        Mention = (" <@!" + str(message.author.id) + ">")
        translator = Translator()
        MessageContent = "Message by " + str(message.author) + " in " + str(message.guild) +  ": " + str(message.content)
        #pip install googletrans==3.1.0a0
        # Commands

        #Help Command(Commandlist)
        if message.content.startswith("+help"):
          #await message.channel.send("The available Commands are: \nHi \nnice \n+foxy \n+prioq \n+queue \n+tps \n+uptime \n+prioeta \n+namemc [Username] \n+mcskin [Username} \n+avatar @User \n+cat \n+dog \n+monke \n+playercount \n+tablist \n+seen \n+stats [Username]\n(\n    +kills \n    +deaths\n    +joins\n    +leaves\n)\n+translate [fromLanguage] [toLanguage] [Text]")
          embed = discord.Embed(title="Help",timestamp=datetime.datetime.utcnow())
          embed.set_author(name="PyBot", url="https://discordapp.com", icon_url="https://i.imgur.com/WgmKaoX.png")
          embed.set_footer(text="Bot by Bluefox#3699", icon_url="https://i.imgur.com/2BGKfWO.png")
          embed.add_field(name="The available Commands are:", value=" \nHi \nnice \n+foxy \n+prioq \n+queue \n+tps \n+uptime \n+prioeta \n+namemc [Username] \n+mcskin [Username} \n+avatar @User \n+cat \n+dog \n+monke \n+playercount \n+tablist \n+seen \n+stats [Username]\n(\n    +kills \n    +deaths\n    +joins\n    +leaves\n)\n+translate [fromLanguage] [toLanguage] [Text]\n +locations [keyword]")
          await message.channel.send(embed=embed)


        #Hi Command
        if message.content == "Hi":
          MessageContent
          print("Hi")
          await message.channel.send('Hi')
           

        #Nice Command
        if message.content.startswith("nice"):
          MessageContent
          await message.channel.send('nicer')
          await message.author.send('the nicest')

        #RandomFox Command
        if message.content.startswith("+foxy"):
          MessageContent
          await message.add_reaction("🦊")
          response = requests.get("https://randomfox.ca/floof")
          fox = response.json()
          await message.channel.send("Here is a cute lil fox for you:")
          await message.channel.send(fox['image'])

        #Priority Queue Command
        if message.content.startswith("+prioq"):
          MessageContent
          await message.add_reaction("👍")
          response = requests.get("https://api.2b2t.dev/prioq")
          prioq = response.json()
          print(prioq[1])
          await message.channel.send("Priority Queue is " + str(prioq[1]) + " right now")

        #Normal Queue Command
        if message.content.startswith('+queue'):
          MessageContent
          await message.add_reaction("👍")
          response = requests.get("https://2b2t.io/api/queue?last=true")
          queue = response.json()
          print(queue[0][1])
          await message.channel.send("Normal Queue is "+ str(queue[0][1]) + " right now." + Mention)

        #TPS Command
        if message.content.startswith("+tps"):
          MessageContent
          await message.add_reaction("👍")
          response = requests.get("https://api.2b2t.dev/status")
          tps = response.json()
          print(tps[0][0])
          await message.channel.send("The TPS of 2b2t is " + str(tps[0][0]) + " right now." + Mention)

        #Uptime Command
        if message.content.startswith("+uptime"):
          MessageContent
          await message.add_reaction("👍")
          response = requests.get("https://api.2b2t.dev/status")
          uptime = response.json()
          print(uptime[0][3])
          await message.channel.send("2b2t is up for: " + str(uptime[0][3]) + "." + Mention)

        #PrioQ ETA
        if message.content.startswith("+prioeta"):
          MessageContent
          await message.add_reaction("👍")
          response = requests.get("https://api.2b2t.dev/prioq")
          eta = response.json()
          print(eta[2])
          if eta[2] == None:
            print("No Time to wait Right now!")
            await message.channel.send("There's no time to wait right now in Priority Queue. Jump on quick " + Mention + "!")
          else:
            print(eta[2])
            await message.channel.send("You have to wait " + str(eta[2]) + " right now in Priority Queue!")

        #Troll Mode Switch
        if message.content.startswith("+troll enable"):
            trollmode = "enable"
            await message.channel.send("Trollmode enabled!")
        if message.content.startswith("+troll disable"):
            trollmode = "disable"
            await message.channel.send("Trollmode disabled!")

        #Avatar Command
        if message.content.startswith("+avatar"):
          MessageContent
          try:
            avatar = str(message.mentions[0].avatar_url)
          #await message.channel.send(str(message.author.avatar_url))
            await message.channel.send(avatar)
          except:
            await message.channel.send(str(message.author.avatar_url))

        #Random Cat Command
        if message.content.startswith("+cat"):
          MessageContent
          response = requests.get("https://api.thecatapi.com/v1/images/search")
          cat = response.json()
          cat_image = cat[0]['url']
          await message.channel.send(cat_image)

        #Random Dog Command
        if message.content.startswith("+dog"):
          MessageContent
          response = requests.get("https://api.thedogapi.com/v1/images/search")
          dog = response.json()
          dog_image = dog[0]['url']
          await message.channel.send(dog_image)
        
        #Return to Monke
        if message.content.startswith("+monke"):
          MessageContent
          await message.channel.send("https://tenor.com/view/reject-modernity-return-to-monke-monke-gif-19167526")
          await message.add_reaction("🐵")

        #Music Commands
          #Join
        #if message.content.startswith("+join"):
            #link = message.content.split(" ")[2]
            #where = message.content.split(" ")[1]
            #channel = get(message.guild.channels, name=where)
            #voicechannel = await channel.connect()
            #vc = await youtube_dl.join_voice_channel(channel)
            #player = await vc.create_ytdl_player(link)
            #player.start()

        #NameMC Command
        if message.content.startswith("+namemc"):
          MessageContent
          name = message.content.split(" ")[1]
          await message.channel.send("https://namemc.com/" + str(name))

        #Minecraft API
        if message.content.startswith("+mcskin"):
              MessageContent
              await message.channel.send("Ok")
              Username = message.content.split(" ")[1]
              print(str(Username))
              response = requests.get("https://api.mojang.com/users/profiles/minecraft/" + str(Username))
              UUID1 = response.json()
              UUID = UUID1['id']
              response2 = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + UUID)
              Skin1 = response2.json()
              SkinValue = Skin1['properties'][0]['value'] 
              b64_string = SkinValue.encode('ascii')
              b64_bytes = base64.b64decode(b64_string)
              decode_str = b64_bytes.decode('ascii')
              #decoded_str = json.loads(decode_str)
              decoded_str = json.loads(decode_str)
          
              
              SkinURL = decoded_str['textures']['SKIN']['url']
              await message.channel.send("Here is " + Username + "'s Minecraft Skin: ")
              await message.channel.send(SkinURL)

          #Server Command
        if message.content.startswith("+serverlist"):
          MessageContent
          print(str(client.guilds))
          #await message.channel.send(str(client.guilds))
            #servers = len(client.guilds)
            #servers1 = servers - 1
            #servers2 = servers - servers1
            #while not servers2 == servers:
              #servers2 + 1
              #await message.channel.send(str(client.guilds[servers2]))
        if message.content.startswith(":SADGE:"):
          MessageContent
          await message.channel.send(":SADGE:")

        #Players online
        if message.content.startswith("+playercount"):
          MessageContent
          response = requests.get("https://api.2b2t.dev/status")
          playercount = response.json()
          #print(playercount[0][1])
          await message.channel.send(str(playercount[0][1]) + " people are online right now!")

        #Tablist
        if message.content.startswith("+tablist"):
          MessageContent
          await message.channel.send("Here is the Tablist:")
          await message.channel.send("https://tab.2b2t.dev/")

        #seen command
        if message.content.startswith("+seen"):
          MessageContent
          player = message.content.split(" ")[1]
          print(player)         
          response = requests.get("https://api.2b2t.dev/seen?username=" + str(player))
          print(response)
          seen = response.json()
          print(seen)
          await message.channel.send(player + " was last seen at " +  seen[0]['seen'])
        
        #Stats Commands
        #Kills
        if message.content.startswith("+kills"):
          MessageContent
          player = message.content.split(" ")[1]
          response = requests.get("https://api.2b2t.dev/stats?username=" + player)
          kills = response.json()
          #print(player + " has " + str(kills[0]['kills']) + " kills!")
          await message.channel.send(player + " has " + str(kills[0]['kills']) + " kills!")
        
        #Deaths
        if message.content.startswith("+deaths"):
          MessageContent
          player = message.content.split(" ")[1]
          response = requests.get("https://api.2b2t.dev/stats?username=" + player)
          deaths = response.json()
          #print(player + " has " + str(kills[0]['kills']) + " kills!")
          await message.channel.send(player + " has " + str(deaths[0]['deaths']) + " deaths!")

        #Joins
        if message.content.startswith("+joins"):
          MessageContent
          player = message.content.split(" ")[1]
          response = requests.get("https://api.2b2t.dev/stats?username=" + player)
          joins = response.json()
          #print(player + " has " + str(kills[0]['kills']) + " kills!")
          await message.channel.send(player + " has " + str(joins[0]['joins']) + " joins!")

        #Leaves
        if message.content.startswith("+leaves"):
          MessageContent
          player = message.content.split(" ")[1]
          response = requests.get("https://api.2b2t.dev/stats?username=" + player)
          leaves = response.json()
          #print(player + " has " + str(kills[0]['kills']) + " kills!")
          await message.channel.send(player + " has " + str(leaves[0]['leaves']) + " leaves!")


        #Full Stats Command Embed
        if message.content.startswith("+stats"):
          MessageContent
          player = message.content.split(" ")[1]
          response = requests.get("https://api.2b2t.dev/stats?username=" + player)
          stats = response.json()
          kills = stats[0]['kills']
          deaths = stats[0]['deaths']
          joins = stats[0]['joins']
          leaves = stats[0]['leaves']
          
          embed = discord.Embed(title="Stats from " + player, colour=discord.Colour(0x4a90e2), url="https://api.2b2t.dev/stats?username=" + player, description="API: https://api.2b2t.dev/stats?username=", timestamp=datetime.datetime.utcfromtimestamp(1628587771))

          embed.set_image(url="https://minotar.net/bust/" + player)
          embed.set_thumbnail(url="")
          embed.set_author(name="PyBot", url="https://discordapp.com", icon_url="https://i.imgur.com/WgmKaoX.png")
          embed.set_footer(text="Bot by Bluefox#3699", icon_url="https://i.imgur.com/2BGKfWO.png")

          embed.add_field(name="Kills", value=kills)
          embed.add_field(name="Deaths", value=deaths)
          embed.add_field(name="Joins", value=joins)
          embed.add_field(name="Leaves", value=leaves)

          await message.channel.send(embed=embed)
        

        #Translation Commands
        
        if message.content.startswith("+translate"):
          if "@" in message.content.lower():
            await message.channel.send("No Pings or @s in the message allowed!")
          else:
            try:
            #MessageContent
              fromLanguage = message.content.split(" ")[1]
              toLanguage = message.content.split(" ")[2]
              text1 = message.content.split(maxsplit=3)[3:]
              #print(text)
              #print((text))

            #if fromLanguage == "auto":
              #await message.channel.send("Language detected" + translator.detect(text))

              print(fromLanguage + " " + toLanguage + " " + str(text1[0]))
              print(translator.detect(text1[0]))
            #detect = translator.detect(text1[0])
           # detected = detect['lang']
            #await message.channel.send("Detected Language: " + googletrans.LANGCODES[detected])

              translated = translator.translate(text1[0], dest=str(toLanguage), src=str(fromLanguage)).text

          #print("Translate en to de: ", translator.translate(text, scr='en', dest='de'))
            #await message.channel.send("Language detected: " + translator.detect(text))
              await message.channel.send("Translated to: '" + translated + "'")
            except:
            #await message.channel.send("ERROR")
              fromLanguage = message.content.split(" ")[1]
              if fromLanguage == "languages":
                await message.channel.send(googletrans.LANGUAGES)


        if message.content.startswith("+locations"):
          keyword = message.content.split(" ")[1]
          URL = "https://2b2tatlas.com/api/locations.php"
          all = requests.get(URL)
          resp = requests.get(URL,params="search=" + keyword)
          jsons = resp.json()
          all_json = all.json()

          if keyword == "help":
            embed = discord.Embed(title="Help", colour=discord.Colour(0x4a90e2), url="", description="", timestamp=datetime.datetime.utcnow())
            embed.set_author(name="PyBot", url="https://discordapp.com", icon_url="https://i.imgur.com/WgmKaoX.png")
            embed.set_footer(text="Bot by Bluefox#3699", icon_url="https://i.imgur.com/2BGKfWO.png")

            embed.add_field(name="How to use:", value="+locations {keyword}")
            await message.channel.send(embed=embed)
          else:
            embed = discord.Embed(title="Locations", colour=discord.Colour(0x4a90e2), url="https://2b2tatlas.com/api/locations.php?search=" + keyword, description="Found: ", timestamp=datetime.datetime.utcnow())
            embed.set_author(name="PyBot", url="https://discordapp.com", icon_url="https://i.imgur.com/WgmKaoX.png")
            embed.set_footer(text="Bot by Bluefox#3699", icon_url="https://i.imgur.com/2BGKfWO.png")
            for i in jsons:
              name = i['name']
              x = i['x']
              y = str(i['y'])
              z = i['z']
              embed.add_field(name=name, value="\nCoords: X: " + x + " Y: " + y + " Z: " + z)
            await message.channel.send(embed=embed)
        if message.content.startswith("+post"):
          content = message.content.split(" ")[1]
          URL = "https://canary.discord.com/api/webhooks/914952397816754246/OClPnRemqypw5QO-_R3ON_WmVVjTEYF0BCnIpiYd2xCTC0K256GW620wmD66YxZGoAzD"
          posting = requests.post(URL, content)
          
          
          




client = Client()
keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)