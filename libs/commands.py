from libs.client import *
from libs.guilds_and_channels import *
from media.files import *
import discord
import typing
import random
import time

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


@botClient.tree.command(name="casino", description="come and fullfil yout gambling addiction", guilds = GUILDS_LIST)
async def casino_command(interaction: discord.Interaction, action: str):
    member = interaction.user
    
    print(f"casino '{action} {member.name}' called by {member.name}")
    
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
            
            await interaction.response.send_message(content=f"Welcome {member.name} to the casino!", silent=True)
            
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
            
@casino_command.autocomplete("action")
async def casino_autocomplete(interaction: discord.Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
    data = []
    for action in ["register", "balance"]:
        if current in action:
            data.append(app_commands.Choice(name=action, value=action))
    return data


@botClient.tree.command(name="roulette", guilds=GUILDS_LIST)
@app_commands.describe(action="[chart]: to see prizes table, [bet]: to make a bet")
@app_commands.describe(bet="add your bet only if you are making one")
@app_commands.describe(number="the number you want to bet on")
@app_commands.describe(tokens="the amount of tokens you want to bet")
async def roullete_command(interaction: discord.Interaction, action: str, bet: str = "", number: int = 0, tokens: int = 0):
    member = interaction.user
    
    print(f"roulette '{action} ({bet},{tokens})' called by {member.name}")
    
    if action == "chart":
        
        chart = "-------------------------"
        prizes = {
            1: ["[singular]      ","bet","x","36"],
            2: ["[1st/2nd/3rd 12]","bet","x","12"],
            3: ["[even/odd]      ","bet","x"," 2"],
            4: ["[red/black]     ","bet","x"," 2"]
            
        }
        for key, list in prizes.items():
            a,b,c,d = list
            chart += "\n{:16} {:3} {:1} {:2}".format(a,b,c,d)
        
        chart += "\n-------------------------"
        
        await interaction.response.send_message(content=f"{chart}", silent=True)
    
    elif action == "bet":
        
        dataR = open("libs/data/CasinoBags_Data.txt","r")
        
        hasEnough = True
        for line in dataR:
            line = line.strip("\n").split("|")
            
            if line[0] != "[id]" and int(line[0]) == member.id:
                
                if int(line[1]) < tokens:
                    hasEnough = False
                
                break
        
        if hasEnough:
            
            await interaction.response.send_message(content=f"Watch Out!{member.name} is betting {tokens} tokens!", silent=True, file=rouletteGif)
            
            options = [i for i in range(0,37)]
            
            black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
            
            result = random.choice(options)
            
            
            time.sleep(8)
            
            won = False
            if bet == "singular" and result == number:
                won = True
                multiplier = 36
            elif (bet == "first12" and (result <= 12)) or (bet == "second12" and (result >= 13 and result <= 24)) or (bet == "third12" and (result >= 25)):
                won = True
                multiplier = 12
            elif (bet == "black" and result in black) or (bet == "red" and result not in black and result != 0):
                won = True
                multiplier = 2
            elif (bet == "even" and result%2 == 2) or (bet == "odd" and result%2 != 2):
                won = True
                multiplier = 2
            
            if won:
                await interaction.edit_original_response(content=f"The result was... {result}! you won {tokens * multiplier} tokens!")
            
            else:
                await interaction.edit_original_response(content=f"The result was... {result}! Sorry, you lost")
            
        else:
            
            await interaction.response.send_message(content=f"You don't have enough token to make that bet", silent=True)

            
                
        
    
    else:
        
        await interaction.response.send_message(content=f"Unknown action. Try again!", silent=True)
        
