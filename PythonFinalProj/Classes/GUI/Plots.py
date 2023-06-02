import tkinter as tk

# Add plots for showing daily basis calories within a month
# Add some example data as it works only for the current day
class Plots(tk.Toplevel):
    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)
        self.title("Monthly progress")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image
