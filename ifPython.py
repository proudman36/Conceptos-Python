print("Programa de evaluación de notas de alumnos")

nota_alumno=input()##Esto es para introducir un valor por teclado. Entre los paréntesis, con comillas, se puede especificar un mensaje antes de que se ingrese el valor

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion
print(evaluacion(int(nota_alumno)))##El int convierte el valor string que ingresa por el input, en un entero

