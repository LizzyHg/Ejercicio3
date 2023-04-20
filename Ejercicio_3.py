from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("SPAI 4.0")
raiz.config(bg='black')
raiz.geometry("800x500")

mainFrame = Frame(raiz, bg='black')
mainFrame.grid(column=0, row=0)
secondFrame = Frame(mainFrame, bg='dark gray')
secondFrame.grid(column=1, row=1, sticky=(N, W))
Label(mainFrame, text=" ", bg='black').grid(column=2, row=1)
thirdFrame = Frame(mainFrame, bg='dark gray')
thirdFrame.grid(column=3, row=1, sticky=(N, W))
Label(mainFrame, text=" ", bg='black').grid(column=1, row=2)
fourthFrame = Frame(mainFrame, bg='dark gray')
fourthFrame.grid(column=1, row=3, columnspan=3, sticky=(N, W))
fifthFrame = Frame(mainFrame, bg='dark gray')
fifthFrame.grid(column=3, row=3, sticky=(E))
Label(mainFrame, text=" ", bg='black').grid(column=4, row=1)
sixthFrame = Frame(mainFrame, bg='dark gray')
sixthFrame.grid(column=5, row=1, sticky=(N), rowspan=3)

#secondFrame
Label(secondFrame, text="Indicadores Digitales", fg='blue', bg='dark gray').grid(column=1, row=1, columnspan=3, sticky=(W))
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=2)
Label(secondFrame, text="Linea 1: ", fg='white', bg='dark gray').grid(column=1, row=3)
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=4)
Label(secondFrame, text="Linea 2: ", fg='white', bg='dark gray').grid(column=1, row=5)
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=6)
Label(secondFrame, text="Linea 1: ", fg='white', bg='dark gray').grid(column=1, row=7)
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=8)
Label(secondFrame, text="Gabinete: ", fg='white', bg='dark gray').grid(column=1, row=9)
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=10)
Label(secondFrame, text="Alarma: ", fg='white', bg='dark gray').grid(column=1, row=11)
Label(secondFrame, text=" ", bg='dark gray').grid(column=1, row=12)
Label(secondFrame, text="Alarma2: ", fg='white', bg='dark gray').grid(column=1, row=13)

Label(secondFrame, text="On", fg='white', bg='dark gray').grid(column=2, row=3, sticky=(E))
Label(secondFrame, text="On ", fg='white', bg='dark gray').grid(column=2, row=5, sticky=(E))
Label(secondFrame, text="On ", fg='white', bg='dark gray').grid(column=2, row=7, sticky=(E))
Label(secondFrame, text="Abierto ", fg='white', bg='dark gray').grid(column=2, row=9, sticky=(E))
Label(secondFrame, text="On ", fg='white', bg='dark gray').grid(column=2, row=11, sticky=(E))
Label(secondFrame, text="Off ", fg='white', bg='dark gray').grid(column=2, row=13, sticky=(E))

Label(secondFrame, text="  ", bg='dark gray').grid(column=3, row=3)

imagen1 = PhotoImage(file="Verde.png")
imagen2 = PhotoImage(file="Rojo.png")

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=3)
etqImagen['image'] = imagen1

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=5)
etqImagen['image'] = imagen1

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=7)
etqImagen['image'] = imagen1

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=9)
etqImagen['image'] = imagen2

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=11)
etqImagen['image'] = imagen2

etqImagen = Label(secondFrame, bg='dark gray')
etqImagen.grid(column=4, row=13)
etqImagen['image'] = imagen1

#thirdFrame
Label(thirdFrame, text="Temperaturas", fg='blue', bg='dark gray').grid(column=1, row=1, columnspan=3, sticky=(W))
Label(thirdFrame, text=" ", bg='dark gray').grid(column=1, row=2)
Label(thirdFrame, text="Temperatura 1: ", fg='white', bg='dark gray').grid(column=1, row=3, sticky=(N, S, W, E))
Label(thirdFrame, text="Temperatura 2: ", fg='white', bg='dark gray').grid(column=2, row=3, sticky=(N, S, W, E))

imagen3 = PhotoImage(file="SVerde.png")
imagen4 = PhotoImage(file="SAmarillo.png")

etqImagen = Label(thirdFrame, bg='dark gray')
etqImagen.grid(column=1, row=4)
etqImagen['image'] = imagen3

etqImagen = Label(thirdFrame, bg='dark gray')
etqImagen.grid(column=2, row=4)
etqImagen['image'] = imagen4

Label(thirdFrame, text=" ", bg='dark gray').grid(column=1, row=5)
Label(thirdFrame, text="Temp. Agua: 58°C", fg='white', bg='dark gray').grid(column=1, row=6, columnspan=2, sticky=(N, S, W, E))
Label(thirdFrame, text="", bg='dark gray').grid(column=1, row=7)
Label(thirdFrame, text="Temp. Ambiente: 32°C", fg='white', bg='dark gray').grid(column=1, row=8, columnspan=2, sticky=(N, S, W, E))
Label(thirdFrame, text="", bg='dark gray').grid(column=1, row=9)
Label(thirdFrame, text="", bg='dark gray').grid(column=1, row=10)

#fourthFrame
Label(fourthFrame, text="", bg='dark gray').grid(column=1, row=1)
Label(fourthFrame, text="Velocidad bomba: ", fg='white', bg='dark gray').grid(column=1, row=2, sticky=(N, S, W, E))

imagen5 = PhotoImage(file="SRojo.png")

etqImagen = Label(fourthFrame, bg='dark gray')
etqImagen.grid(column=1, row=3)
etqImagen['image'] = imagen5

Label(fourthFrame, text="", bg='dark gray').grid(column=1, row=4)
Label(fourthFrame, text="              ", bg='dark gray').grid(column=2, row=1)

#fifthFrame
Label(fifthFrame, text="Nivel del Tanque", fg='blue', bg='dark gray').grid(column=1, row=1, sticky=(W))

imagen6 = PhotoImage(file="Burbuja.png")

etqImagen = Label(fifthFrame, bg='dark gray')
etqImagen.grid(column=1, row=2)
etqImagen['image'] = imagen6

Label(fifthFrame, text="            ", bg='dark gray').grid(column=2, row=1)

#sixthFrame
Label(sixthFrame, text="Producción", fg='blue', bg='dark gray').grid(column=1, row=1, sticky=(W))
Label(sixthFrame, text=" ", bg='dark gray').grid(column=1, row=2)

imagen7 = PhotoImage(file="Grafica.png")

etqImagen = Label(sixthFrame, bg='dark gray')
etqImagen.grid(column=1, row=3)
etqImagen['image'] = imagen7

Label(sixthFrame, text=" ", bg='dark gray').grid(column=1, row=4)
Label(sixthFrame, text="Piezas producidas: 50", fg='white', bg='dark gray').grid(column=1, row=5, sticky=(N, S, W, E))
Label(sixthFrame, text="", bg='dark gray').grid(column=1, row=6)
Label(sixthFrame, text="Piezas defectuosas: 12", fg='white', bg='dark gray').grid(column=1, row=7, sticky=(N, S, W, E))
Label(sixthFrame, text="", bg='dark gray').grid(column=1, row=8)

raiz.mainloop()