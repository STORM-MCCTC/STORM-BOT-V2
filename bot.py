import discord
from discord.ext import commands

client = commands.Bot(command_prefix="~~", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot Connected")

@client.command()
async def ping(ctx):
    await ctx.send("Bot Pinged")

@client.command()
async def h(ctx):
    await ctx.send("commands: | ~~ping | ~~twitch | ")

@client.command()
async def twitch(ctx):
    await ctx.send("https://www.twitch.tv/storm_vtuber")

with open("Bot_token.txt") as f:
    token = f.read()

client.run(token)
