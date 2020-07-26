from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests

#La función sirve para conectar con la API de Telegram
def enviarDatos():
    #Mensajito es la variable donde se almacena el mensaje
    mensajito = textoComentario.get(1.0, "end-1c")

    def comunicacion_escrita(mensaje_bot):
        token_bot = '1032534984:AAEkVLBp9C8vQRXgZMUMdVt_3IGNqWF7GKc'
        bot_chatID = '851010840'
        enviar_com = 'https://api.telegram.org/bot' + token_bot + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + mensaje_bot

        respuesta = requests.get(enviar_com)

        return respuesta.json()

    enviarCOM = comunicacion_escrita(mensajito)
    print(enviarCOM)


app = tk.Tk() 
app.title("Envío Comunicación")
app.geometry('600x400')

labelTop = tk.Label(app,
                    text = "Seleccione su Cargo")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, state = "readonly",
                            values=["Director/a", "Inspector General", "Jefe/a de UTP"]) 
print(dict(comboExample)) 
comboExample.grid(column=1, row=1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())

#-----falta contatenar mensaje (cargo + punto aparte + mensaje)

textoComentario=Text(app, width=30, height=10)
textoComentario.grid(row=4, column=2, padx=10, pady=10)


#cuadroComunicacion=ttk.Entry(app)
#cuadroComunicacion.grid(row=2, column=2, padx=10, pady=10)


EnviarMensaje=Button(app, text="Enviar", width=15, height=2, command=enviarDatos)
EnviarMensaje.grid(row=5, column=2)

botonVolver=Button(app, text="Cerrar", width=10, height=1, command=quit)
botonVolver.grid(row=5, column=1)


app.mainloop()