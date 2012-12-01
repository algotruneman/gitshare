########################################
#
# cypher-c.py OPT1.2 for 26Nov2012 Mechanical MOOC
# DECODER
# Algot Runeman
# Date... 2012-12-01
#
########################################

print 'program cypher-c.py'
print 'Basic rotation/shift cryptography'
print 50*'*'
print 'DECODE the previously coded message.'
b = ''
c = ''
shift = 0
decoded = ''
while shift < 1 or shift >25:
    shift = int(raw_input('Enter a shift value 1-25: '))
    
    if shift > 26 or shift < 1:
        print 'Try again to fit from 1 to 25.'
a = raw_input('Enter the CODED message: ')
a = a.upper()

for i in range(0,len(a)):
    print a[i], '==',ord(a[i]), '-->',
    z = ord(a[i])
    print z, 65-z,
    z = z - shift
    if z + shift == 32: # deal with spaces
        z = 32
    elif z < 65:
        offset = 65 - z
        z = 91 - offset
    
    print chr(z)
    decoded = decoded + chr(z)
print a
print decoded
