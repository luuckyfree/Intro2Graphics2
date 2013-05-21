''''
Author: Zach Rogers
Date: May 14 2013
Title: Dragon Game
Version: 1.0
Date Last Modified: May 17th 2013
Modified Last By: Zach
Changes Made: Set up intro and created character function as well as added the rest of the nodes.


'''


import random
import time

#This is the main function that will start the game by calling the character info module to get
#some basic information
totalEarnings = 0
health = 50
def main():
    characterInfo()
    
    displayIntro()
    caveNumber = chooseCave()
    checkCaveOne(caveNumber, health, totalEarnings)
    levelTwoIntro()
    secondCave = chooseCave()
    levelTwo(secondCave, health, totalEarnings)
    justBeforeTheDragon(secondCave, health, totalEarnings)

    
    '''
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()
        '''
# This module stores gets and store the character information.
def characterInfo():
    #Declaring choice variablese to make their choice not case sensitive
    yesChoice = "yes"
    noChoice = "no" 

    #Get the users name
    name = raw_input("What is your name?")
    print ("Hello " + name + ".")  
    time.sleep(2)
    
    #Give them a choice between risking their life or quiting
    riskLife = raw_input("Are you sure you want to risk your life in search of the dragons treasure? (yes or no)")
    #choosing to quit
    if (riskLife == noChoice):
        print("Smart Choice.  Best not get involved with a dangerous dragon like that")
    #choosing to play and calling the intro module
    elif (riskLife == yesChoice):
        print("Welcome ") + name + (" Let the adventure begin!")
        time.sleep(3)
    # error handling for inproper input    
    else:
        print("noob")

#the introduction to the game.  This is called in the character module
def displayIntro():
    print ('You are on a planet full of dragons. In front of you,')
    print ("......")
    time.sleep(2)
    print ('you see two caves. Who knows what is in either cave.')
    print ("......")
    time.sleep(2)
    print ('perhaps you will stumble upon treasures or perhaps')
    print ("......")
    time.sleep(2)
    print ('you will be eaten by the dragons.')
    
    
#This module choses between caves and gets the user input
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    return cave

#this module determines the result of the cave choice, we are calling chosenCave health and total earnings from other modules.
def checkCaveOne(chosenCave, health, totalEarnings):
    print ('You approach the cave...')
    time.sleep(2)
    print ('It is dark and spooky...')
    time.sleep(2)
    print ('You slip down the rocks and...')
    time.sleep(2)
#this randomly decides which cave is friendly   
    friendlyCave = random.randint(1, 2)
#this if statement prints the results of the cave and displays updated health or earnings based on wether the cave was friendly or not.   
    if chosenCave == str(friendlyCave):
        print ('you find some treasure!')
        totalEarnings = totalEarnings + 25
        time.sleep(1)
        print ('You now have ' + str(totalEarnings) + ' gold')
        return totalEarnings

#The negative side of the cave choice and updated health print
    else:
        print ('You Slip and take ten damage')
        health = health - 10
        time.sleep(1)
        print ('You now have ' + str(health) + ' health')
        return health
    print('Hello')

def levelTwoIntro():
    print ("You look around and realize there is more to this cave system than you originally thought!")
    print ("It's probably best to keep going, you've gone too far now.")
    print ("You come to another fork in the road!")
    
    
def levelTwo(secondCave, health, totalEarnings):
    
    friendlyCave = random.randint(1, 2)
    
    if secondCave == str(friendlyCave):
        print ('you find some treasure!')
        totalEarnings = totalEarnings + 25
        time.sleep(1)
        print ('You now have ' + str(totalEarnings) + ' gold')
        return totalEarnings


    else:
        print ('You Slip and take ten damage')
        health = health - 10
        time.sleep(1)
        print ('You now have ' + str(health) + ' health')
        return health
    print health
    print totalEarnings
       
def justBeforeTheDragon(secondCave, health, totalEarnings):
    time.sleep(3)
    print ("You can hear the dragon now.")
    print("..............")
    print ("you get very scared")
    print('.....................')
    time.sleep(4)
    print("OH $%#&#^$$!!!!!!!!!!!!!!!!")
    friendlyDragon = random.randint(1, 2)
    '''if endGame == str(friendlyDragon):
        print ('You reason with the dragon and he lets you go')
        print ('Whew that was close.  At least I have my' + health + ' health and ' + totalEarnings + ' Gold')
        
    '''
    
    
if __name__ == "__main__": main()