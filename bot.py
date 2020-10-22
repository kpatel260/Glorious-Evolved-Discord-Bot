# bot.py
import FreeRot
import CurrentMatch
import PlayerData
import LastTenMatches
import PlayerMatchHistory
import PastMatchData
import CommandList
import AboutMe
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def freeRot(ctx):
    champs = FreeRot.getFreeRot()
    await ctx.send(embed=champs)

@client.command()
async def currentMatch(ctx, arg):
    participants = CurrentMatch.getPlayerList(arg)
    await ctx.send(embed=participants)
    
@client.command()
async def data(ctx, arg):
    embedVar = PlayerData.getPlayerData(arg)
    await ctx.send(embed=embedVar)

@client.command()
async def teamMatchHistory(ctx, arg):
    matchHistories = LastTenMatches.getPlayerList(arg)
    for participant in matchHistories:
        await ctx.send(participant)

@client.command()
async def playerMatchHistory(ctx, arg):
    matchHistory = PlayerMatchHistory.getPlayerList(arg)
    await ctx.send(embed=matchHistory)

@client.command()
async def playerMatchData(ctx, arg1, arg2):
    matchData = PastMatchData.getSpecificMatch(arg1, arg2)
    for match in matchData:
        await ctx.send(match)

@client.command()
async def commands(ctx):
    embedVar = CommandList.getCommandList()
    await ctx.send(embed=embedVar)

@client.command()
async def about(ctx):
    embedVar = AboutMe.getAboutEmbed()
    await ctx.send(embed=embedVar)


client.run('')
