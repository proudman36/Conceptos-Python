for i in ["Primavera","Verano","Otoño","Invierno"]:##Repite cuatro veces el bucle, porque hay cuatro elementos en la lista
	print("Hola")

for i in ["Primavera","Verano","Otoño","Invierno"]:##Se le asigna un valor de la lista a i por eso es que se deben imprimir los elementos de la lista
	print(i)

for i in ["Pildoras","Informáticas",3]:
	print("Hola", end=" ")##Con esto se nos permite definir en qué queremos que termine la impresión, básicamente con eso se pueden escribir varios strings en este bucle, en una misma línea, y se deja un espacio entre las comillas para que se separen las palabras por un espacio.

for i in "proudman36@hotmail.com":##Esto hace que se recorra cada uno de los caracteres del String, por lo que la instrucción se repetirá tantas veces como haya caracteres en el String
	print("Correo")

email=False
for i in "proudman36@hotmail.com":##Esto recorre todos los caracteres del String y le asigna el valor del caracter al i

	if i=="@":##Esto nos permite saber si en el String hay un @
		email=True

if email==True:
	print("El email es correcto")
else:
	print("El email no es correcto")

arroba=False
punto=False
miEmail = input("Ingrese un correo electrónico: ")
for i in miEmail:
	if i=="@":
		arroba=True
	if i==".":
		punto=True

if arroba==True and punto==True:
	print("El email es valido.")
else:
	print("El email no es valido.")

contadora=0
contadorp=0

miEmail= input("Ingrese un correo electrónico: ")

for i in miEmail:
	if i=="@":
		contadora= contadora+1
	if i==".":
		contadorp= contadorp+1

if(contadora==1 and contadorp>0):
	print("El correo es valido")
else:
	print("El correo no es valido")

