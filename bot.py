import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="~", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    print("Bot Connected")

@client.tree.command(name="ping",description="pings bot")
async def slash_ping(interaction:discord.Interaction):
    await interaction.response.send_message("Commands: | ~ping | ~twitch | ~youtube | ~twitter | ~github | ~website | ~d4 | ~d6 | ~d8 | ~d10 | ~d12 | ~d20 |")

@client.tree.command(name="help",description="shows commands")
async def slash_help(interaction:discord.Interaction):
    await interaction.response.send_message("Commands: | ~ping | ~twitch | ~youtube | ~twitter | ~github | ~website | ~d4 | ~d6 | ~d8 | ~d10 | ~d12 | ~d20 |")

@client.command(brief="Pings Bot", description="Pings Bot")
async def ping(ctx):
    await ctx.send("Bot Pinged")

@client.command(brief="help menu", description="shows list of all commands")
async def h(ctx):
    await ctx.send("Commands: | ~help | ~ping | ~twitch | ~youtube | ~twitter | ~github | ~website | ~d4 | ~d6 | ~d8 | ~d10 | ~d12 | ~d20 |")

@client.command(brief="links STORM's Twitch", description="links STORM_VTUBER on twitch.tv")
async def twitch(ctx):
    await ctx.send("https://www.twitch.tv/storm_vtuber")

@client.command(brief="links STORM's youtube", description="links STORM's youtube")
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/@STORM_VTUBER")

@client.command(brief="links STORM's Twitter", description="links STORM's twitter") 
async def twitter(ctx):
    await ctx.send("https://x.com/STORM_Plus")

@client.command(brief="links STORM's Github", description="links STORM's github")
async def github(ctx):
    await ctx.send("https://github.com/STORM-MCCTC")

@client.command(brief="links STORM's Website", description="links STORM's website")
async def website(ctx):
    await ctx.send("https://storm-mcctc.github.io/STORM-Funny-webpage/")

@client.command(brief="Roll a D4", description="Rolls a Four sided Dice")
async def d4(ctx):
    D4L = [1, 2, 3, 4]
    D4 = random.choice(D4L)
    await ctx.send(f"You rolled {D4} on a D4")

@client.command(brief="Roll a D6", description="Rolls a Six sided Dice")
async def d6(ctx):
    D6L = [1, 2, 3, 4, 5, 6]
    D6 = random.choice(D6L)
    await ctx.send(f"You rolled {D6} on a D6")

@client.command(brief="Roll a D8", description="Rolls a Eight sided Dice")
async def d8(ctx):
    D8L = [1, 2, 3, 4, 5, 6, 7, 8]
    D8 = random.choice(D8L)
    await ctx.send(f"You rolled {D8} on a D8")

@client.command(brief="Roll a D10", description="Rolls a Ten sided Dice")
async def d10(ctx):
    D10L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D10 = random.choice(D10L)
    await ctx.send(f"You rolled {D10} on a D10")

@client.command(brief="Roll a D12", description="Rolls a Twelve sided Dice")
async def d12(ctx):
    D12L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    D12 = random.choice(D12L)
    await ctx.send(f"You rolled {D12} on a D12")

@client.command(brief="Roll a D20", description="Rolls a twenty sided Dice")
async def d20(ctx):
    D20L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    D20 = random.choice(D20L)
    await ctx.send(f"You rolled {D20} on a D20")

with open("Bot_token.txt") as f:
    token = f.read()

client.run(token)