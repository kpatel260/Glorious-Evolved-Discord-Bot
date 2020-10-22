import os
import requests
import json
import discord
from discord.ext import commands
def getPlayerList(summonerName):
    apiKey = str(os.environ.get('riot-api-key'))
    embedVar = discord.Embed(title="Match History", description=("Last Twelve Matches for " + summonerName), color=0x000000)
    summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" +  apiKey).json()
    encryptedId = summonerData['accountId']
    matchList = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedId + "?api_key=" + apiKey).json()
    thumbnailURL = "http://ddragon.leagueoflegends.com/cdn/10.19.1/img/profileicon/" + str(summonerData['profileIconId']) + ".png"
    embedVar.set_thumbnail(url=thumbnailURL)
    i = 0
    while i < 12:
        matchTitle = "Game #" + str(i + 1) + ": "
        matchData = requests.get("https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchList['matches'][i]['gameId']) + "?api_key=" + apiKey).json()
        matchDescription = matchData["gameMode"]
        matchDescription += " - "
        matchParticipants = matchData["participantIdentities"]
        j = 0
        participantId = 0
        while j < 10:
            if matchParticipants[j]["player"]["summonerName"] == summonerName:
                participantId = j + 1
            j += 1
        participants = matchData["participants"]
        champId = participants[participantId - 1]["championId"]
        champName = getChampName(champId)
        matchDescription += champName
        embedVar.add_field(name=matchTitle, value=matchDescription)
        i += 1
    return embedVar


#Returns the name of the Champion corresponding to the given ID
def getChampName(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.19.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['id']
