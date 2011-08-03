'''
Created on 20.07.2011

@author: Nako
'''
#from random import randint
import random   
mysum = 0
mymaxcount = 100000
for xx in range (0,100):
    random.seed(random.randint(0,100))

for i in range(1,mymaxcount):
    #print i
    #irandom = random.randint(0,100)
    irandom = random.random()
    #print "random: ", irandom 
    mysum = mysum + irandom 

print "sum: ", mysum 
print "average:" , mysum / mymaxcount
