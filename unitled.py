import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready. Also WotScript Best Lang. Also fuck that one Felix guy who said C++ sucks for game development.")

@client.event
async def on_message(message):
    if message.content.upper == "!PEAR": 
        await client.send_message(message.channel, ":pear:")    #Now that we added ".upper", the bot can now answer at these commands capitalized
    if message.content.upper == "!GITHUB" or message.content.upper == "!GHUB": 
        await client.send_message(message.channel, "https://github.com/SalmonSan/pepe-jr-bot" % (userID))
    if message.content.upper == "!PING": 
        await client.send_message(message.channel, "<@%s> pong")
    if message.content.upper == "!ANIMEWASAMISTAKE" or message.content.upper == "!ANIME" or message.content.upper == "!AWAM": 
        await client.send_message(message.channel, "I'm sorry to say this, but <@%s>, anime was a mistake." % (userID))
    if message.content.upper == "!LENNY": 
        await client.send_message(message.channel, "( ͡° ͜ʖ ͡°)" % (userID))
                
client.run("NDg1MTQzNTU0ODMwNzYyMDAw.DmvA_g.M-_AhUIaqpd6Q1Zc5UWVP1EZ4xI")
