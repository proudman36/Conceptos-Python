for i in range(5):##Crea una lista de cinco elementos, contando desde la posición cero, que será recorrida.
	print("Hola")
	print(i)##Nos imprime el valor que va adquiriendo i

for i in range(5):
	print(f"Valor de la variable  {i}")

for i in range(5,10):##Se indica desde donde empieza el conteo, en el ejemplo desde cinco, hasta donde, en el ejemplo hasta el nueve (porque no se cuenta el diez)
	print(f"Valor de la variable {i}")

for i in range(5,50,3):##El último argumento le indica de a cuantos números debe contar.
	print(f"Valor de la variable {i}")

valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido==True:
	print("Su correo tiene un @")
else:
	print("Su correo no tiene un @")
	