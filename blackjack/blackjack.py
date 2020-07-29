'''
BLACKJACK - projeto 2
'''

# REQUISITOS

# OK - Um jogador Vs Dealer automatizado
# OK - Player pode esperar ou pedir mais cartas
# OK - Player pode escolher o valor de apostas
# OK - Acompanhar o dinheiro total dos jogadores
# OK - Alertar o jogador de vitórias e perdas

# OK - Usar POO 

# OK - Tentar vários jogadores
# OK - Tentar implementar Double-down



# REGRAS


# between one or more players and a dealer
# each player in turn competes against the dealer
# Players do not compete against each other
# 
# 
# OK - At beginning of each round, player places their bet in the "betting box" 
# 
# OK - Players are each dealt two cards
# OK - the dealer is also dealt two cards
# OK - one up (exposed) and one down (hidden). He knows what it is

# 
# OK - The value of cards 2-10 is their pip value. Face cards (Jack, Queen, and King) are all worth ten. Aces can be worth one or eleven.
# Ok - A hand with an ace valued as 11 is called "soft", meaning that the hand will not bust by taking an additional card. The value of the ace will become one to prevent the hand from exceeding 21. Otherwise, the hand is called "hard".
#  
# OK - draw additional cards to improve their hands
#  
# OK (make a player status instead to check for blackjacks)
# OK - hit: draw, may do as many as wants until not above hard 20 (ace as 1) (check Bust)
# OK - stand: end turn
# OK - double-down: double bet, take one card and finish (check Bust)
#  - split: CAN ONLY SPLIT ONCE, BOOM, DONE if the first two cards have same value, separate to make two hands, bet equal to the first, an ace and ten value card after a split are counted as a non-blackjack, split aces only receive one more card
# OK - surrender (only available as first decision): the house takes half the player's bet
#  
# OK Once all the players have completed their hands, it is the dealer's turn
# OK reveals the hidden
# OK dealer hand will not be completed if all players have either busted (over 21) or received blackjacks(ace + 10-valued-card)
#  
#  
# OK The dealer only hits or stand.
# OK hit until the cards total up to 17 points or higher
#  
# OK each player's hand (that didn't bust) is compared with the dealer
# OK The better hand is where the sum is closer to 21 without exceeding 21
#  
# OK If player busts, instant loses
# OK If player blackjacks and the dealer doesn't, player wins and usually receives bonus
# OK If dealer busts and player doesn't, player wins
# OK If player has better hand than dealer, player wins
# OK If there is a "push" (both with same points), no one wins, bets return
# 
# OK Wins are paid out at 1:1
# OK player blackjacks are paid at 3:2 (receives three dollars for every two bet)
# 













### IMPORTS ###

import os
import time
import random
import pickle







### STATEMENTS ###

sleep = lambda sec: time.sleep(sec)

clear = lambda: os.system('clear')


cardsValues = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k')
cardsSuits = ('spades', 'hearts', 'clubs',  'diamonds')

dealerName = ''
bettingBox = {}




### FUNCTIONS ###


def game():
	'''
	Coordenates the game.
	'''	
	gameOn = True
	
	(dealer, players) = whoPlays()
	
	if players == []:
		gameOn = False
		
		
	
	while gameOn:
		
		playRound(dealer, players)
		
		print('\t\t  ')
		print('\t\t  +-------------------------------------+')
		print('\t\t  |   Continue playing?                 |')
		print('\t\t  |                                     |')
		print('\t\t  |    [Y]es      [N]o                  |')
		print('\t\t  +-------------------------------------+')
		print('\t\t    => Input [Y/N]: ', end='')
		yesNo = input('').upper()
		
		if yesNo == 'N':
			gameOn = False
		
	
	clear()
	print('\t\t  ')
	print('\t\t  +-------------------------------------+')
	print("\t\t  | Ph'nglui mglw'nafh Cthulhu R'lyeh   |")
	print("\t\t  | wgah'nagl fhtagn.                   |")
	print('\t\t  +-------------------------------------+')
	print('\t\t  ')
	print("")





