from tkinter import *
import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.title("Envío Comunicación")
app.geometry('600x400')

titulo = tk.Label(app, text = "Seleccione su Cargo")
titulo.grid(column=0, row=0)

comboCargo = ttk.Combobox(app,  state='readonly',
                            values=["Director/a", "Inspector General", "Jefe/a de UTP"]) 
print(dict(comboCargo)) 
comboCargo.grid(column=1, row=1)
comboCargo.current(0)

print(comboCargo.current(), comboCargo.get())

textoComentario=Text(app, width=30, height=10)
textoComentario.grid(row=4, column=2, padx=10, pady=10)


#cuadroComunicacion=ttk.Entry(app)
#cuadroComunicacion.grid(row=2, column=2, padx=10, pady=10)

#Falta agregar API


EnviarMensaje=Button(app, text="Enviar", width=15, height=2).grid(row=5, column=2)

app.mainloop()