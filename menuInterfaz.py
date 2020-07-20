from tkinter import *

raiz=Tk()
raiz.geometry('300x250')
raiz.title("Opciones")

menuInterfaz=Frame(raiz)
menuInterfaz.pack()

minombre=StringVar()

opción=Label(menuInterfaz, text="Elija una Opción")
opción.grid(row=2, column=0, sticky="e", padx=10, pady=10)

def codigoBoton1():

	minombre.set("comunicación")

botonEnvio=Button(raiz, text="Enviar comunicado", command=codigoBoton1, padx=10, pady=10)
botonEnvio.pack()

def codigoBoton2():

	minombre.set("newregistro")

botonNuevoreg=Button(raiz, text="Agregar nuevo Registro", command=codigoBoton2, padx=10, pady=10)

botonNuevoreg.pack()

def codigoBoton3():

	minombre.set("delregistro")

botonDelreg=Button(raiz, text="Eliminar Registro", command=codigoBoton3, padx=10, pady=10)

botonDelreg.pack()

raiz.mainloop()