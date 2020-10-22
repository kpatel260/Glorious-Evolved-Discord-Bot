#Returns wins/losses over the last 10 matches - IN PROGRESS
import os
import requests
import json
def getPlayerList(summonerName):
    apiKey = str(os.environ.get('riot-api-key'))
    summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + apiKey).json()
    currentMatchID = summonerData['id']
    
    currentMatch = requests.get('https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + currentMatchID + "?api_key=" + apiKey).json()
    participants = currentMatch["participants"]
    participantWinLossData = []
    for participant in participants:
        summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + participant['summonerName'] + "?api_key=" + apiKey).json()
        encryptedID = summonerData['accountId']
        matchHistory = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedID + "?api_key=" + apiKey).json()
        lastTen = matchHistory['matches']
        participantData = participant['summonerName'] + " "
        i = 0
        winLossString = ""
        while i < 5:
            matchOutcome = checkMatch(lastTen[i]["gameId"], participant['summonerName'])
            winLossString += matchOutcome
            i += 1
        participantData = "`%-17s %-10s`" % (participantData, winLossString)
        participantWinLossData.append(participantData)
        
    return participantWinLossData

#Checks whether the given match was a win or a loss then returns the appropriate symbol
def checkMatch(matchID, playerName):
    apiKey = str(os.environ.get('riot-api-key'))
    matchData = requests.get('https://na1.api.riotgames.com/lol/match/v4/matches/' + str(matchID) + "?api_key=" + apiKey).json()
    participants = matchData['participantIdentities']
    participantId = 0
    i = 0
    while i < 10:
        if participants[i]['player']['summonerName'] == playerName:
            participantId = i + 1
        i += 1
    if participantId < 6:
        if matchData['teams'][1]['win'] == "Fail":
            return "W"
        else:
            return "L"
    else:
        if matchData['teams'][1]['win'] == "Fail":
            return "L"
        else:
            return "W"
    
