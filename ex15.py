'''
Created on Apr 16, 2011


@author: Nako
'''

# importing modules/libraryes from Python Standard Library
from sys import argv

# two variables, initialized with variables from script arguments
script, filename = argv

# txt is a file object, pointing to filename
txt = open(filename)

#printing text
print "Here's your file %r:" % filename

# printing , the result of function read() on txt onject
print txt.read()

#printing text
print "I'll also ask you to type it again:"

# file_again ariable gets its value from console - user input
#file_again = raw_input ("> ")
file_again = filename

#opening filename file_again. txt_again is a file object to this file 
txt_again = open(file_again)

#printing the result of function read() on txt_again file object
print txt_again.readlines(1)
txt.close()
txt_again.close()
print "end9"
print "end10 g1@cyg"

