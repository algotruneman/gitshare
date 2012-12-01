########################################
#
# zeller.py
# Exercise OPT.1 for 26Nov2012 Mechanical MOOC
# Algot Runeman
# Date...December 1, 2012
#
########################################

A = 0

print 'This program uses Zeller\'s Algorithm to determine the'
print 'day of the week for any date (AD) entered.'
print 'Have fun!'
print 50*'*'

## Input Section

C = raw_input('\nYear (YYYY): ')
D = int(C[0]+C[1])
##print 'Century:', D
C = int(C[2]+C[3])
##print 'Year: ', C

while A == 0:
    a = raw_input('Month: ')
    a = a.lower()
    if a == 'january' or a == '1':
        A = 11
        C=C-1
    elif a == 'february' or a == '2':
        A = 12
        C=C-1
    elif a == 'march' or a == '3':
        A - 1
    elif a == 'april' or a == '4':
        A = 2
    elif a == 'may' or a == '5':
        A = 3
    elif a == 'june' or a == '6':
        A = 4    
    elif a == 'july' or a == '7':
        A = 5
    elif a == 'august' or a == '8':
        A = 6
    elif a == 'september' or a == '9':
        A = 7
    elif a == 'october' or a == '10':
        A = 8
    elif a == 'november' or a == '11':
        A = 9
    elif a == 'december' or a == '12':
        A = 10
    else:
        print 'You spelled the month wrong!'
    continue
B = ''
while B == '':
    B = int(raw_input('Day of the month: '))    
    if B < 1 or B > 31:
        print 'Rembember all days are from 1 to 31 in any month.'
    continue    
W = (13*A-1)/5
X = C/4
Y = D/4
Z = W+X+Y+B+C-2*D
R = Z%7

print '-----------------'
print 'That date is a',
if R == 0: print 'Sunday.'
elif R == 1: print 'Monday.'
elif R == 2: print 'Tuesday.'
elif R == 3: print 'Wednesday.'
elif R == 4: print 'Thursday.'
elif R == 5: print 'Friday.'
else: print 'Saturday.'



