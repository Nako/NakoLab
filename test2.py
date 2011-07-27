'''
Created on 22.07.2011

@author: Nako
'''
print "hello github"

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)



myString = 'Hello, world!'
myList = [0, 'one', 1, 'two', 3, 'five', 8]
 
print myString[:5]  # prints Hello
print myString[2:]
print myList[2:5]    # prints [0, 'one', 1, 'two', 3]


print 'e' in myString   # prints True
print 5 in myList       # prints False

if 'e' in myString:
    print "e is in mystring"

if 5 in myList:
    print "5 is in mylist"
print "bp0"
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
        print "animal init, with name ", name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
 
class Cat(Animal):
#    def __init__(self, name):
#        print "cat init with name", name
    #def __init__(self, name):
     #   print "cat init with name", name
    def talk(self):
        return 'Meow!'
 
class Dog(Animal):
#    def __init__(self, name):
#        print "dog init with name", name
    def talk(self):
        return 'Woof! Woof!'
 
animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]
print "bp1"
for animal in animals:
    print animal.name + ': ' + animal.talk()
 
# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!


#playerWins = True 
playerWins = True

if playerWins:
    print 'You win!'
else:
    print 'You lose...'

playerWins = False
print "bp2"
#[ print 'You lose...', print 'You win!' ][ playerWins ]
print("You Win!" if playerWins else "You lose!")

