import discord
from discord.ext import commands

client = commands.Bot(command_prefix="~", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot Connected")

@client.command()
async def ping(ctx):
    await ctx.send("Bot Pinged")

@client.command()
async def h(ctx):
    await ctx.send("commands: | ~ping | ~twitch | ~youtube | ~twitter | ~github | ~website |")

@client.command()
async def twitch(ctx):
    await ctx.send("https://www.twitch.tv/storm_vtuber")

@client.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/@STORM_VTUBER")

@client.command()
async def twitter(ctx):
    await ctx.send("https://x.com/STORM_Plus")

@client.command()
async def github(ctx):
    await ctx.send("https://github.com/STORM-MCCTC")

@client.command()
async def website(ctx):
    await ctx.send("https://storm-mcctc.github.io/STORM-Funny-webpage/")

with open("Bot_token.txt") as f:
    token = f.read()

client.run(token)
