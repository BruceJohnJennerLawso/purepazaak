## card.py #####################################################################
## pazaak card objects #########################################################
################################################################################

class pazaakCard(object):
	
	def __eq__(self, other):
		if(self.cardType == other.cardType):
			if(self.cardValue == other.cardValue):
				return True
		return False
	
	def getCardScore(self):
		outputCardValue = self.cardValue
		if(self.doubled):
			outputCardValue = 2*outputCardValue
		elif(self.negated):
			outputCardValue = -outputCardValue	
		return outputCardValue	

	def flipSign(self):
		if(self.negated):
			self.negated = False
		else:
			self.negated = True


class dealtCardPlus(pazaakCard):
	
	def __init__(self, cardValue):
		self.cardValue = cardValue
		self.negated = False
		self.doubled = False
		self.cardType = "additiveDealt"
	
	def __repr__(self):
		if(self.negated):
			prefix = "(-)"
		else:
			prefix = ""
		
		return "%sd%i" % (prefix, self.cardValue)
		
	def applyEffects(self, previousCards):
		## just... nothing because numeric cards have no side effects on other
		## cards
		pass
		
class handCardPlus(pazaakCard):
	
	def __init__(self, cardValue):
		self.cardValue = cardValue
		self.negated = False
		self.doubled = False

		self.cardType = "additiveHand"

	def __repr__(self):
		return "h%i" % self.cardValue


	def applyEffects(self, previousCards):
		## just... nothing because numeric cards have no side effects on other
		## cards
		pass

		
class handCardMinus(pazaakCard):
	
	def __init__(self, cardValue):
		if(cardValue < 0):
			self.cardValue = cardValue
		else:
			self.cardValue = -cardValue
			## if the value passed is positive, store it as a negative anyways
			##
			## assume the value passed was a mistake
		self.negated = False
		self.doubled = False
		self.cardType = "additiveHand"


	def __repr__(self):
		return "h%i" % self.cardValue		

	def applyEffects(self, previousCards):
		## just... nothing because numeric cards have no side effects on other
		## cards
		pass
	
class handCardDouble(pazaakCard):
	def __init__(self):
		self.cardValue = 0	
		self.cardType = "specialHandDouble"
		self.negated = False
		self.doubled = False
	

	def __repr__(self):
		return "dbl"
		
	def applyEffects(self, previousCards):		
		previousCards[-1].doubled = True			



class handCardTwoAndFour(pazaakCard):
	def __init__(self):
		self.cardValue = 0	
		self.cardType = "specialHand2&4"
		self.negated = False
		self.doubled = False	

	def __repr__(self):
		return "2&4"
		
	def applyEffects(self, previousCards):		
		for card in previousCards:
			if(card.cardValue in [2, 4]):
				card.flipSign()
				
class handCardThreeAndSix(pazaakCard):
	def __init__(self):
		self.cardValue = 0	
		self.cardType = "specialHand3&6"
		self.negated = False
		self.doubled = False	

	def __repr__(self):
		return "3&6"
		
	def applyEffects(self, previousCards):		
		for card in previousCards:
			if(card.cardValue in [3, 6]):
				card.flipSign()				

class handCardPlusMinus(pazaakCard):
	def __init__(self, cardValue):
		self.cardValue = cardValue
		self.cardType = "plusMinusHand"
		self.negated = False
		self.doubled = False
		
	def __repr__(self):
		if(self.negated):
			plusPart = "+"
			minusPart = "(-)"
		elif(self.negated == False):
			plusPart = "(+)"
			minusPart = "-"
		return "%s/%s%i" % (plusPart, minusPart, self.cardValue)

	def applyEffects(self, previousCards):
		pass


class handCardPlusMinusTiebreaker(pazaakCard):
	def __init__(self):
		self.cardValue = 1
		self.cardType = "plusMinusTiebreakerHand"
		self.negated = False
		self.doubled = False	

	def __repr__(self):
		if(self.negated):
			plusPart = "+"
			minusPart = "(-)"
		elif(self.negated == False):
			plusPart = "(+)"
			minusPart = "-"
		return "%s/%s1" % (plusPart, minusPart)
		
	def applyEffects(self, previousCards):
		pass

		
		
def playedCardsValue(cardsList):
	score = 0
	
	for card in cardsList:
		cardIndex = cardsList.index(card)
		previousCards = cardsList[0:cardIndex]

		card.applyEffects(previousCards)
	## change any cards that have been changed by double, 3&6, 2&4, 
	
	for card in cardsList:		
		score += card.getCardScore()
	
	##print "\n\n", [{"cardScore": card.getCardScore(),"doubled": card.doubled, "negated": card.negated} for card in cardsList]
	
	return score


def playedCardsHasTiebreak(cardsList):
	if(cardsList[-1].cardType == "plusMinusTieBreakerHand"):
		return True
	else:
		return False	

## the remaining cards to implement are tiebreaker +/- 1, +/- 1 or 2, and the 
## +/- cards 1-6
		
		
if(__name__ == "__main__"):
	playedList = [dealtCardPlus(4), dealtCardPlus(6), handCardThreeAndSix(), dealtCardPlus(5), handCardDouble(), dealtCardPlus(10), dealtCardPlus(1), dealtCardPlus(9), handCardTwoAndFour()]		
	## you know it
	handScore = 0
	
	##for card in playedList:
	##	cardIndex = playedList.index(card)
	##	previousCards = playedList[0:cardIndex]
		##card.applyEffects(previousCards)
		## will need this to apply the side effects of double, 2&4, 3&6 cards
		## later on


	print "Cards: ", playedList, ", score %i" % playedCardsValue(playedList)