def whoPlays():
	'''
	Return the dealer and a list of Players for the currennt Game.
	'''
	global dealerName
	
	dealer = Player('Joãozinho do Veropa (The Dealer)', 0)
	dealerName = dealer.name
	players = []
	
	notDone = True
	clear()
	
	while notDone:
		
		print('')
		print('\t\t\t//===================================\\\\')
		print('\t\t\t||                                   ||')
		print('\t\t\t||           Welcome  to             ||')
		print('\t\t\t||                                   ||')
		print('\t\t\t||            BLACKJACK              ||')
		print('\t\t\t||                                   ||')
		print('\t\t\t\\\\===================================//')
		print('\t\t\t')
		if players != []:
			print('\t\t\t')
			print('\t\t\t+-------------------------------------+')
			print('\t\t\t|    Current Players:                 |')
			for p in players:
				print('\t\t\t|    - %-30s |' %(p.name if len(p.name) <= 30 else p.name[:30]))
			print('\t\t\t|                                     |')
			print('\t\t\t+-------------------------------------+')	
		print('\t\t\t')
		print('\t\t\t+-------------------------------------+')
		print('\t\t\t|    Who is Playing?                  |')
		print('\t\t\t|                                     |')
		print('\t\t\t|   [N]ew Player   [L]oad Player      |')
		if players == []:
			print('\t\t\t|                  [E]xit             |')
			print('\t\t\t+-------------------------------------+')
			print('\t\t\t  => Input [N/L/E]: ', end='')
		else:
			print('\t\t\t|   [P]lay         [E]xit             |')
			print('\t\t\t+-------------------------------------+')
			print('\t\t\t  => Input [N/L/P/E]: ', end='')
		ans = input('').upper()
		
		
		if ans == 'N':	# NEW
			clear()
			
			notNew = True
			
			# List of files
			ls = [fname[:-4]  for r, d, files in os.walk("/home/teles/Coding/python/Projects/blackjack/blackjack_profiles/") for fname in files]
			
			# List of all Saved Player's Names
			if ls != []:
				listSavedPlayersName = [loadPlayer(fname).name for fname in ls]
			else:
				listSavedPlayersName = []
			
			while notNew:
				
				print('\t\t\t')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t|    New Player!                      |')
				print('\t\t\t|                                     |')
				print('\t\t\t|   Players start with $ 100.00       |')
				print('\t\t\t|                                     |')
				print('\t\t\t|    What is your name ?              |')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t  => Type: ', end='')
				name = input('')
				
				if name in listSavedPlayersName:
					notLoaded = False
					print('\t\t\t')
					print('\t\t\t+-------------------------------------+')
					print('\t\t\t|    Sorry!                           |')
					print('\t\t\t|    This name is taken.              |')
					print('\t\t\t|    Try a different name.            |')
					print('\t\t\t|                                     |')
					print('\t\t\t+-------------------------------------+')
					print('\t\t\t  => Press Enter to continue: ', end='')
					x = input('')
					clear()
					
					continue
				
				print('\t\t\t')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t|   " %-30s   |' %(name+' "'))
				print('\t\t\t|                                     |')
				print('\t\t\t|   Is that right?                    |')
				print('\t\t\t|                                     |')
				print('\t\t\t|    [Y]es      [N]o      [C]ancel    |')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t  => Input [Y/N/C]: ', end='')
				yesNo = input('').upper()
				
				if yesNo == 'Y':
					dude = Player(name)
					
					newPlayer(dude)
					players.append(dude)
					
					clear()
					notNew = False
					
				elif yesNo == 'C':
					clear()
					notNew = False
					
				else:
					clear()
			
		elif ans == 'L':	# LOAD
			clear()
			
			notLoaded = True
			
			# List of files
			ls = [fname[:-4]  for r, d, files in os.walk("/home/teles/Coding/python/Projects/blackjack/blackjack_profiles/") for fname in files]
			
			# List of Saved Players (if not already loaded)
			if ls != []:
				listSavedPlayers = [loadPlayer(fname) for fname in ls if loadPlayer(fname).filename not in [p.filename for p in players]]
			else:
				notLoaded = False
				print('\t\t\t')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t|    Sorry!                           |')
				print('\t\t\t|    There are no players saved.      |')
				print('\t\t\t|    Try creating a New Player!       |')
				print('\t\t\t|                                     |')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t  => Press Enter to continue: ', end='')
				x = input('')
				clear()
				
			
			while notLoaded:
				
				print('\t\t\t')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t|    List of Saved Players:           |')
				print('\t\t\t|                                     |')
				
				count = 1
				for p in listSavedPlayers:
					print('\t\t\t| %2d. %-24s $ %4d |' %(count, (p.name if len(p.name) <= 24 else p.name[:24]), p.money))
					count += 1
					
				print('\t\t\t|                                     |')
				print('\t\t\t|    Which one ?                      |')
				print('\t\t\t|                         [C]ancel    |')
				print('\t\t\t+-------------------------------------+')
				print('\t\t\t  => Type (number): ', end='')
				num = input('')
				
				if num.upper() == 'C':
					clear()
					notLoaded = False
								
				try:
					num = int(num)
					num -= 1
					if num not in range(len(ls)):
						clear()
						continue
					
				except:
					clear()
					continue
					
				else:
					players.append(listSavedPlayers[num])
					
					clear()
					notLoaded = False
			
		elif ans == 'P':	# PLAY
			
			if players == []:
				clear()
			else:
				clear()
				notDone = False
			
		elif ans == 'E':	# EXIT
			clear()
			players = []
			notDone = False
			
		else:
			clear()
	
	return (dealer, players)





def newPlayer(player):
	
	with open('/home/teles/Coding/python/Projects/blackjack/blackjack_profiles/%s.pkl' %player.filename,'xb') as output:
		pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)



