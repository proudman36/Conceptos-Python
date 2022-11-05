print("Programa de becas.")
distanciaEscuela=int(input("Introduce la distancia a la escuela en kilometros: "))
print(distanciaEscuela)
numeroHermanos=int(input("Introduce el número de hermanos: "))
print(numeroHermanos)
salarioFamiliar=int(input("Introduce el salario anual bruto: "))
if distanciaEscuela>40 and numeroHermanos>2 or salarioFamiliar<=20000:
	print("Usted aplica para la beca")
else:
	print("No tienes derecho a la beca")

print("Asignaturas optativas")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()##Convierte todo el String que se ingrese en letras minúsculas, esto para facilitar el cumplimiento de la condición (que está toda en minúsculas)

if asignatura in("informática gráfica", "pruebas de software","usabilidad y accesibilidad"):
	print("Asignatura asignada " + opcion)
else:
	print("La asignatura escogida no está contemplada")