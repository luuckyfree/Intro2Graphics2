''''
Author: Zach Rogers
Date: May 14 2013
Title: Dragon Game
Version: 1.3
Date Last Modified: May 23nd 2013
Modified Last By: Zach
Changes Made: added the cheat code and loops to validate the selection or "cheatcode"

'''


#import the time function

import time
cheatcode = "dragonsden"

# the function that appears at the start of the game.  to start the journey
def displayIntro():
    print ('You are on a planet full of dragons. In hunt of the secret treasure,')
    print ('It will be a long journey.  Perhaps you will catch the dragon sleeping,')
    print ('if you are lucky, if not, prepare to fight for the treasure.')
    print ('As many men have before.')

# the first cave decision
def chooseCave():
    caveAtNodeOne = ''
    #loop that validates user control
    while caveAtNodeOne != '1' and caveAtNodeOne != '2' and caveAtNodeOne != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        caveAtNodeOne = raw_input()
    #based on user control send them to the next module    
    if (caveAtNodeOne == '1'):
        Node2()
    elif (caveAtNodeOne == '2'):
        Node3()
        #cheat code loop
    elif (caveAtNodeOne == cheatcode):
        Node7()
    else:
        print("Please Make a Valid Selection")

# the module that handles the second node
def Node2():
    time.sleep(1)
    print 'You stumble'
    time.sleep(1)
    print 'You find ten gold!'
    time.sleep(1)
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    # the loop that handles the user input and sends them to the next module
    Decision = raw_input()
    if (Decision == '1'):
        Node4()
    elif (Decision == '2'):
        Node5()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
#the module that handles the third node.  a node needed to have the positive outcome
def Node3():
    time.sleep(1)
    print 'You stumble'
    time.sleep(1)
    print 'You take ten Damage!!'
    time.sleep(1)
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    # the loop that handles the user input and sends them to the next module
    if (Decision == '1'):
        Node6()
    elif (Decision == '2'):
        Node7()
        #cheat code loop
    elif (Decision == 'dragonsden'):
        Node7()
    else:
        print'Please Make a valid decision  (1 or 2)'

# node 4 module.  The start of the bad decision nodes, there is no more positive outcomes from here
#this only leads to negative outcomes and then loops back to play again
def Node4():
    time.sleep(1)
    print 'You stumble'
    time.sleep(1)
    print 'You take ten Damage!!'
    time.sleep(1)
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    # the loop that handles the user input and sends them to a bad outcome which also restarts the game
    if (Decision == '1'):
        OutNegativeTwo()
    elif (Decision == '2'):
        outNegativeFour()
        #cheat code loop
    elif (Decision == 'dragonsden'):
        Node7()
    else:
        print'Please Make a valid decision  (1 or 2)'
        
# node 5 module.  There is no more positive outcomes from here
#this only leads to negative outcomes and then loops back to play again
def Node5():
    time.sleep(1)
    print 'You stumble'
    time.sleep(1)
    print 'You find ten gold!'
    time.sleep(1)
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    # the loop that controls user input and sends them to a negative outcome which also restarts the game
    if (Decision == '1'):
        OutNegativeOne()
    elif (Decision == '2'):
        outNegativeThree()
        #cheat code loop
    elif (Decision == 'dragonsden'):
        Node7()
    else:
        print'Please Make a valid decision  (1 or 2)'

# the 6th node which will send them to negative outcomes and restart the game.
def Node6():
    time.sleep(1)
    print 'You stumble'
    time.sleep(1)
    print 'You find ten gold!'
    time.sleep(1)
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    #the loop to control user input and send them to negative modules
    if (Decision == '1'):
        OutNegativeOne()
    elif (Decision == '2'):
        outNegativeThree()
        #cheat code loop
    elif (Decision == 'dragonsden'):
        Node7()
    else:
        print'Please Make a valid decision  (1 or 2)'

# the node you must make it to to get to the only positive outcome.
#this either sends the user to a negative outcome or to the positive.
def Node7(): 
    time.sleep(1)   
    print 'You stumble'
    time.sleep(1)
    print 'You can hear the dragon puffing'
    time.sleep(3)
    print 'Surely the dragon is right around the corner'
    Decision = ''
    #loop that validates user control
    while Decision != '1' and Decision != '2' and Decision != "dragonsden":
        print ('Which cave will you go into? (1 or 2)')
        Decision = raw_input()
    #loop that controls player decision and sends them to the node.
    if (Decision == '1'):
        outNegativeThree()
    elif (Decision == '2'):
        positiveOutcome()
    else:
        print'Please Make a valid decision  (1 or 2)'

