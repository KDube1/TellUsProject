import random
import json
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('800x500')

style = Style()
root.configure(background='white')
currentQ= random.randint(0, 14)

totalSum  =0
questionsAsked = 0

style.configure('TButton', font= ('calibri', 10), foreground='black')

lbl = Label(root, text="Telus Challenge", font=("Arial Bold", 30), background = 'white')

lbl.place(relx= 0.32, rely = 0.03)


quitBtn = Button(root, text='Quit', style='TButton', command=root.destroy)

quitBtn.place(relx=0.87,rely=0.93)


def buttonOneCallback():
    global totalSum
    global currentQ
    global questionsAsked
    totalSum+= QBank[currentQ].weights[0]
    if questionsAsked>=5:
        totalSum+= QBank[currentQ].weights[0]
        print("done")
        return
    else:
        flag = True
        while flag:
            tempVal = random.randint(0, 14)
            if (tempVal != currentQ):
                flag = False
        currentQ = tempVal
        updateQuestion(QBank[currentQ].content)
        questionsAsked+=1


def buttonTwoCallback():
    global totalSum
    global currentQ
    global questionsAsked
    totalSum+= QBank[currentQ].weights[1]
    if questionsAsked>=5:
        totalSum+= QBank[currentQ].weights[1]
        print("done")
        return
    else:
        flag = True
        while flag:
            tempVal = random.randint(0, 14)
            if (tempVal != currentQ):
                flag = False
        currentQ = tempVal
        updateQuestion(QBank[currentQ].content)
        questionsAsked+=1

def buttonThreeCallback():
    global totalSum
    global currentQ
    global questionsAsked
    totalSum+= QBank[currentQ].weights[2]
    if questionsAsked>=5:
        totalSum+= QBank[currentQ].weights[2]
        print("done")
        return
    else:
        flag = True
        while flag:
            tempVal= random.randint(0,14)
            if (tempVal!= currentQ):
                flag = False
        currentQ = tempVal
        updateQuestion(QBank[currentQ].content)
        questionsAsked+=1



btnQ1 = Button(root, text='Placeholder', command=buttonOneCallback)
btnQ1.place(relx = 0.17, rely = 0.5)

btnQ2 = Button(root, text='Placeholder2', command=buttonTwoCallback)
btnQ2.place(relx = 0.45, rely = 0.5)

btnQ3 = Button(root, text='Placeholder3', command=buttonThreeCallback)
btnQ3.place(relx = 0.73, rely = 0.5)

questionText = "The question would go here"
questionLbl = Label(root, text=questionText, font=("Arial", 12), background = 'white')
questionLbl.place(relx= 0.06,rely=0.3)

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

def updateQuestion(a):
    questionLbl.config(text=QBank[currentQ].content)
    btnQ1.config(text= QBank[currentQ].options[0])
    btnQ2.config(text= QBank[currentQ].options[1])
    btnQ3.config(text= QBank[currentQ].options[2])




readQuestion()



updateQuestion(currentQ)

root.mainloop()
