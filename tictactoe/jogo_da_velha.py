'''
JOGO DA VELHA - projeto 1
'''



### IMPORTS ###

import os


### STATEMENTS ###

clear = lambda: os.system('clear')

board = []
firstPlayer = 'X'
gameOn = False







### FUNCTIONS ###

def whosFirst():
	global firstPlayer
	clear()
	
	print('\n')
	whosFirst = True
	while whosFirst:
		firstPlayer = input("Who plays first?  (X/O)\nAns: ").upper()
		if firstPlayer not in ['X','O']:
			clear()
			print("\nThat's not an option. Stop being a condescending bitch.")
		else:
			whosFirst = False


def initMatch():
	'''
	Initializes and plays a Match
	'''
	
	global firstPlayer
	global board
	clearBoard()
	
	clear()
	print('\n')
	
	turn = firstPlayer
	matchOn = True
	winner = ''
	while matchOn:
		
		lastMove = play(turn)
		
		(matchOn,winner) = checkMatch(turn, lastMove)
		
		if turn=='X':
			turn = 'O'
		else:
			turn = 'X'
		
	else:
		endMatchMsg(winner)



def clearBoard():
	'''
	Resets the board
	'''
	global board
	board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	
	pass







def displayBoard(board):
	'''
	Displays the board
	'''
	clear()
	
	print(   '/---+----+----\\' )
	print( '| %s |  %s |  %s |' %(board[0][0], board[0][1], board[0][2]))
	print(  '+---+----+----+' )
	print( '| %s |  %s |  %s |' %(board[1][0], board[1][1], board[1][2]))
	print(   '+---+----+----+' )
	print( '| %s |  %s |  %s |' %(board[2][0], board[2][1], board[2][2]))
	print( '\\---+----+----/' )





def play(player):
	
	global board
	
	notPlayed = True
	notPossible = False
	lastMove = [0,0]
	
	while notPlayed:
		
		displayBoard(board)
		
		print("\nPossible moves:\n")
		print( '._____.' )
		print( '|%s|%s|%s|' %( ('7' if board[0][0]==' ' else ' '), ('8' if board[0][1]==' ' else ' '), ('9' if board[0][2]==' ' else ' ')  ))
		print( '|%s|%s|%s|' %( ('4' if board[1][0]==' ' else ' '), ('5' if board[1][1]==' ' else ' '), ('6' if board[1][2]==' ' else ' ')  ))
		print( '|%s|%s|%s|' %( ('1' if board[2][0]==' ' else ' '), ('2' if board[2][1]==' ' else ' '), ('3' if board[2][2]==' ' else ' ')  ))
		print( "'¨¨¨¨¨'" )
		
		print("That's not a possible move bitch!") if notPossible else print('')
		notPossible = False
		move = input("MOVE BITCH (%s): " %player)
		
		
		def check(lin,col):
			if board[lin][col] == ' ':
				board[lin][col] = player
				
				nonlocal notPlayed
				notPlayed = False
				
				nonlocal lastMove
				lastMove = [lin,col]
			else:
				nonlocal notPossible
				notPossible = True
		
		if move == '7':
			check(0,0)
		elif move == '8':
			check(0,1)
		elif move == '9':
			check(0,2)
		elif move == '4':
			check(1,0)
		elif move == '5':
			check(1,1)
		elif move == '6':
			check(1,2)
		elif move == '1':
			check(2,0)
		elif move == '2':
			check(2,1)
		elif move == '3':
			check(2,2)
		else:
			notPossible = True
	
	return lastMove








def checkMatch(player, lastMove):
	'''
	Checks if a match has been won by a specific player.
	Then, checks if there still is any possible move.
	'''
		
	global board
	(line, col) = lastMove
	
	
	checkHoriz = lambda line: board[line] == [player]*3
	checkVert = lambda col: [x[col] for x in board] == [player]*3
	checkDiag1 = lambda: [board[ind][ind] for ind in [0,1,2] ] == [player]*3
	checkDiag2 = lambda: [board[ind][2-ind] for ind in [0,1,2] ] == [player]*3
	
	possibMoves = lambda: ' ' in [ board[i][j]  for i in [0,1,2] for j in [0,1,2]]
	
	if (checkHoriz(line) or checkVert(col)) or (checkDiag1() or checkDiag2()):
		matchOn = False
		winner = player
	elif not possibMoves():
		matchOn = False
		winner = 'T'	# it's a tie
	else:
		matchOn = True
		winner = ''
	
	return (matchOn,winner)







def endMatchMsg(winner):
	
	displayBoard(board)
	print('')
	
	if winner=='X':
		loser = 'O'
	else:
		loser = 'X'
	
	if winner == 'X' or winner == 'O':
		print('EEEEEEEE POORRRAAAA\n\nJogador %s venceu.\n\nChupa %s !\n\n' %(winner, loser))
	elif winner == 'T':
		print("It's a tie, bitch.\n\nNossa, ces são um cu.\n\n")
	else:
		print('...\nO que...\n CARALHOS...\nvcs fizeram?\n\n')








def cont(starting=False):
	'''
	At the start of the game asks who is gonna play first.
	Asks if continue game and changes global gameOn accordingly.
	'''
	
	global gameOn
	
	if starting:
		whosFirst()
		gameOn = True
	else:
		
		cont = True
		while cont:
			ans = input("Continue playing?  (Y/N)\nAns: ").upper()
			if ans not in ['Y','N','']:
				clear()
				print("\nDon't you fucking know how to write?")
			else:
				cont = False
		
		if ans == 'N':
			clear()
			print("\n\nGo fuck yourself.\n\n")
			gameOn = False







### GAME ###

cont(starting=True)

while gameOn:
	
	initMatch()
	
	cont()
	

