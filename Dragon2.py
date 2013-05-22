''''
Author: Zach Rogers
Date: May 14 2013
Title: Dragon Game
Version: 1.1
Date Last Modified: May 21st 2013
Modified Last By: Zach
Changes Made: Removed time to make for quicker testing.  Removed Random caves. Added pre determined nodes.


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
    print 'Cave 1 or 2?'
    Decision = raw_input()
    if (Decision == '1'):
        outNegativeThree()
    elif (Decision == '2'):
        positiveOutcome()
    else:
        print'Please Make a valid decision  (1 or 2)'
    
def OutNegativeOne():
    print 'Fight the Dragon and lose'
    
def OutNegativeTwo():
    print 'Fight the Dragon but manage to escape'
    
def outNegativeThree():
    print 'Fight the dragon down to his last health and lose'
    
def outNegativeFour():
    print "You take one look at the dragon and run away"

def positiveOutcome():
    print 'You defeat the dragon and collect his treasure!'
    

def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        chooseCave()
        
        
        
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()

