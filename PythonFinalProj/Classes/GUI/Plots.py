import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Add plots for showing daily basis calories within a month
# Add some example data as it works only for the current day
class Plots(tk.Toplevel):
    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)
        self.title("Monthly progress")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()
        self.addPlots()

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image


    def addPlots(self):
        fig = Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(111)
        plot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2000, 1500, 1000, 500, 0, 0, 0, 0, 0, 0])
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
