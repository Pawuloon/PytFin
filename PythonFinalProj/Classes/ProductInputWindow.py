import tkinter as tk
from tkinter import messagebox

from PythonFinalProj.Classes.DataBase import DataBase


class ProductInputWindow(tk.Toplevel):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.sub = None
        self.productCarbohydrates = None
        self.productFat = None
        self.productProtein = None
        self.productCal = None
        self.productName = None
        self.title("Product input")
        self.geometry("500x400")
        self.setBackground()
        self.textFields()
        self.initializeDataBase()

    # Create TextFields for user input
    def textFields(self):
        # Product Name
        labelName = tk.Label(self, text="Product name", font="Arial", bg="yellow")
        labelName.pack()
        self.productName = tk.Entry(self)
        self.productName.pack()

        labelCal = tk.Label(self, text="Calories", font="Arial", bg="yellow")
        labelCal.pack()
        self.productCal = tk.Entry(self)
        self.productCal.pack()

        labelProtein = tk.Label(self, text="Protein", font="Arial", bg="yellow")
        labelProtein.pack()
        self.productProtein = tk.Entry(self)
        self.productProtein.pack()

        labelFat = tk.Label(self, text="Fat", font="Arial")
        labelFat.pack()
        self.productFat = tk.Entry(self)
        self.productFat.pack()

        labelCarbo = tk.Label(self, text="Carbohydrates", font="Arial", bg="yellow")
        labelCarbo.pack()
        self.productCarbohydrates = tk.Entry(self)
        self.productCarbohydrates.pack()

        self.sub = tk.Button(self, text="Enter Product", command=self.inputUser, bg="yellow")
        self.sub.pack()

    # display input remake it later on, so it will input this into database of certain user
    @staticmethod
    def inputUser():
        messagebox.showinfo("Info", "Product has been added !!!")

    @staticmethod
    def initializeDataBase():
        data = DataBase()
        data.conn()

    def addToDataBase(self):
        pass

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image
