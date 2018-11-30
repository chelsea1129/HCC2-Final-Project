from tkinter import *
from Wizard import Wizard

from MergingFiles import SelectingFiles
from DataAnalysis import Analysis
from DataGraph import Graph

class finalWizard(Wizard):
    def __init__(self, parent):
        super().__init__(parent)
        steps = [SelectingFiles(self, 'selectFiles'),
                 Analysis(self, 'analyzeData'),
                 Graph(self, 'graphData')]

        self.set_steps(steps)
        self.start()

if __name__ == "__main__":
    root = Tk()

    final_gui = finalWizard(root)
    final_gui.pack()

    root.mainloop()
