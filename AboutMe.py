#Returns an embed containing a list of commands for the bot
import os
import discord
from discord.ext import commands
import requests
import json
def getAboutEmbed():
	embedVar = discord.Embed(title="About Me", description="I am a bot designed to work with the Riot Games API to provide data about past and live matches for any summoner. The Glorious Evolved isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.", color=0x000000)
	thumbnailURL = 'http://ddragon.leagueoflegends.com/cdn/10.19.1/img/champion/Viktor.png'
	embedVar.set_thumbnail(url=thumbnailURL)
	embedVar.add_field(name="Developer", value="Absol260")
	return embedVar
    