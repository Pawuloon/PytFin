import tkinter as tk
from PIL import Image, ImageTk

from PythonFinalProj.Classes.DietWindow import DietWindow
from PythonFinalProj.Classes.Plots import Plots
from PythonFinalProj.Classes.ProductInputWindow import ProductInputWindow


class MyGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.imgName = None
        self.photo = None
        self.title("Weight Calculator")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setBackground()
        self.buttons()
        self.icon()
        self.run()

    # Set icon
    def icon(self):
        path = "../Pics/img_1.png"
        icon = Image.open(path)
        icoPath = "../Pics/IcoIcon.ico"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # Startup Image
    def image(self):
        image = Image.open("../Pics/img.png")
        image = image.resize((500, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.imgName = tk.Label(self, image=self.photo)
        self.imgName.pack()

    def setBackground(self):
        image = tk.PhotoImage(file="../Pics/img.png")
        background = tk.Label(self, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    # Buttons
    # Add new button for accessing your daily diet
    def buttons(self):
        buttonEnterProduct = tk.Button(self, text="Enter your Product", width=70, height=5,
                                       command=self.buEnClick, bg="yellow")

        buttonEnterProduct.place(x=0, y=0, anchor=tk.CENTER)
        buttonEnterProduct.pack()

        # Second button
        buttonAccessDiet = tk.Button(self, text="Access your diet", width=70, height=5,
                                     command=self.dietClick, bg='yellow')
        buttonAccessDiet.place(x=5, y=5, anchor=tk.CENTER)
        buttonAccessDiet.pack()

        # Third Button
        buttonAccessPlot = tk.Button(self, text="Access your monthly progress !", width=70, height=5,
                                     command=self.plotClick, bg='yellow')
        buttonAccessPlot.place(x=10, y=10, anchor=tk.CENTER)
        buttonAccessPlot.pack()

    # Product input window
    def buEnClick(self):
        ProductInputWindow(self)

    def dietClick(self):
        DietWindow(self)

    def plotClick(self):
        Plots(self)

    def run(self):
        self.mainloop()
