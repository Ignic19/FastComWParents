import sys
import os
from tkinter import *


raiz=Tk()
raiz.geometry('300x250')
raiz.title("Menu Opciones")

menuInterfaz=Frame(raiz)
menuInterfaz.pack()

opción=Label(menuInterfaz, text="Elija una Opción:")
opción.grid(row=2, column=0, sticky="e", padx=10, pady=10)

def EnviarComunicación():
	os.system("enviarComunicacion.py")

botonEnvio=Button(raiz, text="Enviar comunicado", command=EnviarComunicación, padx=10, pady=10)
botonEnvio.pack()

def NuevoRegistro():
	os.system("agregarAlumnoApoderado.py")

botonNuevoreg=Button(raiz, text="Agregar nuevo Registro", command=NuevoRegistro, padx=10, pady=10)
botonNuevoreg.pack()

def elimAlumno():
	os.system("eliminarRegistro.py")

botonDelreg=Button(raiz, text="Eliminar Registro", command=elimAlumno, padx=10, pady=10)
botonDelreg.pack()


raiz.mainloop()