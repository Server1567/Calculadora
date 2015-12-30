#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Sígueme en mis Redes Sociales:
Facebook: https://www.facebook.com/Mr.Server1567
Twitter: @server1567
Instagram: @juniorsver

Te dejo mi GitHub: https://github.com/Server1567

"""

from Tkinter import *

# ----- Almacenamiento de datos GLOBALES| START -------------------------

box1 = ""
box2 = ""

floated = False
operation = "operation"

# ----- Almacenamiento de datos GLOBALES| END -------------------------

# ---------- Funciones Numéricas | START --------------------

def add1():
	global box2
	one = "1"
	box2 += one
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add2():
	global box2
	two = "2"
	box2 += two
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add3():
	global box2
	three = "3"
	box2 += three
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add4():
	global box2
	four = "4"
	box2 += four
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add5():
	global box2
	five = "5"
	box2 += five
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add6():
	global box2
	six = "6"
	box2 += six
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add7():
	global box2
	seven = "7"
	box2 += seven
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add8():
	global box2
	eight = "8"
	box2 += eight
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add9():
	global box2
	nine = "9"
	box2 += nine
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def add0():
	global box2
	zero = "0"
	box2 += zero
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def addPunto():
	global box2
	point = "."

	global floated
	floated = True

	box2 += point
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def addPI():
	global box2
	PI = "3.1416"

	global floated
	floated = True

	box2 += PI
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

# ---------- Funciones Numéricas | END --------------------

# ---------- Funciones Operacionales | START --------------------

def delBOX():
	global box2
	canvas = Canvas(window, bg="white", width=233, height=38.5)
	canvas.place(x=0, y=0)
	box1 = ""
	box2 = ""
	label = Label(window, text=box1, bg="white", font="Avenir").place(x=5, y=10)

def X_cuadrado():
	global box2

	if floated == True:
		box2 = float(box2) * float(box2)
	else:
		box2 = int(box2) * int(box2)

	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def Suma():
	global box1
	global box2
	box1 = box2
	box2 = ""

	global operation
	operation = "+"

	canvas = Canvas(window, bg="white", width=233, height=38.5)
	canvas.place(x=0, y=0)
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)


def Resta():
	global box1
	global box2
	box1 = box2
	box2 = ""

	global operation
	operation = "-"

	canvas = Canvas(window, bg="white", width=233, height=38.5)
	canvas.place(x=0, y=0)
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)


def Mult():
	global box1
	global box2
	box1 = box2
	box2 = ""

	global operation
	operation = "*"

	canvas = Canvas(window, bg="white", width=233, height=38.5)
	canvas.place(x=0, y=0)
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)


def Division():
	global box1
	global box2
	box1 = box2
	box2 = ""

	global operation
	operation = "/"

	canvas = Canvas(window, bg="white", width=233, height=38.5)
	canvas.place(x=0, y=0)
	label = Label(window, text=box2, bg="white", font="Avenir").place(x=5, y=10)

def Result():
	global operation
	global floated
	result = None

	""" Evalúa si hay flotante o no con addPunto() """
	if operation == "+":
		if floated == True:
			result = float(box1) + float(box2)

		elif floated == False:
			result = int(box1) + int(box2)

	elif operation == "-":
		if floated == True:
			result = float(box1) - float(box2)

		elif floated == False:
			result = int(box1) - int(box2)

	elif operation == "*":
		if floated == True:
			result = float(box1) * float(box2)

		elif floated == False:
			result = int(box1) * int(box2)

	elif operation == "/":
		if floated == True:
			result = float(box1) / float(box2)

		elif floated == False:
			result = int(box1) / int(box2)

	else:
		pass

	floated = False

	label = Label(window, text=result, bg="white", font="Avenir").place(x=5, y=10)


# ---------- Funciones Operacionales | END --------------------

# ______________________ ÁREA DE LÓGICA | PROCEDIMIENTO_______________________


# Método para añadir números a la variable de almacenamiento
# Al presionar una operación envía la información a la segunda variable y continúa con la primera
# Al presionar Igualdad(=) guarda la segunda variable y muestra el resultado de la operación

# ______________________ ÁREA DE INTERFAZ GRÁFICA | START _______________________

window = Tk()
window.title("Calculadora")
window.geometry("233x315+100+100")
window.resizable(width=False, height=False)

canvas = Canvas(window, bg="white", width=233, height=50)
canvas.place(x=0, y=0)


# Botones numéricos


btn7 = Button(window, text="7", width=6, height=3, command=add7, activebackground="lightgray").place(x= 0, y=95)
btn8 = Button(window, text="8", width=6, height=3, command=add8, activebackground="lightgray").place(x= 51, y=95)
btn9 = Button(window, text="9", width=6, height=3, command=add9, activebackground="lightgray").place(x= 102, y=95)
btn4 = Button(window, text="4", width=6, height=3, command=add4, activebackground="lightgray").place(x= 0, y=150)
btn5 = Button(window, text="5", width=6, height=3, command=add5, activebackground="lightgray").place(x= 51, y=150)
btn6 = Button(window, text="6", width=6, height=3, command=add6, activebackground="lightgray").place(x= 102, y=150)
btn1 = Button(window, text="1", width=6, height=3, command=add1, activebackground="lightgray").place(x= 0, y=205)
btn2 = Button(window, text="2", width=6, height=3, command=add2, activebackground="lightgray").place(x= 51, y=205)
btn3 = Button(window, text="3", width=6, height=3, command=add3, activebackground="lightgray").place(x= 102, y=205)
btn0 = Button(window, text="0", width=6, height=3, command=add0, activebackground="lightgray").place(x= 51, y=260)
btnPunto = Button(window, text=".", width=6, height=3, command=addPunto, activebackground="lightgray").place(x= 102, y=260)
btnPI = Button(window, text="π", width=6, height=3, command=addPI, activebackground="lightgray").place(x= 0, y=260)


btnDiv = Button(window, text="÷", width=10, height=3, command=Division, activebackground="lightgray").place(x= 153, y=40)
btnMult = Button(window, text="×", width=10, height=3, command=Mult, activebackground="lightgray").place(x= 153, y=95)
btnMenos = Button(window, text="-", width=10, height=3, command=Resta, activebackground="lightgray").place(x= 153, y=150)
btnMas = Button(window, text="+", width=10, height=3, command=Suma, activebackground="lightgray").place(x= 153, y=205)
btnResult = Button(window, text="=", width=10, height=3, command=Result, activebackground="lightgray").place(x= 153, y=260)


btnC = Button(window, text="DELETE", width=13, height=3, command=delBOX, activebackground="lightgray").place(x= 51, y=40)
btnCe = Button(window, text="x²", width=6, height=3, command=X_cuadrado, activebackground="lightgray").place(x= 0, y=40)

window.mainloop()

# ______________________ ÁREA DE INTERFAZ GRÁFICA | END _______________________

# ----------------------------- FIN DEL CÓDIGO -------------------------------------------

"""

	Recuerda: "El conocimiento es libre".

"""