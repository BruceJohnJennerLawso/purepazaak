## pazaakSet.py ################################################################
## single round of pazaak, to win, tie, or lose ################################
################################################################################
from player import *

import random
import re

def generateStandardMainDeck():
	outputDeck = []
	for i in range(1, 11):
		for j in range(4):
			outputDeck += [dealtCardPlus(i)]
	return outputDeck

def drawCard(mainDeck):
	random.shuffle(mainDeck)
	return mainDeck.pop()


if(__name__ == "__main__"):
	standardDeck = generateStandardMainDeck()
	
	
	drawnCard = drawCard(standardDeck)
	standardDeck.sort(key=lambda x: x.getCardScore, reverse=False)
	print drawnCard, standardDeck


class pazaakHand(object):
	def __init__(self, player1, player2):
		self.cards = {}
		self.cards["player1"] = []
		self.cards["player2"] = []
		
		self.playersByName = {"player1": player1.playerName, "player2": player2.playerName}
		self.playerState = {"player1": "live", "player2": "live"}
		
		
		self.players = {self.playersByName["player1"]: player1, self.playersByName["player2"]: player2}
		
		self.mainDeck = generateStandardMainDeck()
		##self.player1 = player1
		##self.player2 = player2
		
		
	def getPlayersDict(self):
		return self.players	
		
	def printHandState(self, handNumber, handRound, handsWon):
		print "%i round of hand %i " % (handRound, handNumber), handsWon
		print "%s" % self.playersByName["player1"], self.cards["player1"], playedCardsValue(self.cards["player1"])
		print "%s" % self.playersByName["player2"], self.cards["player2"], playedCardsValue(self.cards["player2"])
		print "\n"	
		
		
	def player1Draw(self):	
		if(self.playerState["player1"] == "live"):
			self.cards["player1"].append(drawCard(self.mainDeck))
	
	
	def player1StateCheck(self, player1Score):
		if(player1Score > 20):
			self.playerState["player1"] = "busted"	
		elif(player1Score == 20):
			self.playerState["player1"] = "stand"
	## broken broken broken, needs to not rely on return call to pass the result out

	def player2Draw(self):	
		if(self.playerState["player2"] == "live"):
			self.cards["player2"].append(drawCard(self.mainDeck))

	def player2StateCheck(self, player2Score):
		
		if(player2Score > 20):
			self.playerState["player2"] = "busted"
			return {self.playersByName["player1"]: "won", self.playersByName["player2"]: "lost"}	
		elif(player2Score == 20):
			self.playerState["player2"] = "stand"
	
	def playHand(self, handNumber, handRound, handsWon):

		
		if(self.playerState["player1"] == "live"):
			self.player1Draw()			
			
			
		player1Score = playedCardsValue(self.cards["player1"])
		player2Score = playedCardsValue(self.cards["player2"])	
		## calculate both players scores so player1 ai can make decisions based
		## on what the scores are
		
		## player 1 ai goes somewhere in here

		##print self.player1.aiCall()


		self.printHandState(handNumber, handRound, handsWon)

		def convertPlayerResponseToCard(playerResponse):
			if(bool(re.match(r"playPlus[0-9]", playerResponse))):
				cardValueToPlay = int(playerResponse[8:])
				return ("plus", cardValueToPlay)
			elif(bool(re.match(r"playMinus[0-9]", playerResponse))):
				cardValueToPlay = int(playerResponse[9:])
				return ("minus", cardValueToPlay)
			elif(bool(re.match(r"playDouble", playerResponse))):
				return ("double", 0)
			elif(bool(re.match(r"play3&6", playerResponse))):
				return ("threeAndSix", 0)
			elif(bool(re.match(r"play2&4", playerResponse))):
				return ("twoAndFour", 0)
			elif(bool(re.match(r"playPlusMinus[0-9]", playerResponse))):
				
				valueAndSign = playerResponse[13:]
				## now need to pull this apart to get the 
				
				print repr(valueAndSign)
				if("minus" in valueAndSign):
					##aaaaa
					value = int(valueAndSign[:-5])
					switch = "minus"
				elif("plus" in valueAndSign):
					value = int(valueAndSign[:-4])
					switch = "plus"
				else: 
					return None
				
				return ("plusMinus", value, switch)
				
			else:
				return None
			
			
			
			

		if(self.playerState["player1"] == "live"):
			playerOrder = "player1"
			player1Decision = self.players[self.playersByName["player1"]].aiCall(True, playerOrder, self, player1Score, player2Score)
			print "%s decision: " % self.playersByName["player1"], player1Decision, "\n"
			if(player1Decision == "stand"):
				self.playerState["player1"] = "stand"
			else:
				cardResponse = convertPlayerResponseToCard(player1Decision)
				if(cardResponse != None):
					playedCard = self.players[self.playersByName["player1"]].playCardByDescription(*cardResponse)
					## note unpacking of arguments
					if(playedCard != None):
						self.cards["player1"].append(playedCard)
						
						player1FollowupDecision = self.players[self.playersByName["player1"]].aiCall(False, playerOrder, self, player1Score, player2Score)
						if(player1FollowupDecision == "stand"):
							self.playerState["player1"] = "stand"
			

		
		
		## this section is p1 decision making, playing cards, and stand/end turn
		## decision
					
		player1Score = playedCardsValue(self.cards["player1"])		
		self.player1StateCheck(player1Score)
		print self.playerState["player1"]
		if(self.playerState["player1"] == "busted"):
			return {self.playersByName["player2"]: "won", self.playersByName["player1"]: "lost"}


		if(self.playerState["player2"] == "live"):
			self.player2Draw()
			
		player2Score = playedCardsValue(self.cards["player2"])
			
			

		## player 2 ai goes here

		if(self.playerState["player2"] == "live"):


			playerOrder = "player2"
			player2Decision = self.players[self.playersByName["player2"]].aiCall(True, playerOrder, self, player2Score, player1Score)

			print "%s decision: " % self.playersByName["player2"], player2Decision
			if(player2Decision == "stand"):
				self.playerState["player2"] = "stand"
			else:
				cardResponse = convertPlayerResponseToCard(player2Decision)
				if(cardResponse != None):
					playedCard = self.players[self.playersByName["player2"]].playCardByDescription(*cardResponse)
					## note unpacking of arguments
					if(playedCard != None):
						self.cards["player2"].append(playedCard)
						
						player2FollowupDecision = self.players[self.playersByName["player2"]].aiCall(False, playerOrder, self, player2Score, player1Score)
						if(player2FollowupDecision == "stand"):
							self.playerState["player2"] = "stand"					
				
		
		
		player2Score = playedCardsValue(self.cards["player2"])
		self.player2StateCheck(player2Score)

		if(self.playerState["player2"] == "busted"):
			return {self.playersByName["player1"]: "won", self.playersByName["player2"]: "lost"}
				
				
				
		playerStates = [self.playerState["player1"], self.playerState["player2"]]
			
		if(playerStates.count("stand") == 2):
			## both players stood, lets see who had the higher score
			if(player1Score == player2Score):
				player1Tiebreak = playedCardsHasTiebreak(self.cards["player1"])
				player2Tiebreak = playedCardsHasTiebreak(self.cards["player1"])				
				
				
				## need something in here that distinguishes if the player has
				## been live this turn or stood last turn
				
				## ie a tiebreaker freshness meter
				if((not player1Tiebreak)and(not player2Tiebreak)):
					return {self.playersByName["player1"]: "tied", self.playersByName["player2"]: "tied"}
				elif((player1Tiebreak == True) and (player2Tiebreak == False)):
					return {self.playersByName["player1"]: "won", self.playersByName["player2"]: "lost"}					
				elif((player1Tiebreak == False) and (player2Tiebreak == True)):
					return {self.playersByName["player1"]: "lost", self.playersByName["player2"]: "won"}
				else:
					## both players somehow played a tiebreak
					## Ive literally never seen this happen in real pazaak, so
					## Im just going to make up the rule here			
					return {self.playersByName["player1"]: "tied", self.playersByName["player2"]: "tied"}
			elif(player1Score > player2Score):
				return {self.playersByName["player1"]: "won", self.playersByName["player2"]: "lost"}
			elif(player2Score > player1Score):
				return {self.playersByName["player2"]: "won", self.playersByName["player1"]: "lost"}		
		elif(playerStates.count("live") == 2):
			return {self.playersByName["player2"]: "live", self.playersByName["player1"]: "live"}
		else:
			return {self.playersByName["player1"]: self.playerState["player1"], self.playersByName["player2"]: self.playerState["player2"]}
		

