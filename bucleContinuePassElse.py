for i in "Python":
	print("Viendo la letra "+i)

for i in "Python":
	if i=="h":
		continue##Esto lo que hace es saltarse una iteración del bucle, es decir si va en la iteración 5 y se pone un continue se salta esa iteración
	print("Viendo la letra "+i)

nombre = "Pildoras Informáticas"
contador = 0
for i in nombre:
	if i == " ":
		continue ##Con esto nos saltamos la iteración en la que se encuentre el espacio y el programa solo nos devuelve el número de letras
	contador+=1
print(contador)

##pass nos devuelve un valor null.

email =input("Introduce tu email, por favor. ")
for i in email:
	if i =="@":
		arroba=True
		break
else: ##Este se ejecuta justo después de que se haya llevado a cabo el ciclo completo, es decir, no es que se ejecute un instrucción u otra, sino que una se ejecuta después de la otra. Pero el else forma parte del bucle for, por lo que al hacer break, se sale también del else.
	arroba=False
print(arroba)