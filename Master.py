lista_palabras = "informatorio"
import random
num = random.randint(0,10)

def Crearlista():
	lista = ["Mauricio","Alan","Marina","Facundo"]
	devuelve = random.choice(lista)
	return devuelve

def Calculalongitud():
	longitud = len(lista[num])
	print "El numero de letras en la palabra es: "
	return longitud


def seleccionar_lista():
	seleccion = random.choice(lista_palabras)
	aux = len(seleccion[0])
		for x in range(aux):
				auxlista = auxlista.replace(seleccion[x], " _ ")
	return auxlista