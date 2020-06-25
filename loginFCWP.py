from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=2000)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text="Password:")
passwordLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():

	minombre.set("Ignacio")

botonEnvio=Button(raiz, text="Iniciar Sesión", command=codigoBoton)
botonEnvio.pack()

##Button(miFrame, text="Entrar").grid(row=6, column=1, padx=10, pady=10)

raiz.mainloop()