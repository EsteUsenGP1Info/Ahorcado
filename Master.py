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