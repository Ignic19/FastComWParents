import sys
import os
from tkinter import *
from tkinter import messagebox
import sqlite3
# import menuIntefaz

ventanaLogin = Tk()
ventanaLogin.title ("Iniciar Sesión")
ventanaLogin.geometry ("350x150+500+250")


Label(ventanaLogin, text = "Usuario").pack()
cuadroUsuario = Entry(ventanaLogin)
cuadroUsuario.pack()

Label(ventanaLogin, text = "Contraseña").pack()
cuadroPassword = Entry(ventanaLogin, show = "*")
cuadroPassword.pack()

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
		
	c.destroy()

Button (text = "Login", command = login).pack()

def abrirmenuinterfaz():

	menuInterfaz = Toplevel(ventanaLogin)
	menuInterfaz.title("Menu Interfaz")
	menuInterfaz.geometry("300x250")

ventanaLogin.mainloop()