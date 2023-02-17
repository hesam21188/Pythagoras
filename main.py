from tkinter import *
import random as rm



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






window.geometry("1280x720")
window.mainloop()