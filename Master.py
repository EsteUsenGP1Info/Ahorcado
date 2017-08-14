# lista_palabras = "informatorio"

# print (lista_palabras)






import os

def limpiar():
	os.system("cls")
	print("         BIENVENIDO AL AHORCADO")


def menu_juego():
		limpiar()
		print ("                  MENU  ")
		print("           *****************")
		print ("          1-Iniciar Partida\n          2-Ranking de Puntos\n          3-Salir del juego")
		print("           *****************")
		print()

		ing = int(input ("Elija una opcion: "))
		if ing==1:
			limpiar()		
			palabra=input("Ingrese una letra: ")

		if ing ==2:
			limpiar()
			print (" \n      RANKING DE PUNTOS\n")
			print("   1-Punisher: 3000 Pts.")
			print("   2-Deathstroke: 2500 Pts.")
			print("   3-Spiderman: 1000 Pts.")
			print()
			opcion=input( "Quiere elegir otra opcion?: si/no   ")
			if opcion=="si":
				return True
			else:
				print ("Has salido del juego")
				return False

		if ing ==3:
			return False
			print ("Has salido del juego")

s = True

while s==True:
	limpiar()
	s=menu_juego()
=======
lista_palabras = list()

import random
import pickle
num = random.randint(0,10)


#Esta Funcion busca la incognita y la referencia de la lista principal. Devuelve dos cadenas,"palabra" y "referencia".
def buscar_lista():
	archivo = open("palabras.dat","rb")
	lista_palabras = pickle.load(archivo)
	archivo.close()
	palref = list()
	palref = random.choice(lista_palabras)
	palabra = palref[0]
	referencia = palref[1]
	return palabra, referencia

def seleccionar_lista():
	seleccion = random.choice(lista_palabras)
	aux = len(seleccion[0])
		for x in range(aux):
				auxlista = auxlista.replace(seleccion[x], " _ ")
	return auxlista

def Crearlista():
	lista = ["Mauricio","Alan","Marina","Facundo"]
	devuelve = random.choice(lista)
	return devuelve

def Calculalongitud():
	longitud = len(lista[num])
	print ("El numero de letras en la palabra es: ")
	return longitud

incognita, referencia = buscar_lista()
print ("\nPalabra: ",incognita,"     - Referencia: ",referencia)
print ("\nFin...")