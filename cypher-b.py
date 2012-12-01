########################################
#
# cypher-b.py OPT1.2 for 26Nov2012 Mechanical MOOC
# ENCODER
# Algot Runeman
# Date... 2012-12-01
#
########################################

print 'program: cypher-b.py'
print 'Basic rotation/shift cryptography.'
print 50*'*'
# Second "working" version does not handle punctuation.
c = ''
b = ''
newMsg = ''
shift = 0
while shift < 1 or shift >25:
    shift = int(raw_input('Enter a shift value 1-25: '))
    
    if shift > 25 or shift < 1:
        print 'Try again to fit from 1 to 25.'
a = raw_input('Enter your short message: ')
a = a.upper()

for i in range(0,len(a)):
    print a[i], '-->',ord(a[i]),
    z = ord(a[i])+shift    
    if z == 32+shift: # deal with spaces
        z = 32
    elif z >90:
        z = z - 26
    
    print chr(z)
    newMsg = newMsg + chr(z)
print a
print newMsg



## cypher-a.py == cypher.py == Initial test code for shift
###'abcdefghijklmnopqrstuvwxyz'
##shift = 0
##while shift < 1 or shift >25:
##    shift = int(raw_input('Enter a shift value 1-25: '))
##    if shift > 25:
##        print 'Try again to fit from 1 to 25.'
##
##for i in range(0,len(a)-shift):
##    b = b + a[i]
##
##for i in range(len(a)-shift,len(a)):
##    c = c + a[i]
##b = c+b
##print 'ORIGINAL'
##print a
##print 'SHIFT',shift
##print b
