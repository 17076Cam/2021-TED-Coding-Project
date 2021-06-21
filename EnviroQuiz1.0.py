# Environment GUI quiz
# Cameron Galbraith
# Version 1.0
"""

make a program that can quiz the user
@copyright 2021 Cameron Galbraith <17076@rangiorahigh.school.nz>
"""
# imports
from appJar import gui



# variables

# class
class GUI:
    # Create GUI
    def __init__(self):
        app = gui("Enviro Quiz", "800x500")
        app.setBg("DarkSlateGray4")
        app.setFont(18)
        with app.frame("Main"):
            app.addLabel("Enviro Quiz", colspan= 4, row = 0, column= 0)
            app.setLabelBg("Enviro Quiz", "blue")
            app.addButton("Start", self.start_quiz, colspan=1, row=7, column=3)
            app.addButton("Close", self.close_quiz, colspan=1, row=7, column=0)
            app.setAllButtonWidths(7)

        with app.frame("questions"):
            app.addLabel("Question here", colspan=4, row=0, column=0)
            app.hideFrame("questions")





    def start_quiz(self):
        self._app.hideFrame("Main")
        self._app.showFrame("questions")

    def close_quiz(self):
        pass

# main
self._app = app
self._app.go()





window = GUI()
window.start.app()


#can add later
'''
app.addMeter("progress")
app.setMeterFill("progress", "blue")
'''
