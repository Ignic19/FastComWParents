from tkinter import *
import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.title("Envío Comunicación")
app.geometry('600x400')

labelTop = tk.Label(app,
                    text = "Seleccione su Cargo")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=["Director/a", "Inspector General", "Jefe/a de UTP"]) 
print(dict(comboExample)) 
comboExample.grid(column=1, row=1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())


textoComentario=Text(app, width=30, height=10)
textoComentario.grid(row=4, column=2, padx=10, pady=10)


#cuadroComunicacion=ttk.Entry(app)
#cuadroComunicacion.grid(row=2, column=2, padx=10, pady=10)


EnviarMensaje=Button(app, text="Enviar", width=15, height=2).grid(row=5, column=2)

app.mainloop()