from tkinter import Tk, Label, Radiobutton, Button, StringVar, Entry, Scale, IntVar, END, W, E, HORIZONTAL, LEFT, Frame, SUNKEN

from Step import Step

# A wizard step for testing purposes (Run Wizard.py)

class DemoStep(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)

        header = Label(self, text="This is a wizard step " + " " + self.stepname, bd=2, relief="groove")
        header.pack(side="top", fill="x")

        self.data[self.stepname]["demo"] = "DEMO STEP"
