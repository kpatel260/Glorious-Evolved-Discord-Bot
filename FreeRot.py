#Returns a list of Champions on Free Rotation for the week
import discord
from discord.ext import commands
import os
import requests
import json
def getFreeRot():
    apiKey = str(os.environ.get('riot-api-key'))
    freeRot = requests.get('https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + apiKey).json()
    list = freeRot["freeChampionIds"]
    champNames = []
    embedVar = discord.Embed(title="Free Rotation", description="The following champions are on Free Rotation", color=0x000000)
    for int in list:
        champName = getChampTitles(int)
        embedVar.add_field(name= champName, value='\u200b')
    return embedVar
        
#Returns the name of the Champion corresponding to the given ID
def getChampName(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['id']

#Returns the title of the Champion corresponding to the given ID            
def getChampTitles(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['name'] + ', ' + champData['data'][key]['title']
