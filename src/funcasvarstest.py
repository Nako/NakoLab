'''
Created on 20.07.2011

@author: Nako
'''
from random import randint 
#import sys

def myrandfunc():
    irandom = randint (0,4)
    print "irandom=", irandom 
    return irandom 

def func0():
    print "func 0"
    #return randint(0,4)
    return myrandfunc()

def func1():
    print "func 1"
    #return randint(0,4)
    return myrandfunc()
def func2():
    print "func 1"
#    return randint(0,4)
    return myrandfunc()

def func3():
    print "func 3"
#    return randint(0,4)
    return myrandfunc()

def func4():
    print "func 4"
#    return randint(0,4)
    return myrandfunc()

flist = {}
'''
flist["zero"] = func0()
flist["one"] = func1()
flist["two"] = func2()
flist["tree"] = func3()
flist["four"] = func4()
'''

flist[0] = func0()
flist[1] = func1()
flist[2] = func2()
flist[3] = func3()
flist[4] = func4()

def runner(nextfunc):
    #debug
    count = 0     
    while True:
        print "nf=", nextfunc
        count = count + 1
        nextfunc = flist[nextfunc]
        if count > 20:
            exit(0)

runner(0)

'''     
print flist["one"]

list1 = []
for x in range (5):
    print x 
    list1.append(x)
'''