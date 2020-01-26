import json

"""
 Question class with attributes associate with each question
"""

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
print(QBank[0].content)

