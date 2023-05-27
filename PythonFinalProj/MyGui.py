import tkinter as tk
from PIL import Image, ImageTk

class MyGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weight Calculator")
        self.window.geometry("500x400")
        self.window.configure(bg="green")
        self.imgName = None
        self.photo = None
        self.icon()
        self.imgage()
        self.buttons()

    # Set icon
    def icon(self):
        path = "Pics/img_1.png"
        icon = Image.open(path)
        icoPath = "Pics/IcoIcon.ico"
        icon.save(icoPath, format="ICO")
        self.window.iconbitmap(icoPath)

    # Startup Image
    def imgage(self):
        image = Image.open("Pics/img.png")
        image = image.resize((500, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.imgName = tk.Label(self.window, image=self.photo)
        self.imgName.pack()

    # Buttons
    def buttons(self):
        buttonEnterProduct = tk.Button(self.window, text="Enter your Product", command=self.buEnClick)
        buttonEnterProduct.pack()

    def buEnClick(self):
        print("It works !")

    def run(self):
        self.window.mainloop()
