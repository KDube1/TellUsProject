
import json
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('800x500')

style = Style()
root.configure(background='white')


style.configure('TButton', font= ('calibri', 10), foreground='black')

lbl = Label(root, text="Telus Challenge", font=("Arial Bold", 30), background = 'white')

lbl.place(relx= 0.32, rely = 0.03)


quitBtn = Button(root, text='Quit', style='TButton', command=root.destroy)

quitBtn.place(relx=0.87,rely=0.93)


btnQ1 = Button(root, text='Placeholder', command=None)
btnQ1.place(relx = 0.17, rely = 0.5)

btnQ2 = Button(root, text='Placeholder2', command=None)
btnQ2.place(relx = 0.45, rely = 0.5)

btnQ1 = Button(root, text='Placeholder3', command=None)
btnQ1.place(relx = 0.73, rely = 0.5)

questionLbl = Label(root, text="The question would go here", font=("Arial", 20), background = 'white')
questionLbl.place(relx= 0.3,rely=0.3)

root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='conU.png'))

QBank = []
threhold = 20

class user:
    point = 0
    terminate = False

    def __init__(self, geog):
        self.geog = geog

    def updatePoint(self, point):
        self.point += point
        if self.point >= threhold:
            terminate = True

    def diagnose(self):
        """
        TODO: DIAGNOSE THE SYMTOMS
        """


class Question:
    content = ""
    options = []
    weights = []

    def __init__(self, content, options, weights):
        self.content = content
        self.options = options
        self.weights = weights

# Function to initialize question bank by reading JSON file and put into Question object
def readQuestion():
    with open('QuestionBank/input.json', 'r') as data:
        data = json.load(data)
        data = data["questions"]

    for eachQ in data:
        temp = Question(eachQ["content"], eachQ["options"], eachQ["weightDist"])
        QBank.append(temp)


readQuestion()



root.mainloop()

