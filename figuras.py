import numpy as np

class Figura:
	def __init__ (self, contorno, relleno):
		self.contorno = contorno
		self.relleno = relleno

# los str de cada clase estan definidas para ser pasadas como el
# titulo del plot, de forma que solo pasamos el nombre de la clase
# y ya no hay que formatear texto fuera de las clases, mas facil.

class Circulo(Figura):
	def __init__(self, radio, contorno, relleno):
		self.radio = radio
		Figura.__init__(self, contorno, relleno)

	def area(self):
		return round((self.radio**2) * 3.1416, 4)

	def perimetro(self):
		return round(2 * self.radio * 3.1416, 3)

	# retorna los puntos para el plot, y los colores
	def plot(self):
		x = np.linspace(-self.radio, self.radio, 200)
		# esta ecuacion da medio circulo, falta el otro medio
		y = np.sqrt(self.radio**2 - x**2)
		# agregamos los mismos valores de x para
		# que no afecte el tema de la dimensiom
		x = np.concatenate((x, x))
		# multiplicamos los valores de y por -1 para tener
		# la mitad negativa del circulo, y los agregamos
		y = np.concatenate((y,y[::-1]*(-1)))
		return x,y,self.contorno, self.relleno

	def __str__(self):
		return f'Cuadrado de perimetro {self.perimetro()} y area {self.area()}'


class Cuadrado(Figura):
	# se inicia con los dos puntos que componen la diagonal
	def __init__(self, diagonales, contorno, relleno):
		self.d1 = list(diagonales[0])
		self.d2 = list(diagonales[1])
		Figura.__init__(self, contorno, relleno)
		# sacamos la diagonal y luego los otros 2 lados
		self.__lados()
		
	def __lados(self):
		# hacemos los procedimientos previos
		self.__diagonal()
		self.__cateto()
		# y sacamos los lados
		self.lados = []
		# los ponemos en orden
		self.lados.append(self.d1)
		# al primero le sumamos en x el lado
		self.lados.append([self.d1[0]+self.lado, self.d1[1]])
		self.lados.append(self.d2)
		# y al segundo en y
		self.lados.append([self.d1[0], self.d1[0]+self.lado])

	def __cateto(self):
		h = self.diagonal
		self.lado = np.sqrt((h**2)/2)

	# privado, sacar la longitud de la diagonal
	def __diagonal(self):
		# sacamos la diagonal
		self.diagonal = self.__distancia(self.d1, self.d2)

	# privado sacar la distancia entre dos puntos
	def __distancia(self, p1, p2):
		suma1 = (p2[0]-p1[0])**2
		suma2 = (p2[1]-p1[1])**2
		return np.sqrt(suma1 + suma2)

	def area(self):
		return round(self.lado**2)

	def perimetro(self):
		return round(self.lado*4)

	def plot(self):
		x,y = [],[]
		# tomamos x,y de cada punto o lado
		for lado in self.lados:
			x.append(lado[0])
			y.append(lado[1])
		# agregamos el primer vertice otra vez
		# para que cierre el contorno del plot
		x.append(self.lados[0][0])
		y.append(self.lados[0][1])
		return x,y,self.contorno, self.relleno

	def __str__(self):
		return f'Cuadrado de perimetro {self.perimetro()} y area {self.area()}'



# solo triangulos equilateros e isoceles
class Triangulo(Figura):
	def __init__ (self, puntos, contorno, relleno):
		self.puntos = puntos
		Figura.__init__(self, contorno, relleno)
	
	# privado sacar la distancia entre dos puntos
	def __distancia(self, p1, p2):
		suma1 = (p2[0]-p1[0])**2
		suma2 = (p2[1]-p1[1])**2
		return np.sqrt(suma1 + suma2)

	def __punto_medio(self, p1, p2):
		return [(p1[0] + p2[0])/2, (p1[1] + p2[1])/2]
	
	def area(self):
		# puntos requeridos para scar la base
		puntos_base = self.puntos[:2]
		# sacamos la base que es la distancia entre los puntos base
		base = self.__distancia(puntos_base[0], puntos_base[1])
		# sacamos el punto medio entre los dos de la base
		punto_medio = self.__punto_medio(self.puntos[0], self.puntos[1])
		# la altura sera la distancio entre el punto medio y el tercer punto
		altura = self.__distancia(punto_medio, self.puntos[2])
		# retornamos el area
		return round((base*altura)/2, 4)

	def perimetro(self):
		# puntos requeridos para scar la base
		puntos_base = self.puntos[:2]
		# sacamos la longitud de cada lado
		base = self.__distancia(puntos_base[0], puntos_base[1])
		lado1 = self.__distancia(puntos_base[0], self.puntos[2])
		lado2 = self.__distancia(puntos_base[1], self.puntos[2])
		# el perimetro es tres veces la base
		return round(base + lado1 + lado2, 4)

	def plot(self):
		x,y = [],[]
		for lado in self.puntos:
			x.append(lado[0])
			y.append(lado[1])
		# agregamos el primer vertice otra vez
		# para que cierre el contorno del plot
		x.append(self.puntos[0][0])
		y.append(self.puntos[0][1])
		return x,y,self.contorno, self.relleno

	def __str__(self):
		return f'Triangulo de perimetro {self.perimetro()} y area {self.area()}'

