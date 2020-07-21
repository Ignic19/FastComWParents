from tkinter import *
#import enviarComunicacion
#import agregarAlumnoApoderado
#import eliminarRegistro

raiz=Tk()
raiz.geometry('300x250')
raiz.title("Opciones")

menuInterfaz=Frame(raiz)
menuInterfaz.pack()

opción=Label(menuInterfaz, text="Elija una Opción")
opción.grid(row=2, column=0, sticky="e", padx=10, pady=10)


def EnviarComunicación():

	enviarComunicacion.set("comunicación")

botonEnvio=Button(raiz, text="Enviar comunicado", command=EnviarComunicación, padx=10, pady=10)
botonEnvio.pack()

def AgregarNuevoRegistro():

	opcion2.set("newregistro")

botonNuevoreg=Button(raiz, text="Agregar nuevo Registro", command=AgregarNuevoRegistro, padx=10, pady=10)
botonNuevoreg.pack()

def EliminarRegistro():

	opcion3.set("elimRegistro")

botonDelreg=Button(raiz, text="Eliminar Registro", command=EliminarRegistro, padx=10, pady=10)
botonDelreg.pack()

raiz.mainloop()