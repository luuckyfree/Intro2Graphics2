''''
Author: Zach Rogers
Date: May 14 2013
Title: Dragon Game
Version: 1.2
Date Last Modified: May 22nd 2013
Modified Last By: Zach
Changes Made: Added sleeps and made the nodes actual story based prints, before they were just test prints for quick testing

'''



import random
import time

def displayIntro():
    print ('You are on a planet full of dragons. In hunt of the secret treasure,')
    print ('It will be a long journey.  Perhaps you will catch the dragon sleeping,')
    print ('if you are lucky, if not, prepare to fight for the treasure.')
    print ('As many men have before.')
    
def chooseCave():
    caveAtNodeOne = ''
    while caveAtNodeOne != '1' and caveAtNodeOne != '2':
        print ('Which cave will you go into? (1 or 2)')
        caveAtNodeOne = raw_input()
        
    if (caveAtNodeOne == '1'):
        Node2()
    elif (caveAtNodeOne == '2'):
        Node3()
    else:
        print("Please Make a Valid Selection")

def Node2():
    print 'Node2'
    print 'You stumble'
    print 'You find ten gold!'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        Node4()
    elif (Decision == '2'):
        Node5()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
    
def Node3():
    print 'Node3'    
    print 'You stumble'
    print 'You take ten Damage!!'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        Node6()
    elif (Decision == '2'):
        Node7()
    else:
        print'Please Make a valid decision  (1 or 2)'

def Node4():
    print 'Node4'
    print 'You stumble'
    print 'You take ten Damage!!'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        OutNegativeTwo()
    elif (Decision == '2'):
        outNegativeFour()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
def Node5():
    print'Node5'
    print 'You stumble'
    print 'You find ten gold!'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        OutNegativeOne()
    elif (Decision == '2'):
        outNegativeThree()
    else:
        print'Please Make a valid decision  (1 or 2)'

def Node6():
    print 'Node6'
    print 'You stumble'
    print 'You find ten gold!'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        OutNegativeOne()
    elif (Decision == '2'):
        outNegativeThree()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
def Node7():    
    print 'Node 7'
    print 'You stumble'
    print 'You can hear the dragon puffing'
    time.sleep(3)
    print 'Surely the dragon is right around the corner'
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        outNegativeThree()
    elif (Decision == '2'):
        positiveOutcome()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
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
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        chooseCave()
        
        
        
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()

