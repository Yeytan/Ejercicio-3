from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("1500x650")
raiz.configure(background="black")

#Frame Principal

mainFrame = ttk.Frame(raiz,background="turquoise4")
mainFrame.grid(column=0,row=0, sticky=(W))

#Frame base negro

mainframeblack = ttk.Frame(raiz, background="black")
mainframeblack.grid(column=0, row=1, sticky=(W), pady=10)

#Frame izquierdo arriba

mainFrameizq = ttk.Frame(mainframeblack,background="black")
mainFrameizq.grid(column=0,row=0,pady=10,sticky=(W,N))

mainFrameizq2 = ttk.Frame(mainFrameizq,background="black")
mainFrameizq2.grid(column=0,row=0,sticky=(W))

#Izquierdo
IzqFrame = ttk.Frame(mainFrameizq2,background="#333333")
IzqFrame.grid(column=0,row=0,sticky=(W),padx=120)

#Derecho
DerFrame = ttk.Frame(mainFrameizq2,background="#333333")
DerFrame.grid(column=0,row=0,sticky=(W,N), padx=370)

#Frame derecho arriba
mainFrameder = ttk.Frame(mainframeblack,background="#333333")
mainFrameder.grid(column=0,row=0,sticky=(W,N),padx=790, pady=10)

mainFrameder2 = ttk.Frame(mainFrameder,background="#333333")
mainFrameder2.grid(column=0,row=0, sticky=(W,N))

mainFrameder3= ttk.Frame(mainFrameder2,background="#333333")
mainFrameder3.grid(column=0,row=0,sticky=(W,N))

#frame izquierda 

Frame2 = ttk.Frame(mainFrameizq,background="black", padx=118)
Frame2.grid(column=0,row=1,sticky=(W,N))

DerAbajoFrame = ttk.Frame(Frame2,background="#333333" )
DerAbajoFrame.grid(column=0,row=0,sticky=(W,N),padx=1,pady=5 )

DerAbajoFrame1 = ttk.Frame(Frame2,background="#333333")
DerAbajoFrame1.grid(column=1,row=0,sticky=(W), padx=2, pady=5)

#Titulo

ttk.Label(mainFrame,text="SPAI 4.0",font=("verdana",11,"bold"),foreground="white",background="turquoise4", width=200,anchor="w",height=2).grid(column=1,row=0,sticky=(W))

imagen3 = PhotoImage(file="boton.png")
imagenb = ttk.Button(mainFrame,background="turquoise4",relief="flat")
imagenb.grid(column=0,row=0,sticky=(W))
imagenb['image'] = imagen3

#Texto Indicadores

ttk.Label(IzqFrame,text="Indicadores Digitales",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333", width=20).grid(column=0,row=0,sticky=(W))
ttk.Label(IzqFrame,text="Linea 1        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 2        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=2,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 1:       On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Gabinete: Abierto",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma:        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=5,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma 2:     Off",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=6,sticky=(W),pady=11)

#Temperatura

ttk.Label(DerFrame,text="Temperatura",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W))
ttk.Label(DerFrame,text="Temperatura 1:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=30,padx=15)
ttk.Label(DerFrame,text="Temperatura 2:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=1,row=1,sticky=(W),pady=30)
ttk.Label(DerFrame,text="Temp.Agua: 58 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(N,S),columnspan=2, pady=2)
ttk.Label(DerFrame,text="Temp.Ambiente: 32 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(N,S),columnspan=2,pady=10)

imagen5 = PhotoImage(file="Temperatura1.png")
imagenT1 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=2,sticky=(W))
imagenT1['image'] = imagen5

imagen6 = PhotoImage(file="Temperatura2.png")
imagenT2 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT2.grid(column=1,row=2,sticky=(W))
imagenT2['image'] = imagen6

#Produccion

ttk.Label(mainFrameder3,text="Produccion",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W),padx=30)

imagen7 = PhotoImage(file="Grafica.png")
imagenG = ttk.Button(mainFrameder3,background="#333333",relief="flat")
imagenG.grid(column=0,row=1,sticky=(W))
imagenG['image'] = imagen7


#Velocidad

ttk.Label(DerAbajoFrame,text="Velocidad Bomba:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=0,sticky=(W), pady=25, padx=55)

imagen8 = PhotoImage(file="Velocidad.png")
imagen4 = ttk.Button(DerAbajoFrame,background="#333333",relief="flat")
imagen4.grid(column=0,row=1,sticky=(W))
imagen4['image'] = imagen8

#Tanque

ttk.Label(DerAbajoFrame1,text="Nivel del Tanque                          ",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W), padx= 15)

imagen9 = PhotoImage(file="Tanque.png")
imagenTan = ttk.Button(DerAbajoFrame1,background="#333333",relief="flat")
imagenTan.grid(column=0,row=1,sticky=(W))
imagenTan['image'] = imagen9

raiz.mainloop()