#The prints for the first negative outcome.  Then it loops to the option to play again
def OutNegativeOne():
    print "You walk in and see the dragon amoung it's treasure..."
    time.sleep(2)
    print "You wake him immediately."
    time.sleep(1)
    print "You take leap at him attacking with your sword!"
    time.sleep(1)
    print "He Attacks back instantly..."
    time.sleep(1)
    print "You take another swing at hime!"
    time.sleep(1)
    print "He is too quick and gobbles you up!"

#The prints for the first negative outcome.  Then it loops to the option to play again   
def OutNegativeTwo():
    print "You walk in and see the dragon amoung it's treasure..."
    time.sleep(2)
    print "You wake him immediately."
    time.sleep(1)
    print "You take leap at him attacking with your sword!"
    time.sleep(1)
    print "He Attacks back instantly..."
    time.sleep(1)
    print "You take another swing at hime!"
    time.sleep(1)
    print "You take a lot of damage!..."
    time.sleep(2)
    print"You manage to grab a bag of coins on the ground"
    time.sleep(1)
    print"and see an exit as you dodge his attacks..."
    print"The Dragon dives towards you with his jaws open."
    time.sleep(3)
    print"You manage to leap him and escape with only a few coins"

#The prints for the first negative outcome.  Then it loops to the option to play again    
def outNegativeThree():
    print "You walk in and see the dragon amoung it's treasure..."
    time.sleep(2)
    print "He is still sleeping..."
    time.sleep(1)
    print "You sneak up behind him and pull out your treasure sack..."
    time.sleep(1)
    print "So Much GOLD!!!"
    time.sleep(1)
    print "You start collecting coins, you will get your treasure after all!"
    time.sleep(1)
    print "10 coins, 100 coins, 1000 coins! Ooops, you dropped one!"
    time.sleep(2)
    print"......"
    time.sleep(2)
    print"........."
    print"You hear a loud roar from behind you!"
    print"Time to battle the dragon"
    print"....."
    time.sleep(3)
    print"He gobbled you up before you could even muster an effort!"

#The prints for the first negative outcome.  Then it loops to the option to play again    
def outNegativeFour():
    print "You walk in and see the dragon amoung it's treasure..."
    time.sleep(2)
    print "He is still sleeping..."
    time.sleep(1)
    print "Man that`s one big dragon!"
    time.sleep(1)
    print "You look at his teeth, wow they are sharp."
    time.sleep(1)
    print "You look at all the treasure... It`s a lot of treasure..."
    time.sleep(1)
    print "You hear a grunt from behind....."
    time.sleep(2)
    print"You drop everything and start running for the exit"
    time.sleep(2)
    print"........."
    time.sleep(3)
    print "You escape at the last second unharmed but not any richer."

#The prints for them positive outcome.  Then it loops to the option to play again
def positiveOutcome():
    print "You walk in and see the dragon amoung it's treasure..."
    time.sleep(2)
    print "You wake him immediately."
    time.sleep(1)
    print "You take leap at him attacking with your sword!"
    time.sleep(1)
    print "He Attacks back instantly..."
    time.sleep(1)
    print "You take another swing at hime!"
    time.sleep(1)
    print "You take a lot of damage!..."
    time.sleep(2)
    print"With the last of your might you raise your sword and leap toward the dragon"
    time.sleep(1)
    print"...."
    time.sleep(1)
    print"...."
    time.sleep(1)
    print"...."
    time.sleep(1)
    print"You open your eyes and see you have hit the dragon in the heart"
    print"He seems to be weak..."
    time.sleep(3)
    print"You give the dragon it's final blow..."
    time.sleep(3)
    print"It drops to the ground and you can relax now."
    time.sleep(4)
    print"Congratulations... You have defeated the dragon"
    time.sleep(1)
    print"You get to keep the secret treasure!"

def main():
    
    #the play again loop, within the loop it will restart the opening module and cave picking system
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        chooseCave()
        
        
        
        
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()

#calling the main function.
if __name__ == "__main__": main()

