import os
import pickle


def limpiar():
	os.system("cls")
	print ("\t\t\tPALABRAS AHORCADO\n\t\t\t------------------\n\n")


def menu():
	print ("Ingrese una opcion:\n")
	print ("\n1 - Ingrese nueva palabra\n2 - Mostrar todas las palabras\n3 - Editar una palabra\n4 - Salir\n")
	op = input(" ")
	return opciones(op)


def opciones(op):
	if op=="1" or op=="2" or op=="3" or op=="4":
		if op=="1":
			return ingresar()
		if op=="2":
			return mostrar()
		if op=="3":
			limpiar()
			return editar()
		if op=="4":
			print ("\nSaliendo...\n\n")
			return False
	else:
		print ("Opcion no valida. pulse cualquier tecla para volver a cargar...")
		input()
		return True


def ingresar():
	limpiar()
	cad1 = input("Ingrese la nueva palabra:   ")
	cad2 = opref()
	print ("Palabra: ",cad1," ",cad2)
	while True:
		conf = input("\nConfirmar palabra nueva? (s para si, n para no):   ")
		if conf=="s" or conf=="n":
			if conf == "s":
				return crearincog(cad1,cad2)
				break
			if conf=="n":
				print ("\nOPERACION CANCELADA. Pulse una tecla para volver al menu principal...")
				input()
				return True
				break
		else:
			print ("Opcion no valida. Pulse cualquier tecla para volver a cargar...")


def opref():
	while True:
		print ("\nElija la referencia")
		print ("1 - Sinonimo\n2 - Breve referencia")
		op = input()
		if op=="1" or op=="2":
			if op=="1":
				print ("Ingrese Sinonimo:   ")
				cad = "Sinonimo: "
				cad += input()
				return cad
				break
			if op=="2":
				print ("Ingrese Referencia:  ")
				cad = input()
				return cad
				break
		else:
			print ("Opcion invalida... Ingrese nuevamente:\n")


def crearincog(cad1,cad2):
	incog = list()
	lista_incognitas = list()
	incog = [cad1,cad2]
	print (incog)
	try:
		archivo1 = open("Palabras.dat","rb")
		lista_incognitas = pickle.load(archivo1)
		archivo1.close()
	except IOError:
		archivo1 = open("Palabras.dat","wb")
		archivo1.close()
	archivo = open("Palabras.dat","wb")
	lista_incognitas.append(incog)
	pickle.dump(lista_incognitas,archivo)
	archivo.close()
	print ("\nPALABRA AGREGADA CON EXITO!")
	input()
	return True
 

def mostrar():
	limpiar()
	print ("Lista de palabras y referencias")
	archivo = open ("Palabras.dat", "rb")
	lista_incognitas = pickle.load(archivo)
	i=1
	for x in lista_incognitas:
		print ("\n",i,"- Palabra: ", x[0])
		print ("     Referencia: ", x[1])
		i+=1
	print ("\n\nVolver al menu principal...")
	archivo.close()
	input()
	return True


def editar():
	limpiar()
	print ("Lista de palabras. Ingrese el numero de palabra que desea editar:\n")
	archivo = open ("Palabras.dat", "rb")
	lista_incognitas = pickle.load(archivo)
	i=0
	for x in lista_incognitas:
		i+=1
		print ("\n",i,"- Palabra: ", x[0],"  -  Referencia: ",x[1])
	archivo.close()
	while  True:
		print ("\n\nElija el numero de palabra que desea editar. Pulse n para Volver al menu principal")
		op = input()
		if op.isdigit():
			inop = int(op)
			if inop<=i:
				i=0
				for x in lista_incognitas:
					if (inop-1)==i:
						print("\nPalabra:  ",x[0])
						while True:
							conf = input("\nConfirmar palabra a editar? (s para si, n para no):   ")
							if conf=="s" or conf=="n":
								if conf == "s":
									return edmenu((inop-1),lista_incognitas)
									break
									break
								if conf=="n":
									print ("\nOPERACION CANCELADA. Pulse una tecla para volver al menu principal...")
									input()
									return True
									break
							else:
								print ("Opcion no valida. pulse cualquier tecla para volver a cargar...")
					i+=1
			else:
				print ("Opcion invalida (palabra no existe)... Ingrese nuevamente:\n")
		else:
			if op=="n":
				return True
				break
			else:
				print ("Opcion invalida... Ingrese nuevamente:\n")


