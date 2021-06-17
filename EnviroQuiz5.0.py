# Cameron Galbraith
# EnviroQuiz
from appJar import gui
import random
"""
Enviromental quiz V5.0
Get all questions frames going
"""
#variables
quiz_progress = -1
question_db = []
progress_bar = -10
score = 0
correct_ans = 0
correct_ann = []

def press(button):
    global quiz_progress
    global progress_bar
    global score
    global correct_ans
    global correct_ann
    if button == "Start Quiz":
        app.hideFrame("welcome")
        app.showFrame("questions")
    correct_ans = correct_ann[quiz_progress]
    if button == correct_ans:
        quiz_progress += 1
        progress_bar += 10
        score += 1
        correct_ans = correct_ann[quiz_progress]
        app.setMeter("progress", (progress_bar), text=None)
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        print(score)
        i = 1
        for option in possible_answers:
            app.setButton(i, option)
            i += 1
    else:
        quiz_progress += 1
        progress_bar += 10
        app.setMeter("progress", (progress_bar), text=None)
        app.setLabel("question_label",question_db[quiz_progress].get_question_text())
        possible_answers = question_db[quiz_progress].get_answer_array()
        print(score)
        i = 1
        for option in possible_answers:
            app.setButton(i, option)
            i += 1
    if quiz_progress == 10:
        app.hideFrame("questions")
        app.showFrame("end_screen")
        app.addLabel("Congratulations you finsihed", colspan=4, row=0, column=0)
        app.addLabel("You scored: %d" % score, colspan=4, row=1, column=0)



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

# runs if you click close at the start of the quiz and closes program
def close_quiz(self):
    app.stop()
# skip button runs if user clicks it same as answering a wrong asnwer
def skip_question(self):
    global quiz_progress
    global progress_bar
    global score
    quiz_progress += 1
    progress_bar += 10
    app.setMeter("progress", (progress_bar), text=None)
    app.setLabel("question_label", question_db[quiz_progress].get_question_text())
    possible_answers = question_db[quiz_progress].get_answer_array()
    print(score)
    i = 1
    for option in possible_answers:
        app.setButton(i, option)
        i += 1
    if quiz_progress == 10:
        app.hideFrame("questions")
        app.showFrame("end_screen")
        app.addLabel("Congratulations you finsihed", colspan=4, row=0, column=0)
        app.addLabel("You scored: %d" % score, colspan=4, row=1, column=0)

# list of question and the answer and possbile answers
question_db.append(Question("How many tons of rubbish just sits on top of the ocean?",["269,000 Tons","272,000 Tons","282,000 Tons,"],"295,000 Tons"))
question_db.append(Question("One average how many paper bags does supermarket go through a year?",["40 Million","50 Million","60 Million"],"70 Million"))
question_db.append(Question("How many Styrofoam cups do Americans throw away each year?",["20 Trillion","25 Trillion","30 Trillion"],"35 Trillion"))
question_db.append(Question("How long can a glass take to decompose?",["1500 Years","2000 Years","3000 Years"],"4000 Years"))
question_db.append(Question("Around what rate are rain forests being cut down at per minute?",["70 Acres","80 Acres","90 Acres"],"100 Acres"))
question_db.append(Question("Around how many trees are cut down each day just for toilet paper?",["27,000","32,000","37,000"],"42,000"))
question_db.append(Question("Recycling one aluminum can save enough energy to run a TV for how long?",["45 Minutes","2 Hour","3 Hours"],"4 Hours"))
question_db.append(Question("What per cent of marine mammals are threatened by accidental deaths?",["78%","80%","82%"],"84%"))
question_db.append(Question("Roughly how many hectares of mangroves are lost every year?",["600,000","700,000","800,000"],"900,000"))
question_db.append(Question("What percent of bottled water is just tap water?",["10%","20%","30%"],"40%"))
question_db.append(Question("New answer can be inputed here",["Answer1","Answer2","Answer3"],"Answer4"))
question_db.append(Question("Another new answer can be inputed here",["Answer1","Answer2","Answer3"],"Answer4"))

# list of places of correct answers
correct_ann.append(1)
correct_ann.append(3)
correct_ann.append(2)
correct_ann.append(4)
correct_ann.append(4)
correct_ann.append(1)
correct_ann.append(3)
correct_ann.append(1)
correct_ann.append(3)
correct_ann.append(4)
correct_ann.append("Input new answer here")

# create a GUI variable called Enviro Quiz
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

# adding widgets to the end screen which shows when quiz progress is 10
with app.frame("end_screen"):
    app.addLabel("You scored", score, colspan=4, row=3, column=0)


# adds buttons and then sets them for the question frame
with app.frame("questions"):
    app.addMeter("progress", colspan=2, row=2, column=2)
    app.setMeterFill("progress", "blue")
    app.setMeter("progress", (progress_bar), text=None)
    app.addLabel("question_label","", colspan=2, row=1, column=2)
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())
    app.addButton(1,press, colspan=2, row=3, column=2)
    app.addButton(2,press, colspan=2, row=4, column=2)
    app.addButton(3,press, colspan=2, row=5, column=2)
    app.addButton(4,press, colspan=2, row=6, column=2)
    app.addButton("Skip", skip_question, colspan=1, row=7, column=3)
    correct_ans = correct_ann[quiz_progress]
    possible_answers = question_db[quiz_progress].get_answer_array()
    i = 1
    for option in possible_answers:
        app.setButton(i,option)
        i+=1


# hiding frames that arent needing to be shown at the start
app.hideFrame("questions")
app.hideFrame("end_screen")
# starts the GUI
app.go()