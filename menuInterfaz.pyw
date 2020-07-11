from tkinter import *

raiz=Tk()

raiz.title("Interfaz Numero 2")

menuInterfaz=Frame(raiz, width=600, height=600)
menuInterfaz.pack()

minombre=StringVar()

opción=Label(menuInterfaz, text="Elija una opción")
opción.grid(row=2, column=0, sticky="e", padx=10, pady=10)

def codigoBoton1():

	minombre.set("comunicación")

botonEnvio=Button(raiz, text="Enviar comunicado", command=codigoBoton1)
botonEnvio.pack()

def codigoBoton2():

	minombre.set("newregistro")

botonNuevoreg=Button(raiz, text="Agregar nuevo Registro", command=codigoBoton2)

botonNuevoreg.pack()

def codigoBoton3():

	minombre.set("delregistro")

botonDelreg=Button(raiz, text="Eliminar Registro", command=codigoBoton3)

botonDelreg.pack()

raiz.mainloop()