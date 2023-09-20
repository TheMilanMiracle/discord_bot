import discord
from discord import app_commands


class BotClass(discord.Client):

  def __init__(self, *, intents: discord.Intents):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)


intents = discord.Intents.default()
intents.message_content = True
botClient = BotClass(intents=intents)
botClient.activity = discord.Activity(name="still testing...",type=0)