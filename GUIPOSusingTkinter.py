from os import close
import sys
from tkinter import *
from tkinter import messagebox
import time, calendar
import tkinter as tk
top=tk.Tk()
top.title("POS")
top.geometry('720x650')
c=Frame(top,bg='blue')

PNE=tk.StringVar()
PPE=tk.IntVar()
QE=tk.IntVar()
TT=tk.IntVar()

def fetch():
    prod=PNE.get()
    price=PPE.get()
    Qt=QE.get()
    

           
    PNE.set("")
    PPE.set('0')
    QE.set('0')

    ttl=TT.get()
    total=price*Qt 
    TT.set(+total)
def checking2():
        
    messagebox.askyesno("warning","Are you sure to EXIT?")        
    
    
PN_lbl = tk.Label(top, text="Product Name").place(x=10,y=100)
PP_lbl = tk.Label(top, text="Product Price").place(x=10,y=200)
Q_lbl = tk.Label(top, text="Quantity").place(x=10,y=300)    
PN_ent = tk.Entry(top, textvariable = PNE).place(x=150,y=100)
PP_ent = tk.Entry(top, textvariable = PPE).place(x=150,y=200)
QE_ent = tk.Entry(top, textvariable = QE).place(x=150,y=300)
TT_label = Button(top, text="TOTAL", bg='black', fg='white').place(x=10,y=450, width=120,height=60)
Ttl_label=tk.Label(top, textvariable= TT, bg='black', fg='white',font=("Courier", 36, "bold")).place (x=200, y=450,width=260, height=60)


button3 = Button(top, text = "SUBMIT", command=fetch).place(x=10, y=400)
button2 = Button(top, text="EXIT", command=checking2).place(x=200,y=600)


c.pack(fill="both", expand=True)

top.mainloop()        
        

        




