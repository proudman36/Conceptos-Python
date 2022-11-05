#Las excepciones son errores que surgen en el código de manera inesperada, como el NullPointerException en Java
def suma(num1,num2):
	resultado=num1+num2
	return resultado

def resta(num1,num2):
	resultado=num1-num2
	return resultado

def multiplica(num1,num2):
	resultado=num1*num2
	return resultado

def division(num1,num2):
	try:
		resultado=num1/num2
		return resultado
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return"Operación errónea"
while True: #Siempre va a ser cierto, por lo que se tiene un bucle infinito
	try:
		op1=(int(input("Ingresa el primer número entero: ")))#Si el valor no es correcto, pasa de una vez al except, mientras que si es correcto lee las dos líneas siguientes de código y por lo tanto al break
		op2=(int(input("Ingresa el segundo número entero: ")))
		break
	except ValueError:
		print("Los valores introducidos no son correctos")
operacion=input("Introduce la operación a realizar(suma, resta, multiplicación, división (ingresar sin tíldes)): ")
operacionMin=operacion.lower()

if operacionMin=="suma":
	print(suma(op1,op2))
elif operacionMin=="resta":
	print(resta(op1,op2))
elif operacionMin=="multiplicacion":
	print(multiplica(op1,op2))
elif operacionMin=="division":
	print(division(op1,op2))
else:
	print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")