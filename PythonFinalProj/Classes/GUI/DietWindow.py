import tkinter as tk


# Window for accessing your own diet
class DietWindow(tk.Toplevel):

    def __init__(self, masterWindow):
        super().__init__(master=masterWindow)
        self.title = "Your Daily Diet!"
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()
        self.data()

    def data(self):
        pass

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        background.image = image
