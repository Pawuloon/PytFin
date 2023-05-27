import tkinter as tk
from PIL import Image, ImageTk

from PythonFinalProj.ProductInputWindow import ProductInputWindow


class MyGui:
    def __init__(self):
        self.imgName = None
        self.photo = None
        self.window = tk.Tk()
        self.window.title("Weight Calculator")
        self.window.geometry("500x400")

        self.setBackground()
        self.buttons()
        self.icon()

    # Set icon
    def icon(self):
        path = "Pics/img_1.png"
        icon = Image.open(path)
        icoPath = "Pics/IcoIcon.ico"
        icon.save(icoPath, format="ICO")
        self.window.iconbitmap(icoPath)

    # Startup Image
    def image(self):
        image = Image.open("Pics/img.png")
        image = image.resize((500, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.imgName = tk.Label(self.window, image=self.photo)
        self.imgName.pack()

    def setBackground(self):
        image = tk.PhotoImage(file="Pics/img.png")
        background = tk.Label(self.window, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    # Buttons
    def buttons(self):
        buttonEnterProduct = tk.Button(self.window, text="Enter your Product", width=70, height=5,
                                       command=self.buEnClick,bg="yellow")
        buttonEnterProduct.place(x=0, y=0, anchor=tk.CENTER)
        buttonEnterProduct.pack()

    def buEnClick(self):
        ProductInputWindow(self.window)

    def run(self):
        self.window.mainloop()
