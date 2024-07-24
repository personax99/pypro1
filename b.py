import tkinter as tk
from tkinter import *
import tkinter.messagebox as msg
form=tk.Tk()
form.geometry('500x500')
lblu=tk.Label(form,text="username")
lblu.grid(row=0,column=0)
etu=tk.Entry(form,width=50)
etu.grid(row=0,column=1)

lblp=tk.Label(form,text="password")
lblp.grid(row=1,column=0)
etp=tk.Entry(form,width=50)
etp.grid(row=1,column=1)

def disp():
    if etu.get()=="admin" and etp.get()=="1234":
        msg.showinfo("msg","LOGIN SUCCESSFUL")
    else:
        msg.showinfo("msg","LOGIN NOT SUCCESSFUL")

btnadd=tk.Button(form,text='LOGIN',command=disp)
btnadd.grid(row=2,column=0)
form.mainloop()