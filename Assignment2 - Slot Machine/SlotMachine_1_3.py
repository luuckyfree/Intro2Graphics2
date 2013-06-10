# Source File Name: slotmachine.py
# Author's Name: Zach Rogers
# Last Modified By: Zach Rogers
# Date Last Modified: Tuesday May 23, 2013
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module

  Version: 0.1 - * Created Back end functions for the slot machine program Reels, pullthehandle, and
                 is_number (a validation function).
                 * Text output provides debugging information to check if the Slot Machine program does
                 what it's supposed to do.
                 * Used research from the internet to set the Reels function to simulate basic slot reels
"""


# import statements
import random
from Tkinter import *

class MyApp():
    
    #define the attributes of the class
    def __init__(self, parent):
        self.myParent = parent
        #creates a frame whose parent is root
        self.myContainer1 = Frame(parent)
        
        self.myContainer1.configure()
        #pack the frame - show it on the screen
        self.myContainer1.pack()
        self.maxBet = 100
        self.money = 10
        
        
        self.labelReal1 = Label(self.myContainer1)
        self.labelReal1.configure(text = "Reel One")
        self.labelReal1.pack()
        
        self.labelReal2 = Label(self.myContainer1)
        self.labelReal2.configure(text = "Reel Two")
        self.labelReal2.pack()
        
        self.labelReal3 = Label(self.myContainer1)
        self.labelReal3.configure(text = "Reel Three")
        self.labelReal3.pack()
        
        self.labelForMoney = Label(self.myContainer1)
        self.labelForMoney.configure(text = "My Money: ")
        self.labelForMoney.pack()
        
        self.CurrentMoneys = 1000
        
        self.labelMoneys = Label(self.myContainer1)
        self.labelMoneys.configure(text = str(self.CurrentMoneys))
        self.labelMoneys.pack()
        
        
        
        self.labelForBet = Label(self.myContainer1)
        self.labelForBet.configure(text = "My Bet: ")
        self.labelForBet.pack()
        
        
        
        self.label1 = Label(self.myContainer1)
        self.label1.configure(text = self.money)
        self.label1.pack()
        
        
        
        #bet 10 button
        self.button1 = Button(self.myContainer1)
        self.button1.configure(text='10', background='green')
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click)
        
        
        '''self.myimage = PhotoImage(file="Desert.gif")'''
        #bet 20 button
        self.button2 = Button(self.myContainer1)
        self.button2.configure(text='20')  
        '''i mage=self.myimage '''
        self.button2.pack(side=LEFT)
        self.button2.bind("<Button-1>", self.button2Click)
        
        # bet 50 button
        self.button3 = Button(self.myContainer1)
        self.button3.configure(text = '50', background='green')
        self.button3.pack(side=RIGHT)
        self.button3.bind("<Button-1>", self.button3Click)
        
        #max bet button
        
        self.button4 = Button(self.myContainer1)
        self.button4.configure(text='max bet', background='red')
        self.button4.pack(side=RIGHT)
        self.button4.bind("<Button-1>", self.button4Click)
        
        
        '''
        #Wins Label
        self.labelForWins = Label(self.myContainer1)
        self.labelForWins.configure(text='Wins: ')
        self.labelForWins.pack()
        
        self.labelWins = Label(self.myContainer1)
        self.labelWins.configure(text = str(self.wins))
        self.labelWins.pack()
        
        #Losses Label
        
        self.labelForLosses = Label(self.myContainer1)
        self.labelForLosses.configure(text='Losses: ')
        self.labelForLosses.pack()
        
        self.labelLosses = Label(self.myContainer1)
        self.labelLosses.configure(text = str(self.losses))
        self.labelLosses.pack()
        
        #Jackpot Label
        self.labelForJack = Label(self.myContainer1)
        self.labelForJack.configure(text='Jackpot: ')
        self.labelForJack.pack()
        
        self.labelJack = Label(self.myContainer1)
        self.labelJack.configure(text = str(self.Jack))
        self.labelJack.pack()
        '''
        #Reset Button
        self.buttonReset = Button(self.myContainer1)
        self.buttonReset.configure(text = 'Reset')
        self.buttonReset.pack()
        self.buttonReset.bind("<Button-1>", self.ButtonResetClick)
        
        
        #Spin Button
        self.buttonSpin = Button(self.myContainer1)
        self.buttonSpin.configure(text = 'Spin!')
        self.buttonSpin.pack()
        self.buttonSpin.bind("<Button-1>", self.ButtonSpinClick)
        
        
    
    def ButtonSpinClick(self, event):
        Fruits = Reels()
        
        
    def ButtonResetClick(self, event):
        self.newMoney = 1000
            
        self.labelMoneys.configure(text = str(self.newMoney))
        
        #reset the labels for spins
        
        
        self.money = self.newMoney
        
        return self.money
    
        
        
        
    def button1Click(self, event):
        
        if (self.money != self.maxBet):
            self.newMoney = self.money + 10
            
            self.label1.configure(text = str(self.newMoney))
            
            self.money = self.newMoney
            return self.money
        else:
            self.newMoney = self.money
            self.label1.configure(text = str(self.newMoney))
            self.money = self.newMoney
            return self.money
    
    def button2Click(self, event):
        
        if (self.money != self.maxBet):
            self.newMoney = self.money + 20
            
            self.label1.configure(text = str(self.newMoney))
            
            self.money = self.newMoney
            return self.money
        else:
            self.newMoney = self.money
            self.label1.configure(text = str(self.newMoney))
            self.money = self.newMoney
            return self.money
    
    
    def button3Click(self, event):
        if (self.money != self.maxBet):
            self.newMoney = self.money + 50
            
            self.label1.configure(text = str(self.newMoney))
            
            self.money = self.newMoney
            return self.money
        else:
            self.newMoney = self.money
            self.label1.configure(text = str(self.newMoney))
            self.money = self.newMoney
            return self.money
            
            
    def button4Click(self, event):
        self.newMoney = self.maxBet
        
        self.label1.configure(text = str(self.newMoney))
        self.money = self.newMoney
        return self.money
    
            
        '''if (self.mytext == 'clicky'):
            
            self.mytext = 'hello'
            self.label1.configure(text=self.mytext)
            self.label1.pack()
        else:
            self.mytext = 'clicky'
            self.label1.configure(text=self.mytext)
            self.label1.pack()
            
          if __name__ == "__main__": main()  
    
   def Reels(self, event):
        self.Bet_Line = [" "," "," "]
        self.Outcome = [0,0,0]
        for self.spin in range(3):
    # Spin those reels
            if self.Outcome[spin] >= 1 and self.Outcome[spin] <=26:   # 40.10% Chance
                self.Bet_Line[spin] = "Blank"
            if self.Outcome[spin] >= 27 and self.Outcome[spin] <=36:  # 16.15% Chance
                self.Bet_Line[spin] = "Grapes"
            if self.Outcome[spin] >= 37 and self.Outcome[spin] <=45:  # 13.54% Chance
                self.Bet_Line[spin] = "Banana"
            if self.Outcome[spin] >= 46 and self.Outcome[spin] <=53:  # 11.98% Chance
                self.Bet_Line[spin] = "Orange"
            if self.Outcome[spin] >= 54 and self.Outcome[spin] <=58:  # 7.29%  Chance
                self.Bet_Line[spin] = "Cherry"
            if self.Outcome[spin] >= 59 and self.Outcome[spin] <=61:  # 5.73%  Chance
                self.Bet_Line[spin] = "Bar"
            if self.Outcome[spin] >= 62 and self.Outcome[spin] <=63:  # 3.65%  Chance
                self.Bet_Line[spin] = "Bell"  
            if self.Outcome[spin] == 64:                         # 1.56%  Chance
                self.Bet_Line[spin] = "Seven"   
                self.Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
            

    
        return self.Bet_Line     
'''

def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    

    
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False


def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("Banana") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = Bet*40,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = Bet*200,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("Banana") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win


def main():
    
        #create a top-level window
    root = Tk()
    #call the MyApp class
    myapp = MyApp(root)
    #execute the mainloop method of the "root" object
    root.mainloop()
    
    
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    # Flag to initiate the game loop
    KeepGoing = True
    
    while KeepGoing == True:
        win = 0
        # Give the player some money if he goes broke
        if Player_Money <1:
            input("You have no more money. Here is $500 \nPress Enter\n")
            Player_Money = 500
        
        # User Input
        Prompt = raw_input(" Place Your Bet ! \n Jackpot $ " + str(Jack_Pot) + "\n Money $ " + str(Player_Money) + "\n Q = quit \n")
        if Prompt  == "q" or Prompt  == "Q":
            KeepGoing = False
            break
        
        if Prompt == "" and Turn >1:
            Bet = Prev_Bet
            print("Using Previous Bet")
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        elif is_number(Prompt ):
            Bet = int(Prompt )
            # not enough money
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
                
            # Let's Play
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        # determine win/loss ratio for debugging purposes
        if win:
            win_number += 1
        else:
            loss_number += 1
        win_ratio = "{:.2%}".format(win_number / Turn)
        print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
                
    
    #The End
    print("- Program Terminated -")
    
if __name__ == "__main__": main()