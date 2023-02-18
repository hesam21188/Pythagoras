from tkinter import *
import random as rm
from PIL import ImageTk, Image


def make_equation(difficulty):
    if difficulty == "easy":
        a = rm.randint(1,20)
        b = rm.randint(1,20)
        c = ((a**2)+(b**2))**0.5
        angle_1.config(text=a)
        angle_2.config(text=b)
        hypotenuse.config(text=c)
    elif difficulty == "normal":
        a = rm.randint(1,40)
        b = rm.randint(1,40)
        c = ((a**2)+(b**2))**0.5
        angle_1.config(text=a)
        angle_2.config(text=b)
        hypotenuse.config(text=c)
    elif difficulty == "hard":
        a = rm.randint(1,80)
        b = rm.randint(1,80)
        c = ((a**2)+(b**2))**0.5
        angle_1.config(text=a)
        angle_2.config(text=b)
        hypotenuse.config(text=c)



window = Tk()
window.title("Pythagoras")
window.iconbitmap("icon.ico")

triangle = ImageTk.PhotoImage(Image.open("triangle.png"))
img_triangle = Label(window, image = triangle)
hypotenuse = Label(window,text="",font="arial 20")
angle_2 = Label(window,text="",font="arial 20")
angle_1 = Label(window,text="X",font="arial 20")
inp_text = Label(window,text="X = ",font="arial 16")
inp = Entry(window,font=('arial 18'))
btn_ok = Button(window,text="ok",fg="yellow",bg="black")
btn_ref = Button(window,text="refresh",fg="yellow",bg="black")


img_triangle.place(relx=0.5, rely=0.5, anchor=CENTER)
angle_1.place(relx=0.5, rely=0.5,y=-25,x=-25, anchor=CENTER)
angle_2.place(relx=0.5, rely=0.5,y=125,x=5, anchor=CENTER)
hypotenuse.place(relx=0.5, rely=0.5,y=20,x=160, anchor=CENTER)
inp.place(relx=0.5, rely=0.5,y=185,x=5, anchor=CENTER)
inp_text.place(relx=0.5, rely=0.5,y=185,x=-155, anchor=CENTER)
btn_ok.place(relx=0.5, rely=0.5,y=235,x=5, anchor=CENTER)
btn_ref.place(relx=0.5, rely=0.5,y=270,x=5, anchor=CENTER)



window.geometry("1360x768")
window.mainloop()