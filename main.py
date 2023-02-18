from tkinter import *
import random as rm
from PIL import ImageTk, Image


def make_equation(difficulty):
    if difficulty == "easy":
        a = rm.randint(1,20)
        b = rm.randint(1,20)
        c = ((a**2)+(b**2))**0.5
    elif difficulty == "normal":
        a = rm.randint(1,40)
        b = rm.randint(1,40)
        c = ((a**2)+(b**2))**0.5
    elif difficulty == "hard":
        a = rm.randint(1,80)
        b = rm.randint(1,80)
        c = ((a**2)+(b**2))**0.5



window = Tk()
window.title("Pythagoras")
window.iconbitmap("icon.ico")


frame1 = Frame(window)
frame1.pack(fill="both",expand=True)

frame2 = Frame(window)
frame2.pack(fill="both",expand=True)

triangle = ImageTk.PhotoImage(Image.open("triangle.png"))
img_triangle = Label(frame1, image = triangle)
img_triangle.place(relx=0.5, rely=0.5, anchor=CENTER)


window.geometry("1360x768")
window.mainloop()