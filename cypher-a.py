########################################
#
# cypher-a.py OPT1.2 for 26Nov2012 Mechanical MOOC
# Algot Runeman
# Start 2012-12-01
# Finish
#
########################################
c = ''
b = ''
a = 'abcdefghijklmnopqrstuvwxyz'
shift = 0
while shift < 1 or shift >25:
    shift = int(raw_input('Enter a shift value 1-25: '))
    if shift > 25:
        print 'Try again to fit from 1 to 25.'

for i in range(0,len(a)-shift):
    b = b + a[i]

for i in range(len(a)-shift,len(a)):
    c = c + a[i]
b = c+b
print 'ORIGINAL'
print a
print 'SHIFT',shift
print b
