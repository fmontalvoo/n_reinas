import random

class NReinas:
	
	def __init__(self, n = 4):
		self.n = n
		self.soluciones = []
		self._ubicar_reinas(0)

	def _ubicar_reinas(self, row):
		if row == self.n:
			print("Termina")
			return True  # Indica que se encontró una solución
		
		print("Ingresa a fila:", row)
		columns = self._generar_aleatorios()
		print(columns)
		
		for col in columns:
			print("Fila:", row, "Columna:", col)
			if self._es_valido(row, col):
				self.soluciones.append((row, col))
				if self._ubicar_reinas(row+1):
					return True
				self.soluciones.pop()

		return False
	

	def _generar_aleatorios(self):
		# columns = []
		# while len(columns) < self.n:
		# 	rand = random.randint(0, self.n - 1)
		# 	if rand not in columns:
		# 		columns.append(rand)
		columns = list(range(self.n))
		random.shuffle(columns)
		return columns
			

	def _es_valido(self, row, col):
		#Si en el arreglo existe unicamente una reina, esta por defecto es una posicion valida
		for r, c in self.soluciones: #Recorre el arreglo de soluciones
			print("Entra >","Posicion Reina:", (r, c), "Posicion nueva:", (row, col))
			#Condicion para validar si la nueva posicion esta en una columna y diagonales distintas de las
			#Reinas ya ubicadas
			if c == col or abs(r - row) == abs(c - col):  
				print("NO Cumple >>>", "Posicion Reina:", (r, c), "Posicion nueva:", (row, col))
				return False
			else:
				print("Cumple >>>", "Posicion Reina:", (r, c), "Posicion Nueva:", (row, col))
		return True
	
	def imprimir_tablero(self):
		tablero = [['◻' for _ in range(self.n)] for _ in range(self.n)]

		print("Solución encontrada:", self.soluciones)
		for f, c in self.soluciones:
			tablero[f][c] = '♛'

		for fila in tablero:
			print(' '.join(fila))
