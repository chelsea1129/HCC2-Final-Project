from tkinter import *
from tkinter.filedialog import askopenfilenames
from Step import Step
import ntpath

class MergeFiles(Step):
    def __init__(self, parent, data, stepname):
        super().__init__(parent, data, stepname)

        self.col_list = []

        self.select_files = Label(self, text='Please select the CSV files you want to merge '
                                             '(press shift to select multiple lines):', wraplength=400)
        self.select_files.pack()

        self.select_files_button = Button(self, text='Select', command=self.open_files)
        self.select_files_button.pack()

    def open_files(self):
        filez = askopenfilenames(parent=self, title='Choose a file')
        file_dir_list = list(filez)
        for dir in file_dir_list:
            name_string = ntpath.basename(dir)
            self.col_list.append(name_string[:-4])

