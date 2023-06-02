import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from PythonFinalProj.Classes.DataBase.DataBase import DataBase
from PythonFinalProj.Classes.Model.Diet import Diet


# Window for accessing your own diet
class DietWindow(tk.Toplevel):

    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)

        self.selection3 = tk.StringVar()
        self.selection2 = tk.StringVar()
        self.selection = tk.StringVar()
        self.optionVariable3 = None
        self.optionVariable2 = None
        self.optionVariable = None

        self.myDiet = []
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

    def selectionGet(self, *args):
        currSelection = self.optionVariable.get()
        self.selection.set(currSelection)

    def selectionGet2(self, *args):
        currSelection2 = self.optionVariable2.get()
        self.selection2.set(currSelection2)

    def selectionGet3(self, *args):
        currSelection3 = self.optionVariable3.get()
        self.selection3.set(currSelection3)

    def confirm(self):
        calories = 0
        proteins = 0
        fats = 0
        carbs = 0
        DataBase().clearDay()
        self.myDiet.append(str(self.selection.get()))
        self.myDiet.append(str(self.selection2.get()))
        self.myDiet.append(str(self.selection3.get()))
        day = datetime.now().strftime("%d/%m/%Y")
        print(self.myDiet)
        for x in self.myDiet:
            x = x.split(' ')
            calories += int(x[1])
            proteins += int(x[2])
            fats += int(x[3])
            carbs += int(x[4])
        DataBase().addDay(Diet(day, calories, proteins, fats, carbs))
        messagebox.showinfo("Info", "Diet added successfully !")
        self.destroy()

    def buttons(self):
        listOfProducts = DataBase().getProducts()
        # Day
        dayLabel = tk.Label(self, text=datetime.now().strftime('%A'), font="Arial", bg='yellow', width=30, height=3)
        dayLabel.pack()
        # Breakfast
        self.selection.set(listOfProducts[0])
        label = tk.Label(self, text="Breakfast", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable, *listOfProducts, command=self.selectionGet)
        option.pack()

        # Lunch
        self.selection2.set(listOfProducts[0])
        label = tk.Label(self, text="Lunch", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable2 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable2, *listOfProducts, command=self.selectionGet2)
        option.pack()

        # Dinner
        self.selection3.set(listOfProducts[0])
        label = tk.Label(self, text="Dinnner", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable3 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable3, *listOfProducts, command=self.selectionGet3)
        option.pack()

        # Confirm
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
