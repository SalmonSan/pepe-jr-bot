import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.content == "!pear":
        await client.send_message(message.channel, ":pear:")
        


client.run("NDg1MTQzNTU0ODMwNzYyMDAw.DmvA_g.M-_AhUIaqpd6Q1Zc5UWVP1EZ4xI")
