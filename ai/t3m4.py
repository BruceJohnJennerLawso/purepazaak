## t3m4.py #####################################################################
## doot doot muthafuckas #######################################################
################################################################################


def aiName():
	return "t3m4"

def foo():
	return "doot doot dwooooo"


def otherPlayer(playerOrder):
	if(playerOrder == "player1"):
		return "player2"
	elif(playerOrder == "player2"):
		return "player1"

def aiTurnCall(firstDecisionPass, playerOrder, thisPazaakHand, thisPlayerScore, otherPlayerScore):
	if(thisPazaakHand.playerState[otherPlayer(playerOrder)] == "stand"):
		if(thisPlayerScore <= 20):
			if(thisPlayerScore > otherPlayerScore):
				return "stand"
	if(thisPlayerScore >= 18):
		diff = thisPlayerScore - otherPlayerScore
		if((diff < 6)and(otherPlayerScore != 20)):
			return "stand"
	return "end"
