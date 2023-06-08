import tkinter as tk
from tkinter import messagebox

import numpy as np

"""
This Class is responsible for creating the BMI window
it allows user to calculate his BMI
"""


class BmiWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master=master)
        self.heightEntry = None
        self.weightEntry = None
        self.geometry("500x400")
        self.title("BMI Calculator")
        self.resizable(False, False)
        self.setBackground()
        self.bmiDisp()

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image

    # Bmi calculations
    def bmiCalc(self):
        bmi = float(self.weightEntry.get()) / np.square(float(self.heightEntry.get()) / 100)
        messagebox.showinfo("BMI", "Your BMI is: " + str(bmi))
        self.destroy()

    # Bmi display
    def bmiDisp(self):
        weightLabel = tk.Label(self, text="Enter your weight in kg: ")
        weightLabel.place(x=0, y=0, anchor=tk.CENTER)
        weightLabel.pack()

        self.weightEntry = tk.Entry(self, width=20, bg="yellow")
        self.weightEntry.place(x=5, y=5, anchor=tk.CENTER)
        self.weightEntry.pack()

        heightLabel = tk.Label(self, text="Enter your height in cm: ")
        heightLabel.place(x=10, y=10, anchor=tk.CENTER)
        heightLabel.pack()

        self.heightEntry = tk.Entry(self, width=20, bg="yellow")
        self.heightEntry.place(x=15, y=15, anchor=tk.CENTER)
        self.heightEntry.pack()

        calcButton = tk.Button(self, text="Calculate", width=30, height=3, command=self.bmiCalc, bg="yellow")
        calcButton.place(x=20, y=20, anchor=tk.CENTER)
        calcButton.pack()
