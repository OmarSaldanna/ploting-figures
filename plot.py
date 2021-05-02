import matplotlib.pyplot as plt

def figura(data, title):
	x, y, contorno, relleno = data
	# ploteamos la funcion como linea
	plt.plot(x, y, color=contorno)
	# rellenamos ese espacio
	plt.fill(x,y, color=relleno)
	# ajustamos el titulo
	plt.title(title)
	# ponemos la malla
	plt.grid()
	# y que sea cuadrada
	plt.gca().set_aspect("equal")
	plt.show()