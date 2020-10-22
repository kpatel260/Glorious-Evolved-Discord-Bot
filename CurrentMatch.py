#Retrieves a list of Summoner Names and Champions for the current match with the given Summoner
import os
import requests
import json
import discord
def getPlayerList(summonerName):
    apiKey = str(os.environ.get('riot-api-key'))
    embedVar = discord.Embed(title="Live Match", description=("Live match data for " + summonerName), color=0x000000)
    summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + apiKey).json()
    currentMatchID = summonerData['id']
    currentMatch = requests.get('https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + currentMatchID + "?api_key=" + apiKey).json()
    if "status" in currentMatch:
        embedVar.add_field(name="ERROR: ", value=(summonerName + " is not currently in a League of Legends game!"))
        return embedVar
    list = currentMatch["participants"]
    participantNames = []
    for participant in list:
        embedVar.add_field(name=participant['summonerName'], value=getChampName(participant['championId']), inline=False)
        participantNames.append('`%-17s %-10s`' % (participant['summonerName'], getChampName(participant['championId'])))
    return embedVar
        
#Returns the name of the Champion corresponding to the given ID
def getChampName(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.16.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['id']
            
