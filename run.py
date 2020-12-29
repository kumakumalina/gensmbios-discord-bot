# bot.py
import discord
import random
import json
import os
from discord.ext import commands

with open("config.json") as f:
    extensions = json.load(f)

def load_extensions():
    for extension in extensions["extension"]:
        try:
            bot.load_extension(extension)
            print("Loading",format(extension),"...Done")
        except Exception as e:
            print("Failed loading {}: {}".format(extension, e))

bot = commands.Bot(command_prefix='>/')

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    await bot.change_presence(activity=discord.Game(name=f"Cooking ACPI with アキくん ʕ•ᴥ•ʔ☆"))
    load_extensions()

#Welcome new member
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server |･`)ﾉ"
    )

bot.run(os.environ.get("TOKEN"))