def loadPlayer(filename):
	
	with open('/home/teles/Coding/python/Projects/blackjack/blackjack_profiles/%s.pkl' %filename,'rb') as input:
		return pickle.load(input)



def savePlayer(player):
	
	with open('/home/teles/Coding/python/Projects/blackjack/blackjack_profiles/%s.pkl' %player.filename,'wb') as output:
		pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
























def playRound(dealer, players):
	'''
	Coordenates the round.
	'''
	global bettingBox
	
	bettingBox = {}
	newDekc = Deck()
	
	
	
	# Round Beggin, Players pace bets
	haventBet = []
	
	for p in players:
		
		p.clearHand()
		
		bettingBox[p.name] = 0
		bet = placeBet(dealer, p)
		
		if bet != 0:
			bettingBox[p.name] = bet
		
		else:
			haventBet.append(p) #LATEEEEEEEEEEEEEEEERRRRRR
	
	for p in haventBet:
		players.remove(p)
	
	
	# Each player is dealt 2 Cards
	dealCard(newDekc, dealer, 2)
	
	for p in players:
		
		dealCard(newDekc, p, 2)
		
		if p.checkBJ():
			displayGame(dealer, p)
			print('\t\t     BLACKJACK !!')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			clear()
			
			turnOn = False
		
		else:
			turnOn = displayOptions(dealer, p, newDekc, firstTurn=True)
		
		
		
		while turnOn:
			
			turnOn = displayOptions(dealer, p, newDekc)
			
	
	# After all the players have ended their turn, is time for the dealer
	dealerPlaying = True
	
	
	if all( bet == 0 for bet in list(bettingBox.values()) ):
		
		displayGame(dealer, p)
		print("\t\t     No one has bet. The round is over.")
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		clear()
		
		dealerPlaying = False
	
	elif all( [p.allBusted() for p in players] ):
		
		displayGame(dealer, p, roundOver=True)
		print("\t\t     All players busted !! The round is over.")
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		clear()
		
		dealerPlaying = False
	
	elif all( [p.allBJ() for p in players] ):
		
		displayGame(dealer, p, roundOver=True)
		print("\t\t     All players have Blacjacks !! The round is over.")
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		clear()
		
		dealerPlaying = False
		
	else:
		
		displayGame(dealer, p, roundOver=True)
		print("\t\t     It's the Dealer's turn.")
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		clear()
	
	
	while dealerPlaying:
		
		if dealer.checkBJ():
			
			displayGame(dealer, p, roundOver=True)
			print('\t\t     The dealer has a BLACKJACK !!')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			clear()
			
			dealerPlaying = False
			
		elif dealer.handPoints() < 17:
			
			dealCard(newDekc, dealer)
			displayGame(dealer, p, roundOver=True)
			print('\t\t     The dealer Hits.')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			clear()
			
			if  dealer.handPoints() > 21:
				
				displayGame(dealer, p, roundOver=True)
				print('\t\t     The dealer Busted !!')
				print('\t\t    => Press Enter to continue: ', end='')
				x = input('')
				clear()
				
				dealerPlaying = False
			
		elif 21 >= dealer.handPoints() >= 17:
			
			displayGame(dealer, p, roundOver=True)
			print('\t\t     The dealer Stands.')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			clear()
			
			dealerPlaying = False
			
		else:
			
			displayGame(dealer, p, roundOver=True)
			print('\t\t     The dealer is confused with your attittudes. Send Help.')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			clear()
			
			dealerPlaying = False
		
	
	# After the dealer is done, acerto de contas
	if not all( bet == 0 for bet in list(bettingBox.values()) ):
		for p in players:
			
			if p.multiHand != []:
				
				notResolved = True
				p.splitCounter = len(p.multiHand)
				
				while notResolved:
					
					displayGame(dealer, p, roundOver=True)
					resolveBet(dealer, p)
					notResolved = False
					
					if (p.splitCounter != 0):
						p.switchHand( - p.splitCounter)
						p.splitCounter -= 1
						notResolved = True
				
				
				
			else:
				displayGame(dealer, p, roundOver=True)
				resolveBet(dealer, p)
			
			
			for card in p.clearHand():
				newDekc.addCard( card )
		
	
	for card in dealer.clearHand():
		newDekc.addCard( card )
	
	for p in haventBet:
		players.append(p)
	
	bettingBox = {}




def placeBet(dealer, player):
	'''
	Place a Bet, and returns its value.
	'''
	
	notBet = True
	
	clear()
	displayGame(dealer, player)
	
	
	print('\n\n')
	while notBet:
		
		bet = input("\t\t  Bet value (integer): ")
		
		# Cancel option
		if bet.upper() == 'C':
			notBet = False
			bet = 0
			continue
		
		# Bet has to be a integer and player has to have balance for the bet.
		try:
			bet = int(bet)
			
		except ValueError:
			clear()
			displayGame(dealer, player)
			print("\n\n\t\t  Needs to be a integer! (Type 'C'  to cancel the bet.)")
			
		except:
			clear()
			displayGame(dealer, player)
			print('\n\n\t\t  Other Error!')
			
		else:
			
			if player.hasBalance(bet):
				player.debt(bet)
				notBet = False
				
			else:
				clear()
				displayGame(dealer, player)
				print("\n\n\t\t  You don't have funds for this bet! (Type 'C'  to cancel the bet.)")
	
	return bet













