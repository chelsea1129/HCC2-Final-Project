from tkinter import *
from tkinter.filedialog import askopenfilenames
from Step import Step
import pandas as pd

import ntpath

class SelectingFiles(Step):
    def __init__(self, parent,stepname):
        super().__init__(parent, stepname)

        self.file_dir_list = []
        self.export_file = False
        self.export_file_name = ''
        self.csv_df_list = []

        Label(self, text='Merge CSV fiels', font=('Helvetica', 20)).grid(sticky='W', row=0, column=1, columnspan=2)
        self.select_files = Label(self, text='Please select the CSV files you want to merge '
                                             '(press shift to select multiple lines):', wraplength=400)
        self.select_files.grid(sticky='W', row=1, column=1)

        self.select_files_button = Button(self, text='Select', command=self.open_files)
        self.select_files_button.grid(row=1, column=2)

        self.empty_label = Label(self, text='')
        self.empty_label.grid(row=2, column=2)

        self.select_files = Label(self, text='Please name your merged file: ')
        self.select_files.grid(sticky='W', row=3, column=1)

        self.file_name = StringVar()
        vcmd1 = (self.register(self.update_export_name), '%P')
        self.text_box = Entry(self, textvariable=self.file_name, validate="key", validatecommand=vcmd1)
        self.text_box.grid(sticky='W', row=3, column=2)
        self.export_file_name = self.file_name.get()

        self.submit = Button(self, text='Submit', command=self.merge_export_final_file)
        self.submit.grid(row=4, column=2)

    def update_export_name(self, new_text):
        self.export_file_name = new_text
        return True

    def open_files(self):
        filez = askopenfilenames(parent=self, title='Choose a file')
        self.file_dir_list = list(filez)

    def merge_export_final_file(self):
        for f in self.file_dir_list:
            temp_df = pd.read_csv(f, header=None)
            name_string = ntpath.basename(f)
            col_name = name_string[:-4]
            temp_df.columns = [col_name]
            self.csv_df_list.append(temp_df)
        self.combined_csv = pd.concat(self.csv_df_list, sort=False, axis=1)
        self.combined_csv.to_csv(self.export_file_name, index=False)

