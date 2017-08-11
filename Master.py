lista_palabras = "informatorio"

print (lista_palabras)


def menu_juego():
	s = False
	while s==False:
		
		print ("Opciones: ")
		print ("1-Iniciar Partida\n2 - Ranking\n3 - Salir del juego")

		ing = int(input ("ingrese una opcion: "))
		if ing ==3:
			s= True
			print ("Has salido del juego")

		
		if ing==1:
			
			print ("\nIniciando...\n\n")

			
			input()