def dealCard(deck, player, num=1):
	'''
	Deals a number of cards, from a deck ta a player's hand.
	'''
	
	for n in range(num):
		player.addToHand(deck.draw())
		







def displayGame(dealer, player, roundOver=False):
	'''
	Display multiple cards.
	
	- Dealers hand
	- Current player's :
		- name (turn)
		- hand
		- bet
		- Funds
	'''
	global bettingBox
	
	clear()
	
	print('\t\t\t')
	print('\t\t\t         DEALER:')
	print('\t\t\t          --x--')
	
	displayCards(dealer,roundOver)
	if roundOver:
		print('\t\t\t      | Points: %2d |' % dealer.handPoints())
	else:
		print('\t\t\t      | Points: ?? |')
	print("\t\t\t      '------------'")
	print('\t\t\t')
	print('\t\t\t        %s' % player.name)
	print('\t\t\t         .--x--.')
	
	displayCards(player,roundOver)
	
	if player.multiHand == [] :
		print( '\t\t\t                    \t\t   .  .--x--.')
		print('\t\t\t      | Points: %2d |\t\t   |  Bet: $ %d' % (player.handPoints(),bettingBox[player.name]))
		print( "\t\t\t      '------------'\t\t   x   --x--")
		print( '\t\t\t                    \t\t   |  Funds: $ %d' % player.money)
		print( "\t\t\t                    \t\t   '  '--x--'")
		
	else:
		possibleHands = [ '', '', '']
		actHands = player.allHandStr()
		
		for ind in range(len(actHands)):
			possibleHands[ind] += actHands[ind]
		
		print( '\t\t\t                    \t\t   .  .--x--.               .  .--x--.')
		print('\t\t\t      | Points: %2d |\t\t   |  Bet: $ %-5d          |  %s' % (player.handPoints(),bettingBox[player.name], possibleHands[0]))
		print( "\t\t\t      '------------'\t\t   x   --x--                x  %s" % possibleHands[1])
		print( '\t\t\t                    \t\t   |  Funds: $ %-5d        |  %s' % (player.money, possibleHands[2]))
		print( "\t\t\t                    \t\t   '  '--x--'               '  '--x--")
	
	




def displayCards(player, roundOver=False):
	'''
	Display multiple cards.
	'''
	global dealerName
	
	def cardStrings(CardId, card=None):
		'''
		Return a list of strings that when printed one under the other display a card.
		Uses Card-Id. If Card-Id '-' is passed, prints back of a card.
		'''
		
		
		if CardId == '-':
			l1 = '.-----------.'
			l2 = '| x-------x |'
			l3 = '| |       | |'
			l4 = '| |       | |'
			l5 = '| |       | |'
			l6 = '| |       | |'
			l7 = '| |       | |'
			l8 = '| x-------x |'
			l9 = "'-----------'"
			
			
		else:
			dictValues = {'a':'A', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'10', 'j':'J', 'q':'Q', 'k':'K'}
			uSuit = {'s':'♠', 'h':'♡', 'c':'♣',  'd':'♢'}
			
			v = dictValues[CardId[0]]
			s = uSuit[CardId[1]]
			
			l1 = '.-----------.'
			l2 = '|%2s         |' %v
			l3 = '|   %s %s %s   |' %((s if v in ['4','5','6','7','8','9','10'] else ' '), (s if v in ['2','3'] else ' '), (s if v in ['4','5','6','7','8','9','10'] else ' '))
			l4 = '|   %s %s %s   |' %((s if v in ['9','10'] else ' '), (s if v in ['7','8','10'] else ' '), (s if v in ['9','10'] else ' '))
			l5 = '|   %s %s %s   |' %((s if v in ['6','7','8'] else ' '), (s if v in ['A','3','5','9'] else ' '), (s if v in ['6','7','8'] else ' '))
			l6 = '|   %s %s %s   |' %((s if v in ['9','10'] else ' '), (s if v in ['8','10'] else ' '), (s if v in ['9','10'] else ' '))
			l7 = '|   %s %s %s   |' %((s if v in ['4','5','6','7','8','9','10'] else ' '), (s if v in ['2','3'] else ' '), (s if v in ['4','5','6','7','8','9','10'] else ' '))
			l8 = '|         %-2s|'%v
			l9 = "'-----------'"
			
		
		if card == None:
			cs = ''
		else:
			cs = str(card)[:-3]
		
		return [l1,l2,l3,l4,l5,l6,l7,l8,l9,cs]
	
	
	
	
	def cardStrAdd(cStr1, cStr2):
		'''
		Adds two lists of Card strings
		'''
		
		for l in range(10):
			cStr1[l] += ('  %15s  ' % cStr2[l])
		
		return cStr1
	
	
	
	cards = [c for c in player.hand]
	cardsDisp = ['','','','','','','','','','']
	
	if cards == []:
		cardsDisp = cardStrAdd(cardsDisp, cardStrings('-'))
		cardsDisp = cardStrAdd(cardsDisp, cardStrings('-'))
		
	else:
		# The dealer only shows one card until the end of the round
		if player.name == dealerName and not roundOver:
			
			cardsDisp = cardStrAdd(cardsDisp, cardStrings(player.hand[0].cardId,player.hand[0]))
			cardsDisp = cardStrAdd(cardsDisp, cardStrings('-'))
			
		else:
			for c in cards:
				cardsDisp = cardStrAdd(cardsDisp, cardStrings(c.cardId,c))
				
			
	for l in range(10):
		print('\t\t%s' % cardsDisp[l])







