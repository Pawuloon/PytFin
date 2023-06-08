import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from PythonFinalProj.Classes.DataBase.DataBase import DataBase

"""
Class responsible for the plots window
This class is responsible for the plots window
It creates the plots window and all the buttons and labels
It also creates the plots and adds it to the database
Uses matplotlib to create the plots   
"""


class Plots(tk.Toplevel):
    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)
        self.title("Weekly progress")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()
        self.addPlots()

    # set the background of the window
    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image

    # add the plots to the window
    def addPlots(self):
        days = DataBase().getDiets()
        dayCalories = []
        for day in reversed(days):
            dayCalories.append(day.calories)
        fig = Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(111)
        plot.set_xlabel("Daily progress")
        plot.plot([1, 2, 3, 4, 5, 6, 7],
                  [dayCalories[0], dayCalories[1], dayCalories[2], dayCalories[3], dayCalories[4], dayCalories[5],
                   dayCalories[6]])
        plot.set_xticks(range(1, 8))
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
