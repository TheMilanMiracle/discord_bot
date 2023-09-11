from libs.client import *
from libs.guilds_and_channels import *
from media.files import *
import discord
import random as r

@botClient.tree.command(name="hello", description="salute the comrade bot!", guilds = GUILDS_LIST)
async def hello_command(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hello!")
    

@botClient.tree.command(name="operate", description="make the bot operate a simple set of operations", guilds = GUILDS_LIST)
async def operate_command(interaction:discord.Interaction, operation: str):
    print(f"'operate {operation}' called")
    await interaction.response.send_message(f"{operation} = {eval(operation)}")
    

@botClient.tree.command(name="avatar", description="can show a bigger version of the avatar of a member",guilds = GUILDS_LIST)
async def avatar_command(interaction:discord.Interaction, member:discord.Member):
    await interaction.response.send_message(member.display_avatar)
    

@botClient.tree.command(name="casino", description="actions: [register/balance]", guilds = GUILDS_LIST)
async def casino_command(interaction: discord.Interaction, action: str):
    member = interaction.user
    
    print(f"casino '{action} {member.name}' called")
    
    if action == "register":
        
        dataR = open("libs/data/CasinoBags_data.txt", "r")
        
        registered = False
        for line in dataR:
            line = line.strip("\n").split("|")
            
            if line[0] != "[id]" and member.id == int(line[0]):
                registered = True
                break
        
        dataR.close()
        
        if registered:
            await interaction.response.send_message(content=f"The user {member.name} is already registered", silent=True)
            
        else:
            dataA = open("libs/data/CasinoBags_data.txt", "a")
            dataA.write(f"\n{member.id}|{0}")
            
            await interaction.response.send_message(content=f"Welcome {member.name} to the casino!")
            
    elif action == "balance":
        
        dataR = open("libs/data/CasinoBags_data.txt", "r")
        
        found = False
        for line in dataR:
            line = line.strip("\n").split("|")
            
            if line[0] != "[id]" and member.id == int(line[0]):
                found = True
                balance = int(line[1])
                break
        
        if found:
            await interaction.response.send_message(content=f"The balance for user {member.name} is {balance} tokens!", silent=True)
            
        else:
            await interaction.response.send_message(content=f"The user {member.name} is not registered",silent=True)