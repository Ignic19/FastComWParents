import sys
import os
from tkinter import *
from tkinter import messagebox
import sqlite3


ventanaLogin = Tk()
ventanaLogin.title ("Iniciar Sesión")
ventanaLogin.geometry ("350x150+500+250")


Label(ventanaLogin, text = "Usuario").pack()
cuadroUsuario = Entry(ventanaLogin)
cuadroUsuario.pack()

Label(ventanaLogin, text = "Contraseña").pack()
cuadroPassword = Entry(ventanaLogin, show = "*")
cuadroPassword.pack()

#------------------------------------------------- esto hace que el boton de pasar a la siguiente pagina habra el menu

def menuInterfaz():
	os.system("menuInterfaz.py")

botonEnvio=Button(ventanaLogin, text="Enviar comunicado", command=menuInterfaz).pack()

#-------------------------------------------------

def login():
	
	db = sqlite3.connect('C:/Users/Ignac/Desktop/FCWP.db')
	c = db.cursor()
	
	usuario = cuadroUsuario.get()
	claves = cuadroPassword.get()
	
	c.execute('SELECT * FROM usuarios WHERE usuario = ? AND claves = ?', (usuario, claves))
	
	if c.fetchall():
		messagebox.showinfo(title = "Iniciando Sesión", message = "Iniciando Sesión")

	else:
		messagebox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")


	#Falta agregar comando en el if para lanzar a la ventana de menuInterfaz.py

Button (text = "Login", command = login).pack()


ventanaLogin.mainloop()