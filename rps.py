########################################
#
# rps.py - 1.7 Rock Paper Scissors MMOOC
# Algot Runeman
# 2012-11-30
#
########################################

##RPS MMOOC 1.7 Truth Table
##=========================

##player 1     - player 2     - Result
##rock         - rock         - tie
##rock         - paper        - p2
##rock         - scissors     - p1
##paper        - paper        - tie
##paper        - rock         - p1
##paper        - scissors     - p2
##scissors     - scissors     - tie
##scissors     - paper        - p1
##scissors     - rock         - p2
p1 = ''
winner = ''

print 'Exercise: 1.7 Rock, Paper, Scissors'
print 50*'*'
print '\nThis is a my weak implementation of the classic game'
print 'because the second player can see the first player\'s guess.'
while p1 != 'rock' or p1 != 'scissors' or p1 != 'paper':
    p1 = raw_input('\n Player 1, enter your guess (rock, paper, scissors)')
    p1 = p1.lower()
    if p1 == 'rock' or p1 == 'paper' or p1 == 'scissors':
        break
    else:
        print "You MUST enter only rock, paper or scissors."
p2 = ''
while p2 != 'rock' or p2 != 'scissors' or p2 != 'paper':
    p2 = raw_input(' Player 2, enter your guess (rock, paper, scissors)')
    p2 = p2.lower()
    if p2 == 'rock' or p2 == 'paper' or p2 == 'scissors':
        break
    else:
        print "You MUST enter only rock, paper or scissors."
    
if p1 == 'rock' and p2 == 'scissors':
    winner = 'Player 1'
elif p1 == 'paper' and p2 == 'rock':
    winner = 'Player 1'
elif p1 == 'scissors' and p2 == 'paper':
    winner = 'Player 1'

elif p2 == 'rock' and p1 == 'scissors':
    winner = 'Player 2'
elif p2 == 'paper' and p1 == 'rock':
    winner = 'Player 2'
elif p2 == 'scissors' and p1 == 'paper':
    winner = 'Player 2'        

else:
    print 'Tie. Run again.\n'

if winner != '':
    print winner,'wins!\n'
raw_input ('tap enter to end.'    )
