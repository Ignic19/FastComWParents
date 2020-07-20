from tkinter import *
from datetime import datetime
#from firebase import firebase

raiz = Tk()
raiz.title("Agregar nuevo Registro")
raiz.geometry('800x500')

miFrame5=Frame(raiz, width=700, height=600)
miFrame5.pack()

InserteDatos=Label(miFrame5, text="Inserte Datos")
InserteDatos.grid(row=0, column=0, sticky="e", pady=10)

InserteNombreAlumnoNuevoReg=Label(miFrame5, text="Nombre Alumno")
InserteNombreAlumnoNuevoReg.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroNombreAlumnoNuevoReg=Entry(miFrame5)
cuadroNombreAlumnoNuevoReg.grid(row=1, column=1, padx=10, pady=10)

InserteApellidoAlumnoNuevoReg=Label(miFrame5, text="Apellido Alumno")
InserteApellidoAlumnoNuevoReg.grid(row=1, column=2, sticky="e", padx=10, pady=10)

cuadroApellidoAlumnoNuevoReg=Entry(miFrame5)
cuadroApellidoAlumnoNuevoReg.grid(row=1, column=3, padx=10, pady=10)

InserteCurso=Label(miFrame5, text="Curso")
InserteCurso.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroCurso=Entry(miFrame5)
cuadroCurso.grid(row=2, column=1, padx=10, pady=10)

InserteLetraCurso=Label(miFrame5, text="Letra del Curso")
InserteLetraCurso.grid(row=2, column=2, sticky="e", padx=10, pady=10)

cuadroLetraCurso=Entry(miFrame5)
cuadroLetraCurso.grid(row=2, column=3, padx=10, pady=10)

InserteNombreApoderado1=Label(miFrame5, text="Nombre Apoderado")
InserteNombreApoderado1.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroNombreApoderado1=Entry(miFrame5)
cuadroNombreApoderado1.grid(row=3, column=1, padx=10, pady=10)

InserteApellidoApoderado1=Label(miFrame5, text="Apellido Apoderado")
InserteApellidoApoderado1.grid(row=3, column=2, sticky="e", padx=10, pady=10)

cuadroApellidoApoderado1=Entry(miFrame5)
cuadroApellidoApoderado1.grid(row=3, column=3, padx=10, pady=10)

InserteTelefonoApoderado1=Label(miFrame5, text="Telefono Apoderado")
InserteTelefonoApoderado1.grid(row=4, column=0, sticky="e", padx=10, pady=10)

cuadroTelefonoApoderado1=Entry(miFrame5)
cuadroTelefonoApoderado1.grid(row=4, column=1, padx=10, pady=10)

InserteApoderadoSustituto=Label(miFrame5, text="Apoderado Secundario")
InserteApoderadoSustituto.grid(row=5, column=0, sticky="e", padx=10, pady=10)

cuadroApoderadoSustituto=Entry(miFrame5)
cuadroApoderadoSustituto.grid(row=5, column=1, padx=10, pady=10)

InserteApellidoApoderadoSustituto=Label(miFrame5, text="Apellido Apoderado Secundario")
InserteApellidoApoderadoSustituto.grid(row=5, column=2, sticky="e", padx=10, pady=10)

cuadroApellidoApoderadoSustituto=Entry(miFrame5)
cuadroApellidoApoderadoSustituto.grid(row=5, column=3, padx=10, pady=10)

InserteTelefonoSustituto=Label(miFrame5, text="Telefono Apoderado Secundario")
InserteTelefonoSustituto.grid(row=6, column=0, sticky="e", padx=10, pady=10)

cuadroTelefonoSustituto=Entry(miFrame5)
cuadroTelefonoSustituto.grid(row=6, column=1, padx=10, pady=10)


def FichaNueva():
	
	db = sqlite3.connect('C:/Users/Ignac/Desktop/FCWP.db')
	c = db.cursor()
	
	NombreAlumno = cuadroNombreAlumnoNuevoReg.get()
	ApellidoAlumno = cuadroApellidoAlumnoNuevoReg.get()
	Curso = cuadroCurso.get()
	LetraCurso = cuadroLetraCurso.get()
	NombreApoderado= cuadroNombreApoderado1.get()
	ApellidoApoderado = cuadroApellidoApoderado1.get()
	TelefonoApoderado = cuadroTelefonoApoderado1.get()
	ApoderadoSecundario = cuadroApoderadoSustituto.get()
	ApellidoApoderadoSecundario = cuadroApellidoApoderadoSustituto.get()
	TelefonoApoderadoSecundario = cuadroTelefonoSustituto.get()
	
	c.execute('INSERT INTO DatosAlumnos ('NombreAlumno','ApellidoAlumno', 'Curso','LetraCurso','NombreApoderado','ApellidoApoderado','TelefonoApoderado','ApoderadoSecundario','ApellidoApoderadoSecundario','TelefonoApoderadoSecundario') ')

c.close()

Button (text = "Guardar Información", command = FichaNueva).pack()

#botonGuardarInfo=Button(miFrame5, text="Guardar Información", command = FichaNueva).pack()
#botonGuardarInfo.grid(row=8, column=3)


raiz.mainloop()