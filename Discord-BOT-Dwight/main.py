import discord
from discord.ext import commands
import music
from keepalive import keep_alive


cogs = [music]

client = commands.Bot(command_prefix='-', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

  
  

keep_alive()
client.run("OTE2OTE0NjYyODI4ODAyMDg5.YaxFUw.EKrtsL9Iv0VR8YoaqMTeCEb0ytk")



