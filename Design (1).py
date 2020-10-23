from tkinter import *
people = ["pierre", "paul", "guillaume", "eliott"]

def number_group():
    title.config(text="alla")


root = Tk()
root.geometry("500x500")

frameLeft = Frame(root)
frameLeft.pack(side=LEFT)

title = Label(root, text="Hello", font=("Courrier", 30))
title.pack(fill="both", side=TOP)


for i in people:
    liste = Label(frameLeft, text=i, padx=5)
    liste.pack()


var1 = IntVar()
c1 = Checkbutton(root, text="2", variable=var1, onvalue=1, offvalue=0, command=number_group)
c1.pack()
c2 = Checkbutton(root, text="3", variable=var1, onvalue=2, offvalue=3, command=number_group)
c2.pack()
c3 = Checkbutton(root, text="4", variable=var1, onvalue=4, offvalue=5, command=number_group)
c3.pack()
c4 = Checkbutton(root, text="5", variable=var1, onvalue=6, offvalue=7, command=number_group)
c4.pack()



root.mainloop()