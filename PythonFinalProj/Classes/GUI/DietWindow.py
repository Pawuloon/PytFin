import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import re

from PythonFinalProj.Classes.DTO.MealDTO import MealDTO
from PythonFinalProj.Classes.DataBase.DataBase import DataBase
from PythonFinalProj.Classes.DTO.DietDTO import DietDTO

"""
Class responsible for the diet window
This class is responsible for the diet window
It creates the diet window and all the buttons and labels
It also creates the diet and adds it to the database
"""


class DietWindow(tk.Toplevel):

    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)

        self.selection6 = tk.StringVar()
        self.selection5 = tk.StringVar()
        self.selection4 = tk.StringVar()
        self.selection3 = tk.StringVar()
        self.selection2 = tk.StringVar()
        self.selection = tk.StringVar()

        self.optionVariable6 = None
        self.optionVariable5 = None
        self.optionVariable4 = None
        self.optionVariable3 = None
        self.optionVariable2 = None
        self.optionVariable = None

        self.myDiet = []
        self.geometry("500x400")
        self.title("Your Daily Diet!")
        self.resizable(False, False)
        self.setBackground()
        self.buttons()

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

    def selectionGet4(self, *args):
        currSelection4 = self.optionVariable4.get()
        self.selection4.set(currSelection4)

    def selectionGet5(self, *args):
        currSelection5 = self.optionVariable5.get()
        self.selection5.set(currSelection5)

    def selectionGet6(self, *args):
        currSelection6 = self.optionVariable6.get()
        self.selection6.set(currSelection6)

    def findLetters(self, string):
        pattern = r"[A-Za-z]+|\d+"
        matches = re.findall(pattern, string)
        letters = "".join([match for match in matches if match.isalpha()])
        numerals = [match for match in matches if match.isdigit()]
        return letters, numerals

    def confirm(self):
        calories = 0
        proteins = 0
        fats = 0
        carbs = 0

        name, nums = self.findLetters(self.selection.get())
        name2, nums2 = self.findLetters(self.selection2.get())
        name3, nums3 = self.findLetters(self.selection3.get())
        name4, nums4 = self.findLetters(self.selection4.get())
        name5, nums5 = self.findLetters(self.selection5.get())
        name6, nums6 = self.findLetters(self.selection6.get())

        self.myDiet.append(MealDTO(name, nums[0], nums[1], nums[2], nums[3]))
        self.myDiet.append(MealDTO(name2, nums2[0], nums2[1], nums2[2], nums2[3]))
        self.myDiet.append(MealDTO(name3, nums3[0], nums3[1], nums3[2], nums3[3]))
        self.myDiet.append(MealDTO(name4, nums4[0], nums4[1], nums4[2], nums4[3]))
        self.myDiet.append(MealDTO(name5, nums5[0], nums5[1], nums5[2], nums5[3]))
        self.myDiet.append(MealDTO(name6, nums6[0], nums6[1], nums6[2], nums6[3]))

        day = str(datetime.now().strftime("%d/%m/%Y"))
        print(day)
        cDay = str(DataBase().getDay())
        formatted = cDay[2:-3]
        print(formatted)

        for x in self.myDiet:
            calories += float(x.calories)
            proteins += float(x.protein)
            fats += float(x.fat)
            carbs += float(x.carbs)

        if formatted == day:
            DataBase().replaceDay(DietDTO(day, calories, proteins, fats, carbs))
        else:
            DataBase().addDay(DietDTO(day, calories, proteins, fats, carbs))
        messagebox.showinfo("Info", "Diet added successfully !\n"
                                    "You can now access your monthly progress !\n"
                            +
                            "\nYour daily intake is:\n" + str(calories) + " calories\n" +
                            str(proteins) + " proteins\n" +
                            str(fats) + " fats\n" +
                            str(carbs) + " carbs\n")
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

        self.optionVariable4 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable4, *listOfProducts, command=self.selectionGet4)
        option.pack()

        # Lunch
        self.selection2.set(listOfProducts[0])
        label = tk.Label(self, text="Lunch", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable2 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable2, *listOfProducts, command=self.selectionGet2)
        option.pack()

        self.optionVariable5 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable5, *listOfProducts, command=self.selectionGet5)
        option.pack()

        # Dinner
        self.selection3.set(listOfProducts[0])
        label = tk.Label(self, text="Dinnner", font="Arial", bg='yellow', width=70, height=2)
        label.pack()

        self.optionVariable3 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable3, *listOfProducts, command=self.selectionGet3)
        option.pack()

        self.optionVariable6 = tk.StringVar(self)
        option = ttk.OptionMenu(self, self.optionVariable6, *listOfProducts, command=self.selectionGet6)
        option.pack()

        # Confirm
        finalConf = tk.Button(self, text="Confirm", width=30, height=2, command=self.confirm, bg='yellow')
        finalConf.pack()
