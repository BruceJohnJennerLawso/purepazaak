## app.py ######################################################################
## command line pazaak, republic senate rules ##################################
################################################################################
from pazaakMatch import *
from sys import argv
import sys

import importlib

import random

def getStandardSideDeck():
	standardSideDeck = [handCardPlus(1), handCardPlus(1), handCardPlus(2), handCardPlus(2), handCardPlus(3), handCardPlus(3), handCardPlus(4), handCardPlus(4), handCardPlus(5), handCardPlus(5), handCardPlus(6), handCardPlus(6)]	
	return standardSideDeck


def getBetterSideDeck():
	standardSideDeck = [handCardPlusMinus(6), handCardPlusMinus(6), handCardThreeAndSix(), handCardMinus(2), handCardTwoAndFour(), handCardMinus(3), handCardPlus(4), handCardMinus(4), handCardPlus(5), handCardMinus(5), handCardDouble(), handCardMinus(6)]	
	return standardSideDeck


def getNormalizedDict(someDict):
	totalCount = 0
	
	for someKey in someDict:
		totalCount += someDict[someKey]
		
	newDict = {}
	for someKey in someDict:
		newDict[someKey] = someDict[someKey]/float(totalCount)
	return newDict
def runDemoGame():
	
	


	moduleNames = ['t3m4', 'atton']
	modules = map(__import__, moduleNames)
	aisDict = {}
	
	for mod in modules:
		aisDict[mod.aiName()] = mod
		
	
	overallHandWinCount = {'T3M4': 0, 'tied': 0, 'Atton': 0}
	overallMatchWinCount = {'T3M4': 0, 'Atton': 0}
	
	
	for i in range(500):
		houseRules = pazaakMatch(aiPazaakPlayer("Atton", getStandardSideDeck(), aisDict["attonRand"]), aiPazaakPlayer("T3M4", getStandardSideDeck(), aisDict["t3m4"]))

		## fifteen minutes into ronto scrag and chill and he gives you this look
		result = houseRules.playMatch()
		print "Match Result: ", repr(result)
		for players in overallHandWinCount:
			overallHandWinCount[players] += result[players]
			if((result[players] == 3)and(players != "tied")):
				overallMatchWinCount[players] += 1


	attonHandWinRatio = overallHandWinCount['Atton']/float(overallHandWinCount['T3M4'])
	print "Overall Hand Win Results: ", repr(overallHandWinCount), "\n(", getNormalizedDict(overallHandWinCount), "), %f\n\n" % attonHandWinRatio
	attonMatchWinRatio = overallMatchWinCount['Atton']/float(overallMatchWinCount['T3M4'])
	print "Overall Match Win Results: ", repr(overallMatchWinCount), "\n(", getNormalizedDict(overallMatchWinCount), "), %f" % attonMatchWinRatio
	
	
	
	
def requestPlayerInput(firstDecisionPass, playerOrder, thisPazaakHand, player1Score, player2Score):
	while(True):
		playerPrompt = raw_input(">")
		if(playerPrompt in ["stand", "end"]):
			return playerPrompt
		elif(playerPrompt in ["showHand"]):
			print thisPazaakHand.players[thisPazaakHand.playersByName[playerOrder]].getHandCards()
		elif((bool(re.match(r"playPlus[0-9]", playerPrompt))) or (bool(re.match(r"playMinus[0-9]", playerPrompt))) or (bool(re.match(r"playDouble", playerPrompt))) or (bool(re.match(r"play2&4", playerPrompt))) or (bool(re.match(r"play3&6", playerPrompt))) or (bool(re.match(r"playPlusMinus[0-9]", playerPrompt)))):
			if(firstDecisionPass):
				return playerPrompt
			else:
				print "Unable to play multiple cards in one turn"
		else:
			print "invalid command '%s'" % playerPrompt


def runSinglePlayerGame():
	
	moduleNames = ['t3m4', 'atton']
	modules = map(__import__, moduleNames)
	
	aisDict = {}
	
	for mod in modules:
		aisDict[mod.aiName()] = mod
	## ie {"t3m4": moduleObject, "attonRand": moduleObject}
	
	standardSideDeck = [handCardPlus(1), handCardPlus(1), handCardPlus(2), handCardPlus(2), handCardPlus(3), handCardPlus(3), handCardPlus(4), handCardPlus(4), handCardPlus(5), handCardPlus(6), handCardPlus(6)]
	
	print "available ai opponents are: ", [aisDict[module].aiName() for module in aisDict], "\n"
	
	opponentId = ""
	
	while(True):
		selectedOpponent = raw_input("please select opponent: ")
		if(selectedOpponent in  [aisDict[module].aiName() for module in aisDict]):
			opponentId = selectedOpponent
			break
		elif(selectedOpponent in ["random"]):
			opponentId = random.choice([aisDict[module].aiName() for module in aisDict])
			break
	
	houseRules = pazaakMatch(humanPazaakPlayer("Revan", getBetterSideDeck(), requestPlayerInput), aiPazaakPlayer(aisDict[opponentId].aiName(), getStandardSideDeck(), aisDict[opponentId]))

	## fifteen minutes into ronto scrag and chill and he gives you this look
	result = houseRules.playMatch()
	print result
	


if(__name__ == "__main__"):
	sys.path.insert(1, './ai')
	## make it possible to import custom ai modules at runtime
	
	try:
		mode = argv[1]
	except IndexError:
		mode = None
	
	if(mode in [None, "test"]):
		runDemoGame()
	elif(mode in ["singlePlayer"]):
		runSinglePlayerGame()


