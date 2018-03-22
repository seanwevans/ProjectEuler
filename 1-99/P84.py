# In the game, Monopoly, the standard board is set up in the following way:
#
# GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
# H2									 	C1
# T2	 									U1
# H1	 									C2
# CH3	 									C3
# R4	 									R2
# G3	 									D1
# CC3	 									CC2
# G2	 									D2
# G1	 									D3
# G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
#
# A player starts on the GO square and adds the scores on two 6-sided dice to determine the number 
# of squares they advance in a clockwise direction. Without any further rules we would expect to 
# visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), 
# CC (community chest), and CH (chance) changes this distribution.
# In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to 
# jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd 
# roll. Instead they proceed directly to jail.
# At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH 
# they take a card from the top of the respective pile and, after following the instructions, it is 
# returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of 
# this problem we are only concerned with cards that order a movement; any instruction not concerned 
# with movement will be ignored and the player will remain on the CC/CH square.
# Community Chest (2/16 cards):
# Advance to GO
# Go to JAIL
# Chance (10/16 cards):
# Advance to GO
# Go to JAIL
# Go to C1
# Go to E3
# Go to H2
# Go to R1
# Go to next R (railway company)
# Go to next R
# Go to next U (utility company)
# Go back 3 squares.
# The heart of this problem concerns the likelihood of visiting a particular square. That is, the 
# probability of finishing at that square after a roll. For this reason it should be clear that,
# with the exception of G2J for which the probability of finishing on it is zero, the CH squares 
# will have the lowest probabilities, as 5/8 request a movement to another square, and it is the
# final square that the player finishes at on each roll that we are interested in. We shall make no
# distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule 
# about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
# By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these
# two-digit numbers to produce strings that correspond with sets of squares.
# Statistically it can be shown that the three most popular squares, in order, are
# JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most
# popular squares can be listed with the six-digit modal string: 102400.
# If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

from random import randrange, shuffle
from collections import Counter
from time import clock

st = clock()

Monopoly_Board = {i:0 for i in range(40)}
Chest = Chance = [i for i in range(16)]
shuffle(Chest)
shuffle(Chance)

GO, JAIL, G2J = 0, 10, 30
C1, E3, H2 = 11, 24, 39
CH = (2,17,33)
CC = (7,22,36)
RR = (5,15,25,35)
UT = (12,28)

doubles = 0
totalrolls = 10**7
board_pos = GO

for i in range(totalrolls):

	die1, die2 = randrange(1,7), randrange(1,7)
	roll = die1 + die2

	if die1 == die2:	doubles += 1
	else:			doubles = 0
	
	if doubles > 2:
		board_pos = JAIL
		doubles = 0
		Monopoly_Board[JAIL] += 1
		continue

	board_pos += roll
	board_pos = board_pos % 40
	
	if board_pos in CH:
		card = Chance[0]
		Chance.remove(card)
		Chance.append(card)
		if card == 0:	board_pos = JAIL
		if card == 1:	board_pos = GO
		if card == 2:	board_pos = C1
		if card == 3:	board_pos = E3
		if card == 4:	board_pos = H2
		if card == 5:	board_pos = RR[0]
		if card == 6 or card == 7:
			if board_pos == CH[0]:	board_pos = RR[0]
			if board_pos == CH[1]:	board_pos = RR[2]
			if board_pos == CH[2]:	board_pos = RR[3]
		if card == 8:
			if board_pos == CH[0] or board_pos == CH[2]:	board_pos = UT[0]
			if board_pos == CH[1]:	board_pos = UT[1]
		if card == 9:
			board_pos -= 3
			board_pos = board_pos % 40
	
	if board_pos in CC:
		card = Chest[0]
		Chest.remove(card)
		Chest.append(card)
		if card == 0:	board_pos = GO
		if card == 1:	board_pos = JAIL
		
	if board_pos == G2J:
		board_pos = JAIL
	
	Monopoly_Board[board_pos] += 1
	
print(Counter(Monopoly_Board).most_common(40))
print(clock() - st)
