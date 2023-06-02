import tkinter as tk
from tkinter import ttk

from PythonFinalProj.Classes.DataBase.DataBase import DataBase


# Window for accessing your own diet
class DietWindow(tk.Toplevel):

    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)
        self.selection = tk.StringVar()
        self.optionVariable = None
        self.geometry("500x400")
        self.title("Your Daily Diet!")
        self.resizable(False, False)
        self.setBackground()
        self.data()
        self.buttons()

    def data(self):
        pass

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image

    def selection_get(self, *args):
        currSelection = self.optionVariable.get()
        self.selection.set(currSelection)

    def confirm(self):
        pass

    def buttons(self):
        listOfProducts = DataBase().getProducts()

        # Breakfast
        label = tk.Label(self, text="Breakfast", font="Arial", bg='yellow', width=70, height=5)
        label.pack()

        self.selection.set(listOfProducts[0])

        self.optionVariable = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable, *listOfProducts, command=self.selection_get)
        option.pack()

        # Lunch
        label = tk.Label(self, text="Lunch", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable, *listOfProducts, command=self.selection_get)
        option.pack()

        # Dinner
        label = tk.Label(self, text="Dinnner", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable, *listOfProducts, command=self.selection_get)
        option.pack()

        finalConf = tk.Button(self, text="Confirm", width=30, height=2, command=self.confirm, bg='yellow')
        finalConf.pack()
        # choiceBox = tk.Listbox(self, width=30, height=5)
        # for product in listOfProducts:
        #     choiceBox.insert(tk.END, product)
        # choiceBox.pack(side=tk.TOP, fill=tk.BOTH)
        #
        # scroll = tk.Scrollbar(self, command=choiceBox.yview)
        # scroll.pack(side=tk.RIGHT, fill=tk.Y)
        # choiceBox.config(yscrollcommand=scroll.set)
