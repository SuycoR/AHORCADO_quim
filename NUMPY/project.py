import random

class Ahorcado:

	def __init__(self):
		self.palabras = ["elefante","raton","gato","perro","jirafa","foca"]
		self.contador = -1 #Posicion del arreglo de palabras
		self.palabraJugador = ""
		self.vidas = 5

	def iniciar(self):
		self.contador = random.randint(0,len(self.palabras)-1)
		self.palabraJugador = ["*" for x in self.palabras[self.contador]]
		print(self.palabraJugador)

	def adivinar(self):
		letra = input("Escribe la letra: ")
		bandera = False #Para verificar si el usuario adivinó la letra
		for i in range(len(self.palabras[self.contador])):
			if letra==self.palabras[self.contador][i]:
				self.palabraJugador[i] = self.palabras[self.contador][i]
				bandera = True
		if bandera==False:
			self.vidas = self.vidas - 1

	def comprobar(self):
		if "*" not in self.palabraJugador:
			print("Ganaste :D ")
			return True
		elif self.vidas == 0:
			print("Perdiste :( ")
			return True
		else:
			return False

obj = Ahorcado()
obj.iniciar()
while obj.comprobar()==False:
	obj.adivinar()
	print("****Actual****")
	print(obj.palabraJugador)
	print("Te quedan " + str(obj.vidas) + " vidas")