from tkinter import *
from algo import *


def display():
    for key in crew.keys():
        Label(fenetre, text=key).pack()

fenetre = Tk()
fenetre.geometry("500x500")

frameLeft = Frame(fenetre, padx=50, pady=50)
frameCenter = Frame(fenetre, padx=50, pady=50)
frameRight = Frame(fenetre, padx=50, pady=25)

title = Label(fenetre, text="Binômotron", font=("Courier", 16, "italic")).grid()


frameLeft.grid(row=1, column=0)
frameCenter.grid(row=1, column=1)
frameRight.grid(row=1, column=2)

for i in people:
    Label(frameLeft, text=i).pack()

number_in_group = IntVar()
c2 = Checkbutton(frameCenter, text='Groupe 2',variable=number_in_group, onvalue=2, offvalue=0).pack()
c3 = Checkbutton(frameCenter, text='Groupe 3',variable=number_in_group, onvalue=3, offvalue=0).pack()
c4 = Checkbutton(frameCenter, text='Groupe 4',variable=number_in_group, onvalue=4, offvalue=0).pack()
c5 = Checkbutton(frameCenter, text='Groupe 5',variable=number_in_group, onvalue=5, offvalue=0).pack()

button = Button(frameRight, text="press me", command=lambda: [compute(number_in_group.get()), display()]).pack()
fenetre.mainloop()