def displayOptions(dealer, player, deck, firstTurn=False):
	'''
	Hndles the player options.
	Returns if the turn is still On
	'''
	
	#
	#  - hit: draw, may do as many as wants until not above hard 20 (ace as 1) (check Bust)
	#  - stand: end turn
	#  - double-down: double bet, take one card and finish (check Bust)
	#  - split: if the first two cards have same value, separate to make two hands, bet equal to the first, an ace and ten value card after a split are counted as a non-blackjack, can't double-down, nor surrender
	#  - surrender (only available as first decision): the house takes half the player's bet
	#  
	global bettingBox
	
	turnOn = True
	notOpted = True	
	
	while notOpted:
		
		
		
		displayGame(dealer, player)
		
		print('\t\t  ')
		print('\t\t  +-------------------------------------+')
		print('\t\t  |    Options:                         |')
		print('\t\t  |                                     |')
		if player.multiHand == []:
			print('\t\t  | [H]it     [S]tand     [D]ouble-down |')
		else:
			print('\t\t  | [H]it     [S]tand                   |')
		if firstTurn and player.splittable():
			print('\t\t  |                                     |')
			print('\t\t  | S[p]lit   S[u]rrender               |')
		elif firstTurn and player.multiHand == []:
			print('\t\t  |                                     |')
			print('\t\t  |           S[u]rrender               |')
		elif player.splittable():
			print('\t\t  |                                     |')
			print('\t\t  | S[p]lit                             |')
		print('\t\t  +-------------------------------------+')
		
		if firstTurn and player.splittable():
			if player.multiHand == []:
				print('\t\t    => What will you do [H/S/D/p/u]: ', end='')
			else:
				print('\t\t    => What will you do [H/S/p]: ', end='')
		elif firstTurn:
			print('\t\t    => What will you do [H/S/D/u]: ', end='')
		elif player.splittable():
			print('\t\t    => What will you do [H/S/p]: ', end='')
		else:
			if player.multiHand == []:
				print('\t\t    => What will you do [H/S/D]: ', end='')
			else:
				print('\t\t    => What will you do [H/S]: ', end='')
			
		opt = input('').upper()
		clear()
		
		
		if opt == 'H':
			
			dealCard(deck, player)
			
			if player.handPoints() > 21:
				
				displayGame(dealer, player)
				resolveBet(dealer, player)
				
				turnOn = False
			notOpted = False
			
		elif opt == 'S':
			turnOn = False
			notOpted = False
			
		elif opt == 'D' and player.multiHand == []:
			
			bet = bettingBox[player.name]
			
			if player.hasBalance(bet):
				player.debt(bet)
				
			else:
				displayGame(dealer, player)
				print("\t\t  You don't have funds to Double-down.")
				print('\t\t    => Press Enter to continue: ', end='')
				x = input('')
				continue
			
			bettingBox[player.name] *= 2
			dealCard(deck, player)
			displayGame(dealer, player)
			
			if player.handPoints() > 21:
				resolveBet(dealer, player)
				
			else:
				print('\t\t     DOUBLE-DOWN !!')
				print('\t\t    => Press Enter to continue: ', end='')
				x = input('')
			
			
			turnOn = False
			notOpted = False
			
		elif opt == 'P' and player.splittable():
			
			bet = bettingBox[player.name]
			
			if player.hasBalance(bet):
				player.debt(bet)
				
				player.splitHand()
				
				player.switchHand( -1)
				dealCard(deck, player)
				
				player.switchHand( -1)
				dealCard(deck, player)
				
				notOpted = False
				continue
				
			else:
				displayGame(dealer, player)
				print("\t\t  You don't have funds to Split.")
				print('\t\t    => Press Enter to continue: ', end='')
				x = input('')
				continue
			
			
			
			
			
			
			
			
			
		elif opt == 'U' and firstTurn:
			
			player.surrendered = True
			
			displayGame(dealer, player)
			
			print('\t\t     You have SURRENDED from the current round.')
			print('\t\t    => Press Enter to continue: ', end='')
			x = input('')
			
			notOpted = False
			turnOn = False
			
			
		else:
			continue
		
		
		
		if not turnOn and (player.splitCounter != 0):
			player.switchHand( - player.splitCounter)
			player.splitCounter -= 1
			turnOn = True
		
	return turnOn




