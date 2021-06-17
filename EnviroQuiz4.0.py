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
progress_bar = 0
score = 0


def press(button):
    global quiz_progress
    global progress_bar
    global score
    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("questions")
    if button == 4:
        quiz_progress += 1
        progress_bar += 10
        score += 1
        app.setMeter("progress", (progress_bar), text=None)
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        i = 1
        for option in possible_answers:
            app.setButton(i, option)
            i += 1
    if quiz_progress == 10:
        app.hideFrame("questions")
        app.showFrame("end_screen")
        app.setLabel("You scored", score, colspan=4, row=3, column=0)




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

#
def close_quiz(self):
    pass


#lists of question and the answer and possbile answers
question_db.append(Question("How many tons of rubbish just sits on top of the ocean?",["221,000 Tons","237,000 Tons","246,000 Tons,"],"269,000 Tons"))
question_db.append(Question("One average how many paper bags does supermarket go through a year?",["30 Million","40 Million","50 Million"],"60 Million"))
question_db.append(Question("How many Styrofoam cups do Americans throw away each year?",["10 Trillion","15 Trillion","20 Trillion"],"25 Trillion"))
question_db.append(Question("How long can a glass take to decompose?",["1500 Years","2000 Years","3000 Years"],"4000 Years"))
question_db.append(Question("Around what rate are rain forests being cut down at per minute?",["70 Acres","80 Acres","90 Acres"],"100 Acres"))
question_db.append(Question("Around how many trees are cut down each day just for toilet paper?",["10,000","15,000","20,000"],"27,000"))
question_db.append(Question("Recycling one aluminum can save enough energy to run a TV for how long?",["30 Minutes","1 Hour","2 Hours"],"3 Hours"))
question_db.append(Question("What per cent of marine mammals are threatened by accidental deaths?",["63%","68%","73%"],"78%"))
question_db.append(Question("Roughly how many hectares of mangroves are lost every year?",["500,000","600,000","700,000"],"800,000"))
question_db.append(Question("What percent of bottled water is just tap water?",["10%","20%","30%"],"40%"))
question_db.append(Question("New answer can be inputed here",["Answer1","Answer2","Answer3"],"Answer4"))
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


with app.frame("end_screen"):
    app.addLabel("You scored", score, colspan=4, row=3, column=0)


#adds buttons and then sets them
with app.frame("questions"):
    app.addMeter("progress")
    app.setMeterFill("progress", "blue")
    app.setMeter("progress", (progress_bar), text=None)
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
app.hideFrame("end_screen")
# start the GUI
app.go()