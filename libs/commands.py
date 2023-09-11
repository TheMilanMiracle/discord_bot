from libs.client import *
import discord

@botClient.tree.command(name="hello", description="salute the comrade bot!")
async def hello_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello!")
    


@botClient.tree.command(name="operate", description="make the bot operate a simple set of operations")
async def operate_command(interaction:discord.Interaction):
    print(f"{interaction.message}, {interaction.data}")
    await interaction.response.send_message("operate")
    

@botClient.tree.command(name="avatar", description="can show a bigger version of the avatar of a member")
async def avatar_command(interaction:discord.Interaction, member:discord.Member):
    await interaction.response.send_message(member.display_avatar)
    

@botClient.tree.context_menu(name="roulette1")
async def roulette_command1(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message("test", ephemeral=True)
    
@botClient.tree.command(name="roulette2", description="Rolls the roullete. Bet your points here!")
async def roulette_command2(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"Your message was {message}", ephemeral=True)