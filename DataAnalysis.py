from tkinter import *
from tkinter.filedialog import askopenfilename
from Step import Step
from scipy import stats

import pandas as pd
import numpy as np

class Analysis(Step):
    def __init__(self, parent, stepname):
        super().__init__(parent, stepname)

        self.csv_name = ''
        self.import_file_path = ''
        self.data_frame = pd.DataFrame()
        self.options = []
        self.sample1 = ''
        self.sample2 = ''

        self.file_name_lbl = Label(text='Which csv data file do you want to run data analysis with?', wraplength=400)
        self.file_name_lbl.pack()


        self.select_files_button = Button(self, text='Select File Here', command=self.open_files)
        self.select_files_button.pack()

        self.ind_t_test_button = Button(self, text='Independent T-test (independent samples)', command=self.ind_t_test)
        self.ind_t_test_button.pack()

        Label(text='Please choose the two samples below: ').pack()

        # Label(text='Sample 1: ').pack()
        # self.sample_var = StringVar()
        # self.dropdown = OptionMenu(self, self.sample_var, list(self.data_frame))
        # self.dropdown.pack()
        #
        # Label(text='Sample 2: ').pack()
        # self.sample2_var = StringVar()
        # self.dropdown2 = OptionMenu(self, self.sample2_var, list(self.data_frame))
        # self.dropdown2.pack()
        #
        # self.render_sample_button(1)
        # self.render_sample_button(2)

    def import_df(self):
        self.data_frame = pd.read_csv(self.import_file_path)
        self.options = list(self.data_frame)
        # menu = self.dropdown["menu"]
        # menu.delete(0, 'end')
        # for col in self.options:
        #     menu.add_command(label=col, command=lambda value=col: self.sample_var.set(value))

        Label(text='Please choose the two samples below: ').pack()
        self.render_sample_button(1)

    def open_files(self):
        self.import_file_path = askopenfilename(parent=self, title='Choose a file')
        self.import_df()

    def ind_t_test(self):
        stats.ttest_ind()

    def render_sample_button(self, sample_num):
        # Label(text='Sample ' + str(sample_num)).pack()
        # sample_var = StringVar()
        # dropdown = OptionMenu(self, sample_var, list(self.data_frame))
        # dropdown.pack()
        #
        # menu = dropdown["menu"]
        # menu.delete(0, 'end')
        # for col in self.options:
        #     menu.add_command(label=col, command=lambda value=col: sample_var.set(value))
        #
        # if sample_num == self.sample1:
        #     self.sample1 = sample_var.get()
        #     print('sample1 = ', self.sample1)
        # elif sample_num == self.sample2:
        #     self.sample2 = sample_var.get()
        #     print('sample2 = ', self.sample2)

        Label(text='Sample 1').pack()
        sample_var1 = StringVar()
        dropdown1 = OptionMenu(self, sample_var1, list(self.data_frame))
        dropdown1.pack()
        menu1 = dropdown1["menu"]
        menu1.delete(0, 'end')
        for col in self.options:
            menu1.add_command(label=col, command=lambda value=col: sample_var1.set(value))

        Label(text='Sample 2').pack()
        sample_var2 = StringVar()
        dropdown2 = OptionMenu(self, sample_var2, list(self.data_frame))
        dropdown2.pack()
        menu2 = dropdown2["menu"]
        menu2.delete(0, 'end')
        for col in self.options:
            menu2.add_command(label=col, command=lambda value=col: sample_var2.set(value))
