import tkinter as tk
from tkinter import messagebox

from PythonFinalProj.Classes.DataBase.DataBase import DataBase

"""
This class is responsible for creating a window for user to input his product

"""


class ProductInputWindow(tk.Toplevel):
    def __init__(self, mainWindow):
        super().__init__(master=mainWindow)
        self.sub = None
        self.productCarbohydrates = None
        self.productFat = None
        self.productProtein = None
        self.productCal = None
        self.productName = None
        self.title("Product input")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()
        self.textFields()

    # Create TextFields for user input
    def textFields(self):
        # Product Name
        labelName = tk.Label(self, text="Product name", font="Arial", bg="yellow")
        labelName.pack()
        self.productName = tk.Entry(self)
        self.productName.pack()

        cal = tk.StringVar()
        labelCal = tk.Label(self, text="Calories", font="Arial", bg="yellow")
        labelCal.pack()
        self.productCal = tk.Entry(self, textvariable=cal)
        self.productCal.pack()

        prot = tk.StringVar()
        labelProtein = tk.Label(self, text="Protein", font="Arial", bg="yellow")
        labelProtein.pack()
        self.productProtein = tk.Entry(self, textvariable=prot)
        self.productProtein.pack()

        fat = tk.StringVar()
        labelFat = tk.Label(self, text="Fat", font="Arial", bg="yellow")
        labelFat.pack()
        self.productFat = tk.Entry(self)
        self.productFat.pack()

        labelCarbo = tk.Label(self, text="Carbohydrates", font="Arial", bg="yellow")
        labelCarbo.pack()
        self.productCarbohydrates = tk.Entry(self, textvariable=fat)
        self.productCarbohydrates.pack()

        self.sub = tk.Button(self, text="Enter Product", command=self.inputUser, bg="yellow")
        self.sub.pack()

    # display input remake it later on, so it will input this into database of certain user

    def inputUser(self):
        messagebox.showinfo("Info", "Product has been added !!!")
        name = self.productName.get()
        cal = self.productCal.get()
        prot = self.productProtein.get()
        fat = self.productFat.get()
        carbs = self.productCarbohydrates.get()
        self.initializeDataBase(name, cal, prot, fat, carbs)
        ProductInputWindow.destroy(self)

    # Initialize database
    def initializeDataBase(self, name=0, cal=0, prot=0, fat=0, carbs=0):
        data = DataBase()
        data.add(name, cal, prot, fat, carbs)

    # Set background
    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image
