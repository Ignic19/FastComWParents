import sys
import os
from tkinter import *
import sqlite3

raiz=Tk()
raiz.title("Eliminar Registro")
raiz.geometry('600x300')

miFrame6=Frame(raiz, width=400, height=300)
miFrame6.pack()

InserteNombreAlumnoElimReg=Label(miFrame6, text="Inserte Nombre Alumno")
InserteNombreAlumnoElimReg.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombreAlumnoElimReg=Entry(miFrame6)
cuadroNombreAlumnoElimReg.grid(row=1, column=1, padx=10, pady=10)

InserteApellidoAlumnoElimReg=Label(miFrame6, text="Inserte Apellido Alumno")
InserteApellidoAlumnoElimReg.grid(row=1, column=2, sticky="e", padx=10, pady=10)

cuadroApellidoAlumnoElimReg=Entry(miFrame6)
cuadroApellidoAlumnoElimReg.grid(row=1, column=3, padx=10, pady=10)

InserteCursoElim=Label(miFrame6, text="Inserte Curso")
InserteCursoElim.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroCursoElim=Entry(miFrame6)
cuadroCursoElim.grid(row=2, column=1, padx=10, pady=10)

def login():
	
	db = sqlite3.connect('C:/Users/Ignac/Desktop/FCWP.db')
	c = db.cursor()

	NombreAlumno = cuadroNombreAlumnoElimReg.get()
	ApellidoAlumno = cuadroApellidoAlumnoElimReg.get()
	Curso = cuadroCursoElim.get()

	c.execute('DELETE FROM DatosAlumnos WHERE NombreAlumno = ?, ApellidoAlumno = ? AND Curso = ?',(NombreAlumno, ApellidoAlumno, Curso))

botonGuardarInfo=Button(miFrame6, text="Eliminar Registro").grid(row=8, column=3)


raiz.mainloop()