# Source File Name: slotmachine.py
# Author's Name: Zach Rogers
# Last Modified By: Zach Rogers
# Date Last Modified: Tuesday June 6th, 2013
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module

  Version: 0.2- * Not connected with slotmachine.py yet.  This was simply understanding tkinter andn usign the
  buttons to alter labels.
"""




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
        
        
        self.labelForBet = Label(self.myContainer1)
        self.labelForBet.configure(text = "My Bet: ")
        self.labelForBet.pack()
        self.maxBet = 100
        self.money = 10
        self.mytext = str(self.money)
        
        self.label1 = Label(self.myContainer1)
        self.label1.configure(text = self.mytext)
        self.label1.pack()
        
        
        
        #bet 10 button
        self.button1 = Button(self.myContainer1)
        self.button1.configure(text='10', background='green')
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click)
        
        
        self.myimage = PhotoImage(file="Desert.gif")
        #bet 20 button
        self.button2 = Button(self.myContainer1)
        self.button2.configure(image=self.myimage)
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
            
            '''
        
def main():
    #create a top-level window
    root = Tk()
    #call the MyApp class
    myapp = MyApp(root)
    #execute the mainloop method of the "root" object
    root.mainloop()

if __name__ == "__main__": main()