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

        Label(self, text='Welcome to the data analysis section!', font=('Helvetica', 20)).grid(sticky='W', row=0, column=1, columnspan=2)

        self.file_name_lbl = Label(self, text='Which csv data file do you want to run data analysis on?', wraplength=400)
        self.file_name_lbl.grid(sticky='W', row=1, column=1)

        self.select_files_button = Button(self, text='Select File Here', command=self.open_files)
        self.select_files_button.grid(sticky='W', row=1, column=2)

        Label(self, text='').grid(row=2, column=1)

    def import_df(self):
        self.data_frame = pd.read_csv(self.import_file_path)
        self.options = list(self.data_frame)

        Label(self, text='Please choose the two samples below: ').grid(sticky='W', row=3, column=1)
        self.render_sample_button()

    def open_files(self):
        self.import_file_path = askopenfilename(parent=self, title='Choose a file')
        self.import_df()

    def ind_t_test(self):
        self.data_frame = pd.read_csv('BVP_Variance.csv')
        print(self.data_frame)
        print('running test')
        self.results = stats.ttest_ind(self.data_frame['bvp_easy'], self.data_frame['bvp_hard'])
        print(self.results)
        self.render_ind_t_test_result(self.results)

    def render_ind_t_test_result(self, result):
        Label(self, text='Indepedent t-test result: ').grid(sticky='W', row=10, column=1)
        Label(self, text='t=' + str(result[0]) + ',  p value=' + str(result[1])).grid(row=10, column=1)
        if result[1] < 0.05:
            Label(self, text='*Result is significant*').grid(row=11, column=2)
        else:
            Label(self, text='Result is not significant').grid(row=11, column=2)

    def paired_t_test(self):
        self.data_frame = pd.read_csv('BVP_Variance.csv')
        print(self.data_frame)
        print('running test')
        self.results_paired = stats.ttest_rel(self.data_frame['bvp_easy'], self.data_frame['bvp_hard'])
        print(self.results_paired)
        self.render_paired_t_test_result(self.results_paired)

    def render_paired_t_test_result(self, result):
        Label(self, text='Paired t-test result: ').grid(sticky='W', row=10, column=1)
        Label(self, text='t=' + str(result[0]) + ',  p value=' + str(result[1])).grid(row=11, column=1)
        if result[1] < 0.05:
            Label(self, text='*Result is significant*').grid(row=11, column=2)
        else:
            Label(self, text='Result is not significant').grid(row=11, column=2)

    def render_test_buttons(self):
        Label(self, text='Please choose a test below:').grid(sticky='W', row=7, column=1)
        self.ind_t_test_button = Button(self, text='Independent T-test (independent samples)', command=self.ind_t_test)
        self.paired_t_test_button = Button(self, text='Paired T-test (dependent samples)', command=self.paired_t_test)

        self.ind_t_test_button.grid(sticky='W', row=8, column=1)
        self.paired_t_test_button.grid(sticky='W', row=8, column=2)
        Label(self, text='').grid(row=9, column=1)

    def render_sample_button(self):
        Label(self, text='Sample 1').grid(sticky='W', row=4, column=1)
        self.sample_var1 = StringVar()
        dropdown1 = OptionMenu(self, self.sample_var1, *list(self.data_frame), command=self.update_sample1)
        dropdown1.grid(sticky='W', row=4, column=2)
        menu1 = dropdown1["menu"]
        menu1.delete(0, 'end')
        for col in self.options:
            menu1.add_command(label=col, command=lambda value=col: self.sample_var1.set(value))

        Label(self, text='Sample 2').grid(sticky='W', row=5, column=1)
        self.sample_var2 = StringVar()
        dropdown2 = OptionMenu(self, self.sample_var2, *list(self.data_frame), command=self.update_sample2)
        dropdown2.grid(sticky='W', row=5, column=2)
        menu2 = dropdown2["menu"]
        menu2.delete(0, 'end')
        for col in self.options:
            menu2.add_command(label=col, command=lambda value=col: self.sample_var2.set(value))

        Label(self, text='').grid(row=6, column=1)

        self.render_test_buttons()

    def update_sample1(self, selection):
        print('sample1: ' + selection)

    def update_sample2(self, selection):
        print('sample2: ' + selection)

