from figuras import Circulo, Cuadrado, Triangulo
from plot import figura
from tkinter import ttk
import tkinter as tk

if __name__ == '__main__':
	##################################### Ejemplos de puntos

	# cuadrado (1,1),(4,4)
	# triangulo (4,2),(8,2),(6,7)
	# colores black,lightblue

	##################################### funciones
	
	# regresara el color de relleno y contorno
	def read_colors():
		return colors.get().split(',')

	# leer puntos para cuadrados o para triangulos
	def read_points():
		# quitar parentesis y comas intermedias
		text = data.get().split('),(')
		text[0] = text[0][1:] # borar el primero
		text[len(text)-1] = text[len(text)-1][:len(text[len(text)-1])-1] # borar el ultimo
		# la lista de puntos
		puntos = []
		for p in text:
			point = p.split(',')
			x = float(point[0])
			y = float(point[1])
			puntos.append((x,y))
		return puntos

	# funcion que se activa al presionar el boton
	def action():
		# leemos el menu
		cat = combo.get()
		# leemos los colores
		contorno, relleno = read_colors()
		# dependiendo de cada cat la figura

		if cat == 'Circulo':
			# leemos directamente el radio
			radio =  int(data.get())
			# instanciamos la clase la figura
			circulo = Circulo(radio, contorno, relleno)
			# y ploteamos la figura
			figura(circulo.plot(), circulo)

		elif cat == 'Cuadrado':
			puntos = read_points()
			# instanciamos la clase la figura
			cuadrado = Cuadrado(puntos, contorno, relleno)
			# y ploteamos la figura
			figura(cuadrado.plot(), cuadrado)

		else:
			puntos = read_points()
			# instanciamos la clase la figura
			triangulo = Triangulo(puntos, contorno, relleno)
			# y ploteamos la figura
			figura(triangulo.plot(), triangulo)


	##################################### crear la ventana
	bg = 'gray4'
	fg = 'white'
	window=tk.Tk()
	window.title("Graficas de Poligonos")
	window.geometry('750x700')
	window.configure(background=bg)
	# puente de variables para el resultado
	bridge = tk.StringVar()

	##################################### etiquetas de texto
	
	label_1 = tk.Label(window, text='Graficadora de Poligonos', bg=bg, fg=fg)
	label_1.config(font=("Courier", 40))
	label_1.pack(padx=10,pady=10,ipadx=5,ipady=5, fill=tk.X)

	label_2 = tk.Label(window, text='Instrucciones', bg=bg, fg=fg, anchor='w')
	label_2.config(font=("Courier", 30))
	label_2.pack(padx=10,pady=5,ipadx=5,ipady=5, fill=tk.X)

	labs = ['-> Circulo: ingresa el radio del circulo',
			'-> Cuadrado: Ingresa los puntos de su diagonal',
			'-> Triangulo: ingresa todos sus puntos',
			'-> Luego ingresa el color del borde y el relleno',
			'!importante, NO PONER ESPACIOS ENTRE COMAS O PUNTOS.']

	for lab in labs:
		label = tk.Label(window, text=lab, bg=bg, fg=fg)
		label.config(font=("Courier", 22))
		label.pack(padx=10,pady=6,ipadx=5,ipady=5, anchor='w')

	##################################### entrada de texto y menu
	
	# entrada para los datos
	data = ttk.Entry(window)
	data.insert(0, 'Datos Aqui')
	data.pack(padx=10,pady=10,side=tk.TOP)

	# entrada para el color y relleno
	colors = ttk.Entry(window)
	colors.insert(0, 'Borde,Relleno')
	colors.pack(padx=10,pady=10,side=tk.TOP)

	# menu para las figuras
	combo = ttk.Combobox(window)
	combo["values"] = ['Circulo', 'Cuadrado', 'Triangulo']
	combo.current(0)
	combo.pack(padx=10,pady=10,side=tk.TOP)


	##################################### boton de graficar

	button = tk.Button(window, text="Graficar Figura", fg="blue", command=action)
	# renderiza el boton de mult
	button.pack(padx=10,pady=10,side=tk.TOP)

	# metodo para cerrar
	def close():
		window.destroy()

	# agregamos un boton de cerrar
	botoncerrar = tk.Button(window,text="Cerrar", fg="red", command=close)
	botoncerrar.pack(padx=10,pady=10,side=tk.TOP)

	# esto es como comenzar a renderizar la pantalla
	window.mainloop()