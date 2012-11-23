########################################
#
# printbasics2.py
# Algot Runeman
# 2012-11-23
#
# I find that it helps me to explain things to myself
# when I program. The input from book or tutorial works
# best for me when I try to explain what I've 'learned'.
#
########################################

source01 = 'first'
source02 = 'word'
source03 = 'second'
source04 = '  t h i r d  '
source05 = 'FOURTH'
source06 = 'OdD lEtTer CASE'
source07 = 'this should look like a title - sort of'
source08 = 'eight eight eight eight'

print ''  ## empty line method 1
print '***************************'
print '*  Print Basics - Part 2  *'
print '***************************'
print ''
print 'The print command must be lower case. "Print age" will not work.'
print 'PRINT age will not work either.'
print 'All Python commands are lower case.'
print ''
print 'In Python, either quote mark can "enclose" the other.'
print 'But, you must match the quote marks. Both outer must be the same.'
print 'The command \"print \'something\'\" works.'
print 'print \'something" does not work'
print 'TRY to be CONSISTENT. It will make your code easier to read.'
print ''
print 'In the 3.x versions of Python, print is a function call.'
print "That means print('something') replaces the earlier version: print 'something'"
print ''
print 'Commas are needed between the "items" of a print statement.'
print 'print "John", age , for example'
raw_input ("\n\nEnter for next section:")

print ''
print '***************************'
print '*     Combining Strings   *'
print '***************************'
print ''
print 'Combining strings is "concatenating".'
print 'Do it with "variable1 + variable2."
print 'The first two words are:',source01,'and',source02
print 'Concatenate - ', source01 + source02, '<--note lack of spaces'

## to get the newline code to print, use extra slash \
print 'Note next blank line created with "newline - \\n" in next print'

print '\nConcatenate with extra space concatenated between -->', source03 + ' ' + source02
print 'Make a long line quickly with "-"*50'
print '-'*50
raw_input ("\n\nEnter for next section:")

#################
# Case controls #
#################

## print variables 'as-is'
print '*****************************'
print '* Original string variables *'
print '*****************************'
print ''
print 'These are the original string variables which will be used in examples.'
print 'variable "source01" is: ', source01
print 'variable "source02" is: ', source02
print 'variable "source03" is: ', source03
print 'variable "source04" is: ', source04
print 'variable "source05" is: ', source05
print 'varibale "source06" is: ', source06
print 'variable "source07" is: ', source07
print 'variable "source08" is: ', source08
raw_input ("\n\nEnter for next section:")

print '***************************'
print '* Control of string case  *'
print '***************************'
print ''
print 'There are case control "methods".' 
           
## All of the string - upper()
print 'Use variable.upper() to convert to all CAPS.'
print 'All caps, any string - ', source01, ":", source01.upper() ## All caps
print '-'*50
## Just first letter of string - capitalize()
print 'Use variable.capitalize() to for just first letter of string like sentences.'
print 'Capitalize only first letter of string -', source01, 'becomes', source01.capitalize()
print '-'*50

## Remove whitespace at beginning or end - strip()
print 'Remove leading and trailing whitespace -', source04, 'becomes', source04.strip()
print 'Spaces inside the sring are not removed.'
print '-'*50

## Lower case - lower()
print 'Lower case a string -',source05, 'becomes', source05.lower()

print '-'*50
## Swap case - swapcase()
print 'Swap case -', source06.swapcase()

## Title case - title()
## NOTE doesn't ignore the journalistic standard of ignoring connector words like 'A'
print source07, ":", source07.title()
print 'A real title would not capitalize connector words like "of".'
print 50*'-'

## replace(old, new)
print 'replace(old,new) replaces words in a string.'
print source08, 'becomes', source08.replace('eight','five')
print 'Strings to replace must be in quotes, as usual.'
print 'You can count part way through "variable.replace(old,new,2)'
print 'Replace first two only:', source08, 'becomes', source08.replace('eight','five',2)
print 50*'-'
raw_input("Tap the Enter to finish:")           


