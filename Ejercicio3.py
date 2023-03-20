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
 #Frameizqabajo
mainFrameizqabajo = ttk.Frame(mainFrameizq,background="black", padx=118)
mainFrameizqabajo.grid(column=0,row=1,sticky=(W,N))

mainFrameizqabajo1 = ttk.Frame(mainFrameizqabajo,background="#333333" )
mainFrameizqabajo1.grid(column=0,row=0,sticky=(W,N),padx=1,pady=5 )

mainFrameizqabajo2 = ttk.Frame(mainFrameizqabajo,background="#333333")
mainFrameizqabajo2.grid(column=1,row=0,sticky=(W), padx=2, pady=5)

#Titulo

ttk.Label(mainFrame,text="SPAI 4.0",font=("verdana",11,"bold"),foreground="white",background="turquoise4", width=200,anchor="w",height=2).grid(column=1,row=0,sticky=(W))

imagenboton = PhotoImage(file="boton.png")
imagenb = ttk.Button(mainFrame,background="turquoise4",relief="flat")
imagenb.grid(column=0,row=0,sticky=(W))
imagenb['image'] = imagenboton

#Texto Indicadores

ttk.Label(IzqFrame,text="Indicadores Digitales",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333", width=20).grid(column=0,row=0,sticky=(W))
ttk.Label(IzqFrame,text="Linea 1        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 2        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=2,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 1:       On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Gabinete: Abierto",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma:        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=5,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma 2:     Off",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=6,sticky=(W),pady=11)

imagenverde1 = PhotoImage(file="botonverde2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=1, sticky=(E))
imagenT1['image'] = imagenverde1

imagenverde2 = PhotoImage(file="botonverde2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=2, sticky=(E))
imagenT1['image'] = imagenverde2

imagenverde3 = PhotoImage(file="botonverde2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=3, sticky=(E))
imagenT1['image'] = imagenverde3

imagenroja = PhotoImage(file="botonrojo2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=4, sticky=(E))
imagenT1['image'] = imagenroja

imagenroja1 = PhotoImage(file="botonrojo2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=5, sticky=(E))
imagenT1['image'] = imagenroja1

imagenverde4 = PhotoImage(file="botonverde2.png")
imagenT1 = ttk.Button(IzqFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=6, sticky=(E))
imagenT1['image'] = imagenverde4




#Temperatura

ttk.Label(DerFrame,text="Temperatura",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W))
ttk.Label(DerFrame,text="Temperatura 1:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=30,padx=15)
ttk.Label(DerFrame,text="Temperatura 2:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=1,row=1,sticky=(W),pady=30)
ttk.Label(DerFrame,text="Temp.Agua: 58 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(N,S),columnspan=2, pady=2)
ttk.Label(DerFrame,text="Temp.Ambiente: 32 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(N,S),columnspan=2,pady=10)

imagentemp = PhotoImage(file="Temperatura1.png")
imagenT1 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=2,sticky=(W))
imagenT1['image'] = imagentemp

imagentemp2 = PhotoImage(file="Temperatura2.png")
imagenT2 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT2.grid(column=1,row=2,sticky=(W))
imagenT2['image'] = imagentemp2

#Produccion

ttk.Label(mainFrameder3,text="Produccion",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W),padx=30)

imagengrafica = PhotoImage(file="Grafica.png")
imagenG = ttk.Button(mainFrameder3,background="#333333",relief="flat")
imagenG.grid(column=0,row=1,sticky=(W))
imagenG['image'] = imagengrafica


#Velocidad

ttk.Label(mainFrameizqabajo1,text="Velocidad Bomba:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=0,sticky=(W), pady=25, padx=55)

imagenvel = PhotoImage(file="Velocidad.png")
imagen4 = ttk.Button(mainFrameizqabajo1,background="#333333",relief="flat")
imagen4.grid(column=0,row=1,sticky=(W))
imagen4['image'] = imagenvel

#Tanque

ttk.Label(mainFrameizqabajo2,text="Nivel del Tanque                          ",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W), padx= 15)

imagentanque = PhotoImage(file="Tanque.png")
imagenTan = ttk.Button(mainFrameizqabajo2,background="#333333",relief="flat")
imagenTan.grid(column=0,row=1,sticky=(W))
imagenTan['image'] = imagentanque

raiz.mainloop()