def resolveBet(dealer, player):
	'''
	Credit or Debt the bet on the Player's balance, according to the result of the game.
	
	Saves the info of the player.
	
	Show Messages of what happend.
	'''
	#
	# If player busts, instant loses
	# If player blackjacks and the dealer doesn't, player wins and usually receives bonus
	# If dealer busts and player doesn't, player wins
	# If player has better hand than dealer, player wins
	# If there is a "push" (both with same points), no one wins, bets return
	# 
	
	global bettingBox
	
	savePlayer(player)
	
	bet = bettingBox[player.name]
	
	if player.surrendered :
		# surrender
		player.credit( bet * ( 0 + .5) )
		
		player.surrendered = False
		
		print('\t\t     You Surrendered !!')
		print('\t\t     You get half of your bet back.')
		print('\t\t     ')
		print('\t\t     Your bet: $ %.2f' % (bet / 2))
		print('\t\t      Reward:  $ 0')
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	elif player.handPoints() > 21:
		# No money for you
	
		print('\t\t     You Busted.')
		print('\t\t     Bet lost !!')
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	elif player.checkBJ() and not dealer.checkBJ() and player.multiHand == []:
		# BJ
		player.credit( bet * (3/2 + 1) )
		
		print('\t\t     You got a BLACKJACK !!')
		print('\t\t     You win a bonus !!')
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t      Reward:  $ %.2f' % (bet * 3/2))
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	elif dealer.handPoints() > 21 and not player.handPoints() > 21:
		# Dealer Busted. You win!
		player.credit( bet * (  1 + 1) )
		
		print('\t\t     The Dealer Busted !!')
		print('\t\t     You win !!')
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t      Reward:  $ %d' % bet)
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
		
	elif player.handPoints() > dealer.handPoints():
		# More points
		player.credit( bet * (  1 + 1) )
		
		print('\t\t     You are closer to 21 than the Dealer !!')
		print('\t\t     You win !!')
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t      Reward:  $ %d' % bet)
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	elif player.handPoints() == dealer.handPoints():
		# Push
		player.credit( bet * (  0 + 1) )
		
		print('\t\t     You and the Dealer have equal points.')
		print("\t\t     It's a Push")
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t      Reward:  $ 0')
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	elif player.handPoints() < dealer.handPoints():
		# Less points
		
		print('\t\t     The Dealer is closer to 21 than you !!')
		print('\t\t     You lost.')
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t    => Press Enter to continue: ', end='')
		x = input('')
		
	else:
		# ???????
		
		print('\t\t     How the Fuck did you get here ?!')
		print("\t\t     It's Something !!")
		print('\t\t     ')
		print('\t\t     Your bet: $ %d' % bet)
		print('\t\t      Reward:  $ who knows')
		print('\t\t    => Press Enter to yeet right the fuck off: ', end='')
		x = input('')
		
		
	
	savePlayer(player)





















### CLASSES ###

class Card:
	'''
	Identify each card on the deck
	'''
	
	# Unicode suits
	uSuit = {'spades':'♠', 'hearts':'♡', 'clubs':'♣',  'diamonds':'♢'}
	
	# Dictionary for Card-Id
	dictValues = {'Ace': 'a', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '0', 'j': 'j', 'q': 'q', 'k': 'k'}
	
	
	def __init__(self,cardValue,cardSuit):
		
		# Card value and point
		self.cardValue = cardValue
		
		if isinstance(cardValue, int):
			self.point = cardValue
			
		elif isinstance(cardValue, str) and cardValue=='Ace':
			self.point = 11
		else:
			self.point = 10
		
		
		# Card suit writen and unicode
		self.cardSuit = cardSuit
		self.suit = self.uSuit[cardSuit]
		
		
		# Card as string format display
		self.cardStr = '%3s of %s(%s)' %(self.cardValue,self.cardSuit,self.suit)
		
		# Card-Id
		self.cardId = '%s%s' %( self.dictValues[str(self.cardValue)] , self.cardSuit[0])
		'''
		Ex)
		as = Ace of spades(♠)
		2h = 2 of hearts(♡)
		0c = 10 of clubs(♣)
		jd = j of diamonds(♢)
		'''
		
		
	def __str__(self):
		return self.cardStr