def edmenu(inop, lista_incognitas):
	i =0
	for x in lista_incognitas:
		if i==inop:
			cad = x[0]
			cad2 = x[1]
			break
		i+=1
	while True:
		limpiar()
		print("Palabra:  ", cad,"     Referencia: ",cad2)
		print ("\n\nElija una opcion\n\n1 - Modificar\n2 - Eliminar\n3 - Volver menu principal")
		op = input()
		if op=="1" or op=="2" or op=="3":
			if op=="1":
				return modificar(inop,lista_incognitas)
			if op=="2":
				return eliminar(inop,lista_incognitas)
			if op=="3":
				return True
				break
		else:
			print ("Opcion invalida... Pulse cualquier tecla para ingresar nuevamente una opcion...\n")
			input()


def eliminar(inop,lista_incognitas):
	while True:
		conf = input("\n¿Eliminar palabra? (s/n):  ")
		if conf=="s" or conf=="n":
			if conf=="s":
				print ("\n",lista_incognitas[inop])
				lista_incognitas.pop(inop)
				archivo = open("Palabras.dat","wb")
				pickle.dump(lista_incognitas,archivo)
				archivo.close()
				print ("PALABRA ELIMINADA CON EXITO!")
				input()
				return True
			if conf=="n":
				print ("\nOPERACION CANCELADA. Pulse una tecla para volver al menu principal...")
				input()
				return True
				break
		else:
			print ("Opcion invalida... Ingrese nuevamente:\n")


def modificar(inop,lista_incognitas):
	palmod = input("\nIngrese la nueva palabra:  ")
	f = True
	while f:
		conf1 = input("\n¿Desea modificar la referencia? (s/n)")
		if conf1=="s" or conf1=="n":
			if conf1=="s":
				while True:
					print ("Elija la nueva referencia")
					print ("\n1 - Sinonimo\n2 - Breve referencia")
					op = input()
					if op=="1" or op=="2":
						if op=="1":
							print ("Ingrese Sinonimo:   ")
							cad = "Sinonimo: "
							cad += input()
							f = False
							break
						if op=="2":
							print ("Ingrese Referencia:  ")
							cad = input()
							f = False
							break
					else:
						print ("Opcion invalida... Ingrese nuevamente:\n")
			if conf1=="n":
				cad = lista_incognitas[inop][1]
				break
		else:
			print ("Opcion invalida... Ingrese nuevamente:\n")
	print ("\nPalabra: ",palmod,"     Referencia: ",cad)
	incog = list()
	incog = [palmod,cad]
	lista_incognitas[inop] = incog
	return okmod(lista_incognitas)


def modmenu():
	pass


def okmod(lista_incognitas):
	while True:
		conf = input("\n¿Confirmar modificacion de palabra? (s para si, n para no):   ")
		if conf=="s" or conf=="n":
			if conf == "s":
				archivo = open("Palabras.dat","wb")
				pickle.dump(lista_incognitas,archivo)
				archivo.close()
				print ("\nPALABRA MODIFICADA CON EXITO!")
				input()
				return True
				break
			if conf=="n":
				print ("\nOPERACION CANCELADA. Pulse una tecla para volver al menu principal...")
				input()
				return True
				break
		else:
			print ("Opcion no valida. Pulse cualquier tecla para volver a cargar...")
	
	


flag = True

while flag:
	limpiar()
	flag = menu()