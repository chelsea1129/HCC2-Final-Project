from tkinter import *
from tkinter.filedialog import askopenfilenames
from Step import Step
from Wizard import Wizard

from MergingFiles import MergeFiles


class finalWizard(Wizard):
    def __init__(self, parent, data):
        super().__init__(parent, data)

        steps = [MergeFiles(self, self.data, 'mergeFiles')]

        self.set_steps(steps)
        self.start()

if __name__ == "__main__":
    root = Tk()

    data = {}
    final_gui = finalWizard(root, data)
    final_gui.pack()

    root.mainloop()
