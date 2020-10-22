import os
import requests
import json
def getSpecificMatch(summonerName, matchNum):
	apiKey = str(os.environ.get('riot-api-key'))
	#print(apiKey)
	summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" +  apiKey).json()
	encryptedId = summonerData['accountId']
	matchList = requests.get("https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedId + "?api_key=" + apiKey).json()
	matchData = requests.get("https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchList['matches'][int(matchNum) - 1]['gameId']) + "?api_key=" + apiKey).json()
	itemData = requests.get("http://ddragon.leagueoflegends.com/cdn/10.19.1/data/en_US/item.json").json()
	itemList = itemData['data']
	runeData = requests.get("http://ddragon.leagueoflegends.com/cdn/10.19.1/data/en_US/runesReforged.json").json()
	summonerSpellData = requests.get("http://ddragon.leagueoflegends.com/cdn/9.19.1/data/en_US/summoner.json").json()
	matchDataStrings = []
	


	gameMode = ""
	if(matchData['gameMode'] == "CLASSIC"):
		gameMode = "Summoner's Rift"
	elif(matchData['gameMode'] == "ARAM"):
		gameMode = "All Random All Mid"

	queueType = ""
	if(matchData['queueId'] == 400):
		queueType = "5v5 Draft Pick"
	elif(matchData['queueId'] == 420):
		queueType = "5v5 Ranked Solo"
	elif(matchData['queueId'] == 430):
		queueType = "5v5 Blind Pick"
	elif(matchData['queueId'] == 440):
		queueType = "5v5 Ranked Flex"
	elif(matchData['queueId'] == 450):
		queueType = "5v5 ARAM"
	
	gameLength = ""
	seconds = matchData['gameDuration']
	minutes = int(seconds / 60)
	seconds = seconds % 60
	if(seconds < 10):
		gameLength = str(minutes) + ":0" + str(seconds)
	else:
		gameLength = str(minutes) + ":" + str(seconds)
	

	gameType = "";
	if(matchData['gameType'] == "MATCHED_GAME"):
		gameType = "Matchmade Game"
	elif(matchData['gameType'] == "CUSTOM_GAME"):
		gameType = "Custom Game"

	matchDataStrings.append("`{:20} | {:16} | {:5} | {:15}`".format(gameMode, queueType, gameLength, gameType))
	participantData = matchData['participants']
	participantIdentities = matchData['participantIdentities']
	teamOneData = matchData['teams'][0]

	teamOneWinCond = ""
	if(teamOneData['win'] == "Win"):
		teamOneWinCond = "Victory"
	else:
		teamOneWinCond = "Defeat"
	teamOneDragons = "Dragons: " + str(teamOneData['dragonKills'])
	teamOneTowers = "Towers: " + str(teamOneData['towerKills'])
	teamOneBarons = "Barons: " + str(teamOneData['baronKills'])

	matchDataStrings.append("`{:8} | {:9} | {:12} | {:12} | {:11}`".format(teamOneWinCond, "Blue Team", teamOneDragons, teamOneTowers, teamOneBarons))
	i = 0
	while i < 5:
		summonerName = participantIdentities[i]['player']['summonerName']
		champion = str(participantData[i]['stats']['champLevel']) + " - " + getChampName(participantData[i]['championId'])
		summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" +  apiKey).json()
		summonerRankData = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerData['id'] + "?api_key=" + apiKey).json()
		j = 0
		while j < len(summonerRankData):
			if summonerRankData[j]['queueType'] == "RANKED_SOLO_5x5":
				summonerRank = str(summonerRankData[j]['tier']) + " " + str(summonerRankData[j]['rank'])
			j += 1
		kda = str(participantData[i]['stats']['kills']) + "/" + str(participantData[i]['stats']['deaths']) + "/" + str(participantData[i]['stats']['assists'])
		damageDealt = "Damage Dealt: " + str(participantData[i]['stats']['totalDamageDealt'])
		wardScore = "Vision Score: " + str(participantData[i]['stats']['visionScore'])
		cs = "CS: " + str(participantData[i]['stats']['totalMinionsKilled'] + participantData[i]['stats']['neutralMinionsKilled']) 
		summonerSpell1 = participantData[i]['spell1Id']
		summonerSpell1Name = ""
		if summonerSpell1 == 21:
			summonerSpell1Name = "Barrier"
		elif summonerSpell1 == 1:
			summonerSpell1Name = "Cleanse"
		elif summonerSpell1 == 14:
			summonerSpell1Name = "Ignite"
		elif summonerSpell1 == 3:
			summonerSpell1Name = "Exhaust"
		elif summonerSpell1 == 4:
			summonerSpell1Name = "Flash"
		elif summonerSpell1 == 6:
			summonerSpell1Name = "Ghost"
		elif summonerSpell1 == 7:
			summonerSpell1Name = "Heal"
		elif summonerSpell1 == 13:
			summonerSpell1Name = "Clarity"
		elif summonerSpell1 == 11:
			summonerSpell1Name = "Smite"
		elif summonerSpell1 == 32:
			summonerSpell1Name = "Snowball"
		elif summonerSpell1 == 12:
			summonerSpell1Name = "Teleport"
		
		summonerSpell2 = participantData[i]['spell2Id']
		summonerSpell2Name = ""
		if summonerSpell2 == 21:
			summonerSpell2Name = "Barrier"
		elif summonerSpell2 == 1:
			summonerSpell2Name = "Cleanse"
		elif summonerSpell2 == 14:
			summonerSpell2Name = "Ignite"
		elif summonerSpell2 == 3:
			summonerSpell2Name = "Exhaust"
		elif summonerSpell2 == 4:
			summonerSpell2Name = "Flash"
		elif summonerSpell2 == 6:
			summonerSpell2Name = "Ghost"
		elif summonerSpell2 == 7:
			summonerSpell2Name = "Heal"
		elif summonerSpell2 == 13:
			summonerSpell2Name = "Clarity"
		elif summonerSpell2 == 11:
			summonerSpell2Name = "Smite"
		elif summonerSpell2 == 32:
			summonerSpell2Name = "Snowball"
		elif summonerSpell2 == 12:
			summonerSpell2Name = "Teleport"
		
		
		
		

		matchDataStrings.append("`{:20} | {:15} | {:10} | {:10} | {:23} | {:18} | {:8} | {:10} | {:10}`".format(summonerName, champion, summonerRank, kda, damageDealt, wardScore, cs, summonerSpell1Name, summonerSpell2Name))

		item0 = participantData[i]['stats']['item0']
		item1 = participantData[i]['stats']['item1']
		item2 = participantData[i]['stats']['item2']
		item3 = participantData[i]['stats']['item3']
		item4 = participantData[i]['stats']['item4']
		item5 = participantData[i]['stats']['item5']
		item6 = participantData[i]['stats']['item6']
		if item0 != 0:
			item0Name = itemList[str(item0)]['name']
		else:
			item0Name = ""
		if item1 != 0:
			item1Name = itemList[str(item1)]['name']
		else:
			item1Name = ""
		if item2 != 0:
			item2Name = itemList[str(item2)]['name']
		else:
			item2Name = ""
		if item3 != 0:
			item3Name = itemList[str(item3)]['name']
		else:
			item3Name = ""
		if item4 != 0:
			item4Name = itemList[str(item4)]['name']
		else:
			item4Name = ""
		if item5 != 0:
			item5Name = itemList[str(item5)]['name']
		else:
			item5Name = ""
		if item6 != 0:
			item6Name = itemList[str(item6)]['name']
		else:
			item6Name = ""
		

		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("Items ", item0Name, item1Name, item2Name, "                       "))
		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("                       ", item3Name, item4Name, item5Name, item6Name))
		
		primaryRunePath = participantData[i]['stats']['perkPrimaryStyle']
		secondaryRunePath = participantData[i]['stats']['perkSubStyle']
		j = 0
		while j < len(runeData):
			if runeData[j]['id'] == primaryRunePath:
				primaryRunePathId = j
			j += 1
		j = 0
		while j < len(runeData):
			if runeData[j]['id'] == secondaryRunePath:
				secondaryRunePathId = j
			j += 1

		rune0 = participantData[i]['stats']['perk0']
		rune1 = participantData[i]['stats']['perk1']
		rune2 = participantData[i]['stats']['perk2']
		rune3 = participantData[i]['stats']['perk3']
		rune4 = participantData[i]['stats']['perk4']
		rune5 = participantData[i]['stats']['perk5']

		primaryRuneData = runeData[primaryRunePathId]
		secondaryRuneData = runeData[secondaryRunePathId]
		j = 0
		while j < len(primaryRuneData['slots'][0]['runes']):
			if primaryRuneData['slots'][0]['runes'][j]['id'] == rune0:
				rune0Name = primaryRuneData['slots'][0]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][1]['runes'][j]['id'] == rune1:
				rune1Name = primaryRuneData['slots'][1]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][2]['runes'][j]['id'] == rune2:
				rune2Name = primaryRuneData['slots'][2]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][3]['runes'][j]['id'] == rune3:
				rune3Name = primaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		rune4Name = ""
		j = 0
		while j < 3:
			if secondaryRuneData['slots'][1]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][1]['runes'][j]['name']
			elif secondaryRuneData['slots'][2]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][2]['runes'][j]['name']
			elif secondaryRuneData['slots'][3]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		rune5Name = ""
		j = 0
		while j < 3:
			if secondaryRuneData['slots'][1]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][1]['runes'][j]['name']
			elif secondaryRuneData['slots'][2]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][2]['runes'][j]['name']
			elif secondaryRuneData['slots'][3]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("Runes                  ", rune0Name, rune1Name, rune2Name, rune3Name))
		matchDataStrings.append("`{:25} {:25} | {:25} |`".format("                       ", rune4Name, rune5Name))
		matchDataStrings.append("`---------------------------------------------------------------------------------------------------------------------------------------`")
		i += 1


	matchDataStrings.append("`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
	matchDataStrings.append("`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

	teamTwoData = matchData['teams'][1]

	teamTwoWinCond = ""
	if(teamTwoData['win'] == "Win"):
		teamTwoWinCond = "Victory"
	else:
		teamTwoWinCond = "Defeat"
	teamTwoDragons = "Dragons: " + str(teamTwoData['dragonKills'])
	teamTwoTowers = "Towers: " + str(teamTwoData['towerKills'])
	teamTwoBarons = "Barons: " + str(teamTwoData['baronKills'])

	matchDataStrings.append("`{:8} | {:9} | {:12} | {:12} | {:11}`".format(teamTwoWinCond, "Red Team", teamTwoDragons, teamTwoTowers, teamTwoBarons))
	i = 5
	while i < 10:
		summonerName = participantIdentities[i]['player']['summonerName']
		champion = str(participantData[i]['stats']['champLevel']) + " - " + getChampName(participantData[i]['championId'])
		summonerData = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" +  apiKey).json()
		summonerRankData = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerData['id'] + "?api_key=" + apiKey).json()
		j = 0
		while j < len(summonerRankData):
			if summonerRankData[j]['queueType'] == "RANKED_SOLO_5x5":
				summonerRank = str(summonerRankData[j]['tier']) + " " + str(summonerRankData[j]['rank'])
			j += 1
		kda = str(participantData[i]['stats']['kills']) + "/" + str(participantData[i]['stats']['deaths']) + "/" + str(participantData[i]['stats']['assists'])
		damageDealt = "Damage Dealt: " + str(participantData[i]['stats']['totalDamageDealt'])
		wardScore = "Vision Score: " + str(participantData[i]['stats']['visionScore'])
		cs = "CS: " + str(participantData[i]['stats']['totalMinionsKilled'] + participantData[i]['stats']['neutralMinionsKilled'])
		summonerSpell1 = participantData[i]['spell1Id']
		summonerSpell1Name = ""
		if summonerSpell1 == 21:
			summonerSpell1Name = "Barrier"
		elif summonerSpell1 == 1:
			summonerSpell1Name = "Cleanse"
		elif summonerSpell1 == 14:
			summonerSpell1Name = "Ignite"
		elif summonerSpell1 == 3:
			summonerSpell1Name = "Exhaust"
		elif summonerSpell1 == 4:
			summonerSpell1Name = "Flash"
		elif summonerSpell1 == 6:
			summonerSpell1Name = "Ghost"
		elif summonerSpell1 == 7:
			summonerSpell1Name = "Heal"
		elif summonerSpell1 == 13:
			summonerSpell1Name = "Clarity"
		elif summonerSpell1 == 11:
			summonerSpell1Name = "Smite"
		elif summonerSpell1 == 32:
			summonerSpell1Name = "Snowball"
		elif summonerSpell1 == 12:
			summonerSpell1Name = "Teleport"
		
		summonerSpell2 = participantData[i]['spell2Id']
		summonerSpell2Name = ""
		if summonerSpell2 == 21:
			summonerSpell2Name = "Barrier"
		elif summonerSpell2 == 1:
			summonerSpell2Name = "Cleanse"
		elif summonerSpell2 == 14:
			summonerSpell2Name = "Ignite"
		elif summonerSpell2 == 3:
			summonerSpell2Name = "Exhaust"
		elif summonerSpell2 == 4:
			summonerSpell2Name = "Flash"
		elif summonerSpell2 == 6:
			summonerSpell2Name = "Ghost"
		elif summonerSpell2 == 7:
			summonerSpell2Name = "Heal"
		elif summonerSpell2 == 13:
			summonerSpell2Name = "Clarity"
		elif summonerSpell2 == 11:
			summonerSpell2Name = "Smite"
		elif summonerSpell2 == 32:
			summonerSpell2Name = "Snowball"
		elif summonerSpell2 == 12:
			summonerSpell2Name = "Teleport"
		
		
		
		

		matchDataStrings.append("`{:20} | {:15} | {:10} | {:10} | {:23} | {:18} | {:8} | {:10} | {:10}`".format(summonerName, champion, summonerRank, kda, damageDealt, wardScore, cs, summonerSpell1Name, summonerSpell2Name))

		item0 = participantData[i]['stats']['item0']
		item1 = participantData[i]['stats']['item1']
		item2 = participantData[i]['stats']['item2']
		item3 = participantData[i]['stats']['item3']
		item4 = participantData[i]['stats']['item4']
		item5 = participantData[i]['stats']['item5']
		item6 = participantData[i]['stats']['item6']
		if item0 != 0:
			item0Name = itemList[str(item0)]['name']
		else:
			item0Name = ""
		if item1 != 0:
			item1Name = itemList[str(item1)]['name']
		else:
			item1Name = ""
		if item2 != 0:
			item2Name = itemList[str(item2)]['name']
		else:
			item2Name = ""
		if item3 != 0:
			item3Name = itemList[str(item3)]['name']
		else:
			item3Name = ""
		if item4 != 0:
			item4Name = itemList[str(item4)]['name']
		else:
			item4Name = ""
		if item5 != 0:
			item5Name = itemList[str(item5)]['name']
		else:
			item5Name = ""
		if item6 != 0:
			item6Name = itemList[str(item6)]['name']
		else:
			item6Name = ""
		

		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("Items ", item0Name, item1Name, item2Name, "                       "))
		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("                       ", item3Name, item4Name, item5Name, item6Name))
		
		primaryRunePath = participantData[i]['stats']['perkPrimaryStyle']
		secondaryRunePath = participantData[i]['stats']['perkSubStyle']
		j = 0
		while j < len(runeData):
			if runeData[j]['id'] == primaryRunePath:
				primaryRunePathId = j
			j += 1
		j = 0
		while j < len(runeData):
			if runeData[j]['id'] == secondaryRunePath:
				secondaryRunePathId = j
			j += 1

		rune0 = participantData[i]['stats']['perk0']
		rune1 = participantData[i]['stats']['perk1']
		rune2 = participantData[i]['stats']['perk2']
		rune3 = participantData[i]['stats']['perk3']
		rune4 = participantData[i]['stats']['perk4']
		rune5 = participantData[i]['stats']['perk5']

		primaryRuneData = runeData[primaryRunePathId]
		secondaryRuneData = runeData[secondaryRunePathId]
		j = 0
		while j < len(primaryRuneData['slots'][0]['runes']):
			if primaryRuneData['slots'][0]['runes'][j]['id'] == rune0:
				rune0Name = primaryRuneData['slots'][0]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][1]['runes'][j]['id'] == rune1:
				rune1Name = primaryRuneData['slots'][1]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][2]['runes'][j]['id'] == rune2:
				rune2Name = primaryRuneData['slots'][2]['runes'][j]['name']
			j += 1
		j = 0
		while j < 3:
			if primaryRuneData['slots'][3]['runes'][j]['id'] == rune3:
				rune3Name = primaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		j = 0
		while j < 3:
			if secondaryRuneData['slots'][1]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][1]['runes'][j]['name']
			elif secondaryRuneData['slots'][2]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][2]['runes'][j]['name']
			elif secondaryRuneData['slots'][3]['runes'][j]['id'] == rune4:
				rune4Name = secondaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		j = 0
		while j < 3:
			if secondaryRuneData['slots'][1]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][1]['runes'][j]['name']
			elif secondaryRuneData['slots'][2]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][2]['runes'][j]['name']
			elif secondaryRuneData['slots'][3]['runes'][j]['id'] == rune5:
				rune5Name = secondaryRuneData['slots'][3]['runes'][j]['name']
			j += 1

		matchDataStrings.append("`{:25} {:25} | {:25} | {:25} | {:25}`".format("Runes                  ", rune0Name, rune1Name, rune2Name, rune3Name))
		matchDataStrings.append("`{:25} {:25} | {:25} |`".format("                       ", rune4Name, rune5Name))
		matchDataStrings.append("`---------------------------------------------------------------------------------------------------------------------------------------`")
		i += 1

	return matchDataStrings

#Returns the name of the Champion corresponding to the given ID
def getChampName(id):
    champData = requests.get('http://ddragon.leagueoflegends.com/cdn/10.19.1/data/en_US/champion.json').json()
    for key in champData['data']:
        if id == int(champData['data'][key]['key']):
            return champData['data'][key]['id']
