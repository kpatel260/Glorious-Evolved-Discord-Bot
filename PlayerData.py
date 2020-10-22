#Returns an embed containing data for the current match for a specific player - IN PROGRESS
import os
import discord
from discord.ext import commands
import requests
import json
def getPlayerData(summonerName):
    apiKey = str(os.environ.get('riot-api-key'))
    summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + apiKey).json()
    currentMatchID = summonerData['id']
    
    currentMatch = requests.get('https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + currentMatchID + "?api_key=" + apiKey).json()
    list = currentMatch["participants"]
    for participant in list:
        if summonerName == participant['summonerName']:
            champName = getChampName(participant['championId'])
        
    embedVar = discord.Embed(title=summonerName, description=champName, color=0x00ff00)
    thumbnailURL = 'http://ddragon.leagueoflegends.com/cdn/10.16.1/img/champion/' + champName + '.png'
    embedVar.set_thumbnail(url=thumbnailURL)
    embedVar.set_author(name="Flash", icon_url="http://ddragon.leagueoflegends.com/cdn/10.16.1/img/spell/SummonerFlash.png")
    embedVar.set_author(name="Flash", icon_url="http://ddragon.leagueoflegends.com/cdn/10.16.1/img/spell/SummonerFlash.png")
    embedVar.set_footer(text="Flash", icon_url="http://ddragon.leagueoflegends.com/cdn/10.16.1/img/spell/SummonerFlash.png")
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    
    
    return embedVar


def getChampName(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['id']
