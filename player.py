## player.py ###################################################################
## player at the match level ###################################################
################################################################################

from card import *
import random

class pazaakPlayer(object):
	def __init__(self, playerName, sideDeckCards):
		self.playerName = playerName
		
		self.sideDeck = sideDeckCards

		self.handCards = self.drawHandCards()

	def drawHandCards(self):
		## obviously draws completely wrong right now
		##return self.sideDeck[0:3]
	
		return random.sample(set(self.sideDeck), 4)	

	def getHandCards(self):
		## obviously draws completely wrong right now
		##return self.sideDeck[0:3]
	
		return self.handCards


	def playCardByDescription(self, description, value, switch="plus"):
		if(description == "plus"):
			if(handCardPlus(value) in self.handCards):
				self.handCards.remove(handCardPlus(value))
				return handCardPlus(value)
		elif(description == "minus"):
			if(handCardMinus(value) in self.handCards):
				self.handCards.remove(handCardMinus(value))
				return handCardMinus(value)	
		elif(description == "double"):
			if(handCardDouble() in self.handCards):	
				self.handCards.remove(handCardDouble())
				return handCardDouble()
		elif(description == "threeAndSix"):
			if(handCardThreeAndSix() in self.handCards):	
				self.handCards.remove(handCardThreeAndSix())
				return handCardThreeAndSix()		
		elif(description == "twoAndFour"):
			if(handCardTwoAndFour() in self.handCards):	
				self.handCards.remove(handCardTwoAndFour())
				return handCardTwoAndFour()					
		elif(description == "plusMinus"):
			if(handCardPlusMinus(value) in self.handCards):	
				self.handCards.remove(handCardPlusMinus(value))
				
				handCardToReturn = handCardPlusMinus(value)
				if(switch == "minus"):
					handCardToReturn.flipSign()
				
				return handCardToReturn				
						
	def runAiCall():
		return self.aiCall()


class aiPazaakPlayer(pazaakPlayer):
	def __init__(self, playerName, sideDeckCards, aiModule):
		super(aiPazaakPlayer, self).__init__(playerName, sideDeckCards)
		self.aiCall = aiModule.aiTurnCall

class humanPazaakPlayer(pazaakPlayer):
	def __init__(self, playerName, sideDeckCards, turnCall):
		super(humanPazaakPlayer, self).__init__(playerName, sideDeckCards)
		self.aiCall = turnCall
