from tkinter import *
from tkinter import ttk
from algo import *


def create_group(number_in_group):
    crew = compute(number_in_group)
    new_windows = Toplevel(fenetre)


    # Using treeview widget 
    treev = ttk.Treeview(new_windows, selectmode ='browse') 
    
    # Calling pack method w.r.to treeview 
    treev.pack(side ='right') 
    
    # Constructing vertical scrollbar 
    # with treeview 
    verscrlbar = ttk.Scrollbar(new_windows,  
                            orient ="vertical",  
                            command = treev.yview) 
    
    # Calling pack method w.r.to verical  
    # scrollbar 
    verscrlbar.pack(side ='right', fill ='x') 
    
    # Configuring treeview 
    treev.configure(xscrollcommand = verscrlbar.set) 
    
    # Defining number of columns 
    treev["columns"] = ("1", "2", "3") 
    
    # Defining heading 
    treev['show'] = 'headings'
    
    # Assigning the width and anchor to  the 
    # respective columns 
    treev.column("1", width = 100, anchor ='c') 
    treev.column("2", width = 100, anchor ='c') 
    treev.column("3", width = 250, anchor ='c') 
    
    # Assigning the heading names to the  
    # respective columns 
    treev.heading("1", text ="Index") 
    treev.heading("2", text ="Group") 
    treev.heading("3", text ="People in group") 
    for i in range(len(crew.keys())):
        treev.insert("", "end", text="L1", values=(i, "Group"+str(1), crew["group " + str(i+1)]))





    



fenetre = Tk()
fenetre.geometry("500x500")

frameLeft = Frame(fenetre, padx=50, pady=50)
frameCenter = Frame(fenetre, padx=50, pady=50)
frameRight = Frame(fenetre, padx=50, pady=25)

Label(fenetre, text="Binômotron", font=("Courier", 16, "italic")).grid()


frameLeft.grid(row=1, column=0)
frameCenter.grid(row=1, column=1)
frameRight.grid(row=1, column=2)

for i in people:
    Label(frameLeft, text=i).pack()

number_in_group = IntVar()
Checkbutton(frameCenter, text='Groupe 2',variable=number_in_group, onvalue=2, offvalue=0).pack()
Checkbutton(frameCenter, text='Groupe 3',variable=number_in_group, onvalue=3, offvalue=0).pack()
Checkbutton(frameCenter, text='Groupe 4',variable=number_in_group, onvalue=4, offvalue=0).pack()
Checkbutton(frameCenter, text='Groupe 5',variable=number_in_group, onvalue=5, offvalue=0).pack()

Button(frameRight, text="press me", command=lambda: create_group(number_in_group.get())).pack()
fenetre.mainloop()