class Deck:
	'''
	Identify a specific deck of cards
	'''
	
	
	def __init__(self):
		global cardsValues
		global cardsSuits
		
		# Deck is initialized with all possible cards
		self.deckCards = [Card(value, suit) for suit in cardsSuits for value in cardsValues]
		
		# Deck list of Cards-Id's
		self.listCardsId = [card.cardId for card in self.deckCards]
	
	def __str__(self):
		deckStr = ''
		
		global cardsValues
		global cardsSuits
		
		
		for value in cardsValues:
			for suit in cardsSuits:
				
				if Card(value, suit).cardId in self.listCardsId:
					deckStr += '%18s' % (Card(value, suit).cardStr)
					
				else:
					deckStr += '%18s' % '--   '
				
				deckStr += ('\t' if suit != 'diamonds' else '\n')
				
		return deckStr
	
	
	
	def addCard(self, card):
		'''
		Receive card and adds to the deck
		'''
		
		self.deckCards.append(card)
		self.listCardsId.append(card.cardId)
	
	
	
	def removeCard(self, cardId):
		'''
		Use Card-Id to remove a specific Card from the Deck
		'''
		
		if cardId in self.listCardsId:
			
			i = self.listCardsId.index(cardId)
			
			self.deckCards.pop(i)
			self.listCardsId.pop(i)
			
		else:
			print("ERROR: card not in deck. Card-Id: '%s'\nFullDeck:\n" % cardId)
			print(self)
	
	
	def draw(self):
		'''
		Draw a random Card within the Deck.
		Removes from the Deck and Returns it.
		'''
		
		i = random.randrange(len(self.deckCards))
		
		drawnCard = self.deckCards[i]
		
		self.deckCards.pop(i)
		self.listCardsId.pop(i)
		
		return drawnCard
	









class Player:
	
	# List that saves a hand of cards
	hand = []
	
	multiHand = []
	splitCounter = 0
	
	def __init__(self, name, money=100):
		self.name = name
		self.money = money
		self.clearHand()
		
		# Defines a valid filename to Store data
		valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		self.filename = ''.join(char for char in self.name if char in valid_chars)
		
		self.surrendered = False
	
	
	
	def __str__(self):
		return "\n\t   --Player--\n\tName: %s\n\tMoney: %.2f\n\t       --\n\tFile name: '%s'\n\t       --\n\tCurrent hand: %s\n\t     --xx--\n" %(self.name, self.money, self.filename, self.handStr())
	
	
	# Checks if player has balance
	hasBalance = lambda self, val: True if self.money >= val > 0 else False
	
	
	def debt(self, val):
		if self.hasBalance(val):
			self.money -= val
			return True
		
		else:
			return False
	
	
	def credit(self, val):
		self.money += val
		
	
	def addToHand (self, card):
		'''
		Add a card to hand
		'''
		self.hand.append(card)
	
	def handPoints (self):
		'''
		Returns the pontuation of the hand
		'''
		points = 0
		
		for card in self.hand:
			points += card.point
		
		if points > 21:
			
			for card in self.hand:
				if card.cardId[0] == 'a':
					points -= 10
		
		return points
	
	def handStr (self):
		'''
		Returns Hand in string form
		'''
		
		hs = ''
		
		if self.hand == []:
			hs = 'Hand empty!'
		else:
			for card in self.hand:
				hs += '%s, ' %card
				
		return hs
	
	
	displayHand = lambda self: print( self.handStr())
	
	def clearHand(self):
		cardsReturned, self.hand = self.hand, []
		
		for h in self.multiHand:
			for card in h:
				cardsReturned.append(card)
		
		self.multiHand = []
		self.splitCounter = 0
		
		return cardsReturned
	
	
	def checkBJ(self):
		'''
		Return true if hand is Blackjack, False otherwise.
		'''
		acesIds = ['as','ah','ac','ad']
		tenValuedIds = ['0s', '0h', '0c', '0d', 'js', 'jh', 'jc', 'jd', 'qs', 'qh', 'qc', 'qd', 'ks', 'kh', 'kc', 'kd']
		
		return ( len(self.hand) == 2 and self.handPoints() == 21 and all([ (card.cardId in (acesIds+tenValuedIds)) for card in self.hand ]) )
		
	
	
	
	def splittable(self):
		return ( len(self.hand)==2 and self.hand[0].cardId[0]==self.hand[1].cardId[0]  )
	
	
	def splitHand(self):
		self.multiHand.append( [self.hand.pop()] )
		self.splitCounter += 1
		
	
	def switchHand(self, ind):
		self.hand, self.multiHand[ind] = self.multiHand[ind], self.hand
		
	def allHandStr (self):
		'''
		Returns a list all (holding) Hands in string form
		'''
		ahs = []
		
		ind = 0
		
		for h in self.multiHand:
			ahs.append('')
			
			for card in h:
				ahs[ind] += '%s, ' % card
			
			ind += 1
		
		return ahs
	
	def allBusted(self):
		busted = True
		
		def eachHandPoints (hand):
			'''
			Returns the pontuation of the hand
			'''
			points = 0
			
			for card in hand:
				points += card.point
			
			if points > 21:
				
				for card in hand:
					if card.cardId[0] == 'a':
						points -= 10
			
			return points
		
		
		if eachHandPoints(self.hand) <= 21:
			busted = False
			
		for hand in self.multiHand:
			if eachHandPoints(hand) <= 21:
				busted = False
		
		return busted
	
	
	
	
	
	def allBJ(self):
		BJ = True
		
		def eachHandPoints (hand):
			'''
			Returns the pontuation of the hand
			'''
			points = 0
			
			for card in hand:
				points += card.point
			
			if points > 21:
				
				for card in hand:
					if card.cardId[0] == 'a':
						points -= 10
			
			return points
		
		def eachCheckBJ(hand):
			'''
			Return true if hand is Blackjack, False otherwise.
			'''
			acesIds = ['as','ah','ac','ad']
			tenValuedIds = ['0s', '0h', '0c', '0d', 'js', 'jh', 'jc', 'jd', 'qs', 'qh', 'qc', 'qd', 'ks', 'kh', 'kc', 'kd']
			
			return ( len(hand) == 2 and eachHandPoints (hand) == 21 and all([ (card.cardId in (acesIds+tenValuedIds)) for card in hand ]) )
		
		
		if not eachCheckBJ(self.hand):
			BJ = False
			
		for hand in self.multiHand:
			if not eachCheckBJ(hand):
				BJ = False
		
		return BJ








