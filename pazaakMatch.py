## pazaakMatch.py ##############################################################
## best of five pazaak hands, winner take all ##################################
################################################################################
from pazaakHand import *


class pazaakMatch(object):
	def __init__(self, player1, player2):
		self.players = {"player1": player1.playerName, "player2": player2.playerName}

		self.player1 = player1
		self.player2 = player2
		
		self.handsWon = {self.players["player1"]: 0, self.players["player2"]: 0, "tied": 0}
		
		
	def playMatch(self):
		handNumber = 1
		while(True):

			
			currentHand = pazaakHand(self.player1, self.player2)
			## this is close, just needs to handle ending conditions
			
			drawNumber = 1
			while(True):

				
				result = currentHand.playHand(handNumber, drawNumber, self.handsWon)
				print "\nlast round result: ", result, "\n"
				playerResults = [result[player] for player in result]
				if("tied" in playerResults):
					## keep going...
					drawNumber +=1
					playersDict = currentHand.getPlayersDict()
					
					self.player1 = playersDict[currentHand.playersByName["player1"]]
					self.player2 = playersDict[currentHand.playersByName["player2"]]	
					break
				elif("lost" in playerResults):
					playersDict = currentHand.getPlayersDict()
					self.player1 = playersDict[currentHand.playersByName["player1"]]
					self.player2 = playersDict[currentHand.playersByName["player2"]]
					break
				drawNumber +=1

				
			currentHand.printHandState(handNumber, drawNumber, self.handsWon)
			print result
			
			if(result[self.players["player1"]] == "tied"):
				self.handsWon["tied"] += 1
			elif(result[self.players["player1"]] == "won"):
				self.handsWon[self.players["player1"]] += 1
				handNumber += 1
			elif(result[self.players["player1"]] == "lost"):
				self.handsWon[self.players["player2"]] += 1	
				handNumber += 1
				
			for player in [self.players["player1"], self.players["player2"]]:
				if(self.handsWon[player] == 3):
					return self.handsWon



