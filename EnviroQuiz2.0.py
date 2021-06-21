# Cameron Galbraith
# EnviroQuiz
from appJar import gui
import random
"""
Enviromental quiz V3.0
Get all questions frames going
"""
#variables
quiz_progress = 0
question_db = []



def press(button):
    global quiz_progress

    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("questions")
    if button == 4:
        print("Correct")
        quiz_progress += 1


# class definitions
class Question:
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    # returns True if correct answer is selected
    def check_correct(self, selected_answer):
        _correct = True
        return _correct

    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        _answer_array.append(self.correct_answer)
        return _answer_array

    # returns the answer text
    def get_question_text(self):
        return self.question


def close_quiz(self):
    pass


#lists of question and the answer and possbile answers
question_db.append(Question("How many tons of rubbish just sits on top of the ocean?",["221,000 Tons","237,000 Tons","246,000 Tons"],"269,000 Tons"))
question_db.append(Question("What is the capital of Russia?",["Kazikstan","Bejing","Kiev"],"Moscow"))
question_db.append(Question("What is Russias national Animal?",["Bird","Dog","Cat"],"Eurasian brown bear"))

# create a GUI variable called app
app = gui("Enviro Quiz", "800x500")
app.setBg("DarkSlateGray4")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame("welcome"):
    app.addLabel("Enviro Quiz", colspan= 4, row = 0, column= 0)
    app.addLabel("Welcome to the environment quiz press Start to advance", colspan=4, row=3, column=0)
    app.setLabelBg("Enviro Quiz", "blue")
    app.addButton("Start Quiz",press, colspan=1, row=7, column=3)
    app.addButton("Close", close_quiz, colspan=1, row=7, column=0)
#adds buttons and then sets them
with app.frame("questions"):
    app.addLabel("question_label","")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButton(1,press)
    app.addButton(2,press)
    app.addButton(3,press)
    app.addButton(4,press)
    app.addButton("Skip", close_quiz, colspan=1, row=7, column=3)
    possible_answers = question_db[quiz_progress].get_answer_array()
    i = 1
    for option in possible_answers:
        app.setButton(i,option)
        i+=1



app.hideFrame("questions")
# start the GUI
app.go()
