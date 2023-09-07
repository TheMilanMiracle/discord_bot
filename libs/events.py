import libs.client as bc
import libs.guilds_and_channels as gc
import discord

import datetime as dtt


@bc.botClient.event
async def on_ready():
  print(f"The bot is booted up, as {bc.botClient.user}, with id {bc.botClient.user.id}")
  for guild in bc.botClient.guilds:
    gc.GUILDS_LIST.append(guild)
    for channel in bc.botClient.get_all_channels():
      if channel.name == "bot":
        gc.CHANNELS_LIST.append(channel.id)
