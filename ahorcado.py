import time
def ahor():

	print(" ")
	nombre = input("¿Como te llamas?  ")
	print(" ")
	print("Hola " + nombre, " Es hora de jugar al ahorcado")
	print(" ")
	time.sleep(1)
	print("Comienza a adivinar")
	print(" ")
	time.sleep(0.5)
	print(" ")
	palabra='sudestada'
	tupalabra=''
	vidas=5

	while vidas > 0:
		fallas=0
		for letra in palabra:
			if letra in tupalabra:
				print(letra,end="")
			else:
				print("*",end="")
				fallas+=1
		if fallas == 0:
			print("")
			print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Felicidades, ganaste!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			break
		print('\n')
		tuletra = input("Introduce una letra: ")
		tupalabra += tuletra

		if tuletra not in palabra:
			vidas -= 1
			print("Equivocaión")
			print("Tu tienes", +vidas, "vidas")
		if vidas == 0:

			print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡PERDISTE", nombre, "JAJAJAJ !!!!!!!!!!!!!!!!!!!!!!")
	else:
		print("Gracias por participar!")
		print("Queres volver a jugar??")
	print("")
	opcion = input("Ingrese si = para volver a jugar, no = para salir: ")
	if opcion == "si":
		return ahor()
	else:
		print("Gracias por jugar!!")

ahor()