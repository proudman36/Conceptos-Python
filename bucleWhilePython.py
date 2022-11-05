import math
i=1
while i<=10:
	print("Ejecución "+str(i))
	i=i+1

print("Terminó la ejecución")

edad=int(input("Ingrese una edad "))
while edad<0 or edad>120:
	print("Edad incorrecta")
	edad=int(input("Ingrese una edad "))
print("Tu edad es de: "+str(edad)+" años")

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número entero por favor: "))

intentos = 0

while numero<0:
	print("No se puede hallar la raíz de un número negativo")
	if intentos==2:
		print("Has consumido demasiados intentos el programa ha finalizado")
		break
	numero=int(input("Introduce un número entero por favor: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de "+str(numero)+" es "+str(solucion))

