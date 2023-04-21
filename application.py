"""
Assignment: Final Project
Date: 4_21_23

Colin Clifford - Group Leader, Database, Navigator
Chima Okere - Database, Debugger/Tester
Ken Nguyen - UI/GUI, Debugger/Tester
Zhen Zhou - Navigator, UI/GUI

Create an application where users are able to create/edit an account 
and store contact information through a user interface. This application 
will allow users to have an organized database of their contacts, 
allowing users to not have to frantically look for a specific contact. 
They would have all their contact information with a click of a few buttons.

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.createWidgets()

    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text='Hello World') #create attribute
        self.mondialLabel.config(bg = "#00ffff") #give it unique properties
        self.mondialLabel.grid() #place it on grid


        self.quitButton = tk.Button(self, text='Quit', command = add_number)
        self.quitButton.grid()

def present_contact(self):
    self.numberLabel.config(text = return_contact_name)
    
class ContactBook:
    def return_contact_name(self):
        # theres a whole process where we have to pass in some value and return a name based on what we pass in
        
        return "Name"

def add_number():
    print(5)

if __name__ == '__main__':
app = Application()
app.master.title('Sample application')
app.mainloop()
