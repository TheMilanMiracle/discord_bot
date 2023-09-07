from libs.client import *
from libs.guilds_and_channels import *
from libs.commands import *
import discord

import datetime as dtt


@botClient.event
async def on_ready():
  print(f"The bot is booted up, as {botClient.user}, with id {botClient.user.id}")
  
  #to sync the command tree with the bot client
  await botClient.tree.sync()
  


@botClient.event
async def on_message(message):
  if message.author == botClient.user:
    return
  

  
  else:
    if message.author.nick == "tester":
      if message.content.startswith("\\sleep"):
        print("going to sleep...")
        await botClient.close()
        
      if message.content.startswith("\\sync"):
        print("sync...")
        await botClient.tree.sync()

