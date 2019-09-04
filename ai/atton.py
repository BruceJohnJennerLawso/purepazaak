## atton.py ####################################################################
## slippery mf #################################################################
################################################################################
from card import *

def aiName():
	return "attonRand"


def foo():
	return "Ronto Scrag"


def otherPlayer(playerOrder):
	if(playerOrder == "player1"):
		return "player2"
	elif(playerOrder == "player2"):
		return "player1"

def aiTurnCall(firstDecisionPass, playerOrder, thisPazaakHand, thisPlayerScore, otherPlayerScore):
	
	if(firstDecisionPass):
		toTwenty = 20-thisPlayerScore
		print "Hand cards: ", thisPazaakHand.players[thisPazaakHand.playersByName[playerOrder]].getHandCards()
		print "toTwenty: ", toTwenty
	
		handCardToTwenty = (handCardPlus(toTwenty) in thisPazaakHand.players[thisPazaakHand.playersByName[playerOrder]].getHandCards())
	
		print "toTwenty in Hand: ", handCardToTwenty
	
		if(handCardToTwenty):
			return "playPlus%i" % toTwenty
	if(thisPazaakHand.playerState[otherPlayer(playerOrder)] == "stand"):
		if(thisPlayerScore <= 20):
			if(thisPlayerScore > otherPlayerScore):
				return "stand"
				## easy mode win
				
				
	##thisPazaakHand.players[thisPazaakHand.players[thisPazaakHand.playersByName[otherPlayer(playerOrder]].
	## how to reference the other player object in this scope if I want to
	
	
	if(thisPlayerScore >= 16):
		diff = thisPlayerScore - otherPlayerScore
		if((diff <= 1)and(otherPlayerScore != 20)):
			return "stand"


	return "end"
