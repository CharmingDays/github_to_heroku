import discord
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is s.
bot = commands.Bot(command_prefix="s.")


#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")

    
@bot.command()

async def greet(msg,user:discord.Member):
    await msg.send(f"Hello there {user}")


@bot.command(aliases=['echo','copy','say'])
async def repeat(msg,*,message=None):
    if message == None:
        await msg.send("Enter a message to repeat")
    
    else:
        await msg.send(f"{msg.author.name}: {message}")
                   
@commands.has_any_role(["President","Owner"])
@bot.command()
async def ban(msg,*users:discord.Member):
    if not users:
        await msg.send("Please mention a user to ban")
    else:
        for i in users:
            await msg.guild.ban(i)                   

bot.run(os.environ['BOT_TOKEN'])
