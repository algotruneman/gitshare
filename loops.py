########################################
#
# loops.py - Exercise 1.8 MMOOC-26nov2012
# Algot Runeman <algot.runeman@verizon.net>
# 2012-11-30
#
########################################

# 1.8.1
# for loop decimal equivalents of fractions
print '\nExercise 1.8.1'
print 50*'*'
for i in range(1,11):
    print '1 /',i,'=', 1.0/float(i)
    
#######################################
# 1.8.2
# while loop countdown from user's input
print '\nExercise 1.8.2'
print 50*'*'

start = input ('give me a whole number: ')
print 'Counting down!'
while start >= 0:
    print start
    start = start - 1
print 'Done!'    

########################################
# 1.8.3
# show values of base up to exponent
print '\nExercise 1.8.3'
print 50*'*'
val = 0.0
a = float (raw_input('Enter the base: '))
b = int (raw_input('Enter the exponent: '))           
count = 1.0
#while count < b+1:
for count in range(1,b+1):
    val = a ** count
    print val, count
    count = count + 1
    
#########################################
# 1.8.4
# Force an even number input
print '\nExercise 1.8.4'
print 50*'*'
a = 0
tries = 1
while a == 0:
    answer = raw_input('Plesse enter an even number: ')
    guess = int(answer)
    guess = guess % 2
    if guess != 0:
        print 'The number you enter must be EVEN! I told you before.'
        tries += 1
        continue
    else: a = 1
print 'Thanks',answer,'is EVEN.'
if tries == 1:
    print "And you got it in one try!"
else:
    print "But it took you",tries,"tries to get it!"


