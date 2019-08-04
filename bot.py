import discord
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is a.
bot = commands.Bot(command_prefix="$")


#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")


@bot.command()
async def greet(msg, *users: discord.Member):
    names=[user.name for user in users]
    await msg.send(f"Hello there {' '.join(names)}")

@bot.command()
async def repeat(msg,*,message=None):
    if message == None:
        await msg.send("Enter a message to repeat")
    
    else:
        await msg.send(f"{msg.author.name}: {message}")

bot.run(os.environ['BOT_TOKEN'])