### TEST ###



#print('\t\u2660\t\u2665\t\u2666\t\u2663\n\t\u2664\t\u2661\t\u2662\t\u2667')
#        ♠       ♥       ♦       ♣
#        ♤       ♡       ♢       ♧

'''
newDekc = Deck()

print(newDekc)

print(Card('k','clubs').cardId in newDekc.listCardsId) # true

print(Card('K','clubs').cardId in newDekc.listCardsId) # false


print((Card('Ace','diamonds').cardStr))
print(len(Card('Ace','diamonds').cardStr))
'''


'''
newDekc = Deck()

print('\nFull deck:\n\n',newDekc,'\n')

newDekc.removeCard('as')
newDekc.removeCard('2h')
newDekc.removeCard('3c')
newDekc.removeCard('4d')
newDekc.removeCard('5c')
newDekc.removeCard('6h')
newDekc.removeCard('7s')
newDekc.removeCard('8h')
newDekc.removeCard('9c')
newDekc.removeCard('0d')
newDekc.removeCard('jc')
newDekc.removeCard('qh')
newDekc.removeCard('ks')

print('\nSome cards Removed:\n\n',newDekc,'\n')

newDekc.removeCard('ks')
'''

'''
teles = Player('teles', 100)

print(teles)

placeBet(teles)

print(teles)
'''


'''

teles = Player('teles', 1000)

newDekc = Deck()
print ('\nNew Deck:\n',newDekc)

print ('\nHand:  ',end='')
teles.displayHand()

dealCard(newDekc, teles, 3)
print ('\nRandom Card Drawn!\n\nDeck:\n',newDekc)

print ('\nHand:  ',end='')
teles.displayHand()
print('')



#'''

'''

teles = Player('teles', 1000)
theReceiver = Player('reci', 1000)

newDekc = Deck()

print ('Teles Hand:  ',end='')
teles.displayHand()
print ('Reci Hand:  ',end='')
theReceiver.displayHand()

print('\n\nTeles Draw\n\n')
dealCard(newDekc, teles, 3)

print ('Teles Hand:  ',end='')
teles.displayHand()
print ('Reci Hand:  ',end='')
theReceiver.displayHand()

print('\n\nTeles handed to Reci\n')
theReceiver.hand = teles.clearHand()

print ('Teles Hand:  ',end='')
teles.displayHand()
print ('Reci Hand:  ',end='')
theReceiver.displayHand()




#'''




'''
teles = Player('Joãozinho do Veropa (The Dealer)', 615)
newPlayer(teles)
del teles

teles = loadPlayer('JoozinhodoVeropaTheDealer')
newDekc = Deck()
dealCard(newDekc, teles, 3)
teles.displayHand()
newPlayer(teles)
del teles

teles = loadPlayer('JoozinhodoVeropaTheDealer')
print(teles)
del teles
'''


'''
teles = Player('teles', 1000)
newDekc = Deck()

displayCards(teles)

dealCard(newDekc, teles, 10)

displayCards(teles)
'''




'''

teles = Player('teles', 1000)
newDekc = Deck()

while True:
	
	clear()
	
	teles.clearHand()
	
	dealCard(newDekc, teles, 2)
	
	displayCards(teles)
	
	print('\n\tPoints: %d' % teles.handPoints())
	
	if teles.checkBJ():
		print ('\n\tBLACKJACK\n\nAAAAAAAAAAAAA')
	
	else:
		print ('\n\tnot bj')
		
	x = input('')



#'''




### GAME ###

game()

