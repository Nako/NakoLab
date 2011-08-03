# -*- coding: utf-8 -*-
'''
Created on 14.07.2011

@author: nako
'''

'''
Homework

Now write a similar game to the one that I created in the last exercise. 
It can be any kind of game you want in the same flavor. 
Spend a week on it making it as interesting as possible. 
For extra credit, use lists, functions, and modules (remember those from Ex. 13?) as much as possible, 
and find as many new pieces of Python as you can to make the game work.

There is one catch though, write up your idea for the game first. 
Before you start coding you must write up a map for your game. 
Create the rooms, monsters, and traps that the player must go through on paper before you code.

Once you have your map, try to code it up. 
If you find problems with the map then adjust it and make the code match.
'''

import random
#from array import *
#import numarray
#import numpy
import array 
from numpy import * 

'''
# ARRAY HOWTO !
mlist1 = [
[7, 12, 23],
[22, 31, 9],
[4, 17, 31]]

print mlist1  # [[7, 12, 23], [22, 31, 9], [4, 17, 31]]

# show list_item at index 1
print mlist1[1]  # [22, 31, 9]

# show item 2 in that sublist
print mlist1[1][2]  # 9

# change the value
mlist1[1][2] = 99

print mlist1  # [[7, 12, 23], [22, 31, 99], [4, 17, 31]]


###########
# create a 10 x 10 matrix of zeroes
matrix10x10 = [[0 for col in range(10)] for row in range(10)]
 
# fill it with 1 diagonally
for i in range(10):
    matrix10x10[i][i] = 1
 
# show it
for row in matrix10x10:
    print row
 
"""
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
"""

'''


'''
a = array('l', 
          [1, 2, 3, 4, 5]
          [1, 2, 3, 4, 5]
          [1, 2, 3, 4, 5]
          )
print a[2] 
'''
'''
b = array('l',
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
)
'''

#a = zeros((3,5))
a = zeros((3,5))
a[1,2] = 8
print a
 
rooms_descriptions = ["room zero", "room one", "room_two"]

maze_x = 4
maze_y = 4
maze = []

def create_maze():
    for x in range(0,maze_x):
        maze.append(x)
        for y in range(0,maze_y):
            maze.append(y)

def makeRandomMaze(dimension):
    """ Generate a random maze of size dimension x dimension """    
    rows = []
    for x in range(dimension):
        row = []
        for y in range(dimension):
            row.append(random.randrange(2))
        random.shuffle(row)
        rows.append(row)
    
    return rows
                           

def room_zero():
    print room_zero.__name__
    print rooms_descriptions[0]
    
    
def die(diestring):
    print "game over"
    print diestring
    exit (0)

def start():
    dieturns = 5
    debugcounter = 0    
    print "start of the game"
    while True:
        debugcounter = debugcounter + 1 
        if debugcounter >= dieturns:
            die("debug: too many turns: %d" % dieturns)
    
        # game body start
        
        room_zero()
        
        
        # game body end

#start()
create_maze()
print maze 


#xmaze = makeRandomMaze(6)
#print xmaze


mazeborder = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
       ]

print mazeborder 
