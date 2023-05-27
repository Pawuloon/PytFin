import tkinter as tk
from PIL import Image, ImageTk


class MyGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weight Calculator")
        self.imgName = None
        self.photo = None
        self.buttons()

    def buttons(self):
        # Add image to the app
        self.window.geometry("500x400")
        image = Image.open("Pics/img.png")
        image = image.resize((500, 200), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.imgName = tk.Label(self.window, image=self.photo)
        self.imgName.pack()

        # Buttons
        buttonEnterProduct = tk.Button(self.window, text="Enter your Product", command=self.buEnClick)
        buttonEnterProduct.pack()

    def buEnClick(self):
        print("It works !")

    def run(self):
        self.window.mainloop()
