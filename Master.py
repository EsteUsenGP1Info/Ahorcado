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
				auxlista = aux.replace(seleccion[x], " _ ")
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