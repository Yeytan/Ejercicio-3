from tkinter import *
from tkinter import ttk
import tkinter.ttk as ttk
import tkinter as ttk

raiz = Tk()
raiz.configure(background="black")
raiz.geometry("1000x600")

MenuFrame = ttk.Frame(raiz,background="turquoise4")
MenuFrame.grid(column=0,row=0)

raiz.mainloop()