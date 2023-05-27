import tkinter as tk
from tkinter import messagebox


class ProductInputWindow(tk.Toplevel):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.productCarbohydrates = None
        self.productFat = None
        self.productProtein = None
        self.productCal = None
        self.productName = None
        self.title("Product input")
        self.geometry("500x400")

    # Create TextFields for user input
    def textFields(self):
        # Product Name
        self.productName = tk.Entry(self)
        self.productName.pack()

        self.productCal = tk.Entry(self)
        self.productCal.pack()

        self.productProtein = tk.Entry(self)
        self.productProtein.pack()

        self.productFat = tk.Entry(self)
        self.productFat.pack()

        self.productCarbohydrates = tk.Entry(self)
        self.productCarbohydrates.pack()

    # display input remake it later on, so it will input this into database of certain user
    def inputUser(self):
        messagebox.showinfo("Name: {}, Calories {}, Protein{}, Fat{}, Carbohydrates{}"
                            .format(self.productName, self.productCal, self.productProtein,
                                    self.productFat, self.productCarbohydrates))
