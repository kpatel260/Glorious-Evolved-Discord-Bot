#Returns an embed containing a list of commands for the bot
import os
import discord
from discord.ext import commands
import requests
import json
def getCommandList():
	embedVar = discord.Embed(title="Bot Commands", description="Here are all of the valid commands for The Glorious Evolved", color=0x000000)
	thumbnailURL = 'http://ddragon.leagueoflegends.com/cdn/10.19.1/img/champion/Viktor.png'
	embedVar.set_thumbnail(url=thumbnailURL)
	embedVar.add_field(name="!about", value="Returns a brief description of what I am.", inline=False)
	embedVar.add_field(name="!freeRot", value="Returns the current week's free rotation of champions.", inline=False)
	embedVar.add_field(name="!currentMatch [SummonerName]", value="Returns the summoner names and champions for the current game for a given summoner.", inline=False)
	embedVar.add_field(name="!teamMatchHistory [SummonerName]", value="Returns the outcome of the last 5 matches for each summoner in the given summoner's game.", inline=False)
	embedVar.add_field(name="!playerMatchHistory [SummonerName]", value="Returns a list of the last 10 matches for the given summoner.", inline=False)
	embedVar.add_field(name="!playerMatchData [summonerName] [gameNumber]", value="Returns in-depth match data for the given match taken from the last 10 matches for the given summoner.", inline=False)
	return embedVar
    