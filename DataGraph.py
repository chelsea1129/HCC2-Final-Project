from tkinter import *
from tkinter.filedialog import askopenfilename
from Step import Step
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

class Graph(Step):
    def __init__(self, parent, stepname):
        super().__init__(parent, stepname)

        self.csv_name = ''
        self.import_file_path = ''
        self.data_frame = pd.DataFrame()
        self.options = []

        Label(self, text='Create Data Graphs', font=('Helvetica', 20)).grid(sticky='W', row=0, column=1)

        self.file_name_lbl = Label(self, text='Which csv data file do you want to plot?')
        self.file_name_lbl.grid(sticky='W', row=1, column=1)

        self.select_files_button = Button(self, text='Select File Here', command=self.open_files)
        self.select_files_button.grid(sticky='W', row=1, column=2)

        Label(self, text='').grid(row=2)

    def open_files(self):
        self.import_file_path = askopenfilename(parent=self, title='Choose a file')
        self.import_df()

    def import_df(self):
        self.data_frame = pd.read_csv(self.import_file_path)
        print(self.data_frame)
        self.render_plot_on_GUI()

    def render_plot_on_GUI(self):
        plt.clf()
        matplotlib.use('TkAgg')
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        plot_widget = canvas.get_tk_widget()
        ax = plt.gca()
        for col in list(self.data_frame):
            print('col is' + col)
            self.data_frame.plot(kind='line', y=col, ax=ax)
        plot_widget.grid(row=3, column=1, columnspan=4)
