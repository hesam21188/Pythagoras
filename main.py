from tkinter import *
import random as rm
from PIL import ImageTk, Image


score = 0

def make_equation():
    a = rm.randint(1,10)
    b = rm.randint(1,10)
    angle_1.config(text=a)
    angle_2.config(text=b)
    make_equation.c = (a**2)+(b**2)


def submit():
    answer = inp.get()
    if int(answer) == int(make_equation.c):
        print("True")
        global score
        score += 1
        socor.config(text=f"Score : {score}")
    else:
        print("false ",make_equation.c)
        score -= 0.5
        socor.config(text=f"Score : {score}")
    inp.delete(0, END)
    make_equation()

def handler(e):
    submit()


window = Tk()
window.title("Pythagoras")
window.iconbitmap("icon.ico")

triangle = ImageTk.PhotoImage(Image.open("triangle.png"))
img_triangle = Label(window, image = triangle)
hypotenuse = Label(window,text="X",font="arial 20")
angle_2 = Label(window,text="",font="arial 20")
angle_1 = Label(window,text="",font="arial 20")
inp_text = Label(window,text="X = ",font="arial 16")
inp = Entry(window,font=('arial 18'))
btn_ok = Button(window,text="ok",fg="yellow",bg="black",command=submit)
btn_ref = Button(window,text="refresh",fg="yellow",bg="black",command=make_equation)
radical = Label(window,text="√",font="arial 32 bold")
socor = Label(window,text="Score : 0",font="arial 16",bg="black",fg="yellow")


img_triangle.place(relx=0.5, rely=0.5, anchor=CENTER)
angle_1.place(relx=0.5, rely=0.5,y=-25,x=-25, anchor=CENTER)
angle_2.place(relx=0.5, rely=0.5,y=125,x=5, anchor=CENTER)
hypotenuse.place(relx=0.5, rely=0.5,y=20,x=160, anchor=CENTER)
inp.place(relx=0.5, rely=0.5,y=185,x=5, anchor=CENTER)
inp_text.place(relx=0.5, rely=0.5,y=185,x=-165, anchor=CENTER)
radical.place(relx=0.5, rely=0.5,y=185,x=-140, anchor=CENTER)
btn_ok.place(relx=0.5, rely=0.5,y=235,x=5, anchor=CENTER)
btn_ref.place(relx=0.5, rely=0.5,y=270,x=5, anchor=CENTER)
socor.place(relx=0.5, rely=0.5,y=-200, anchor=CENTER)
make_equation()
window.bind('<Return>',handler)



window.geometry("1360x768")
window.mainloop()