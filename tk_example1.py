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

def add_number():
    print(5)

app = Application()
app.master.title('Sample application')
app.mainloop()