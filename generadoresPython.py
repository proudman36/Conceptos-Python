#Los generadores son estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer)
#Dichos valores se almacenan de uno en uno
#Se nos devuelve un valor de uno en uno en un objeto iterable, luego de que devuelve un valor el generador queda en estado de espera para que lo vuelvan a llamar
#La sintaxis de un generador es la misma de una función, solo que en el caso del return se sustituye por yield
def funcioPares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista


print(funcioPares(10))

def generaPares(limite): #No hace falta crear la lista, pues el generador ya nos devuelve un objeto iterable
	num=1
	while num<limite:
		yield num*2
		num+=1

devuelvePares=generaPares(10) #Hay que crear una variable objeto, donde se almacena el objeto iterable que devuelve el generador

#for i in devuelvePares:
	#print(i)

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

def devuelveCiudades(*ciudades): #Esto es para indicarle al programa que va a recivir un número indeterminado de elementos y que esos argumentos los va a recivir en forma de tupla
	for i in ciudades:
#		for j in i:
			yield from i#Hace lo mismo que si se hiciera un bucle anidado, para obtener los datos dentro de otro dato


ciudades_devueltas=devuelveCiudades("Madrid", "Tokio","Barcelona","Valencia")
print(next(ciudades_devueltas))#Aquí con el yield from se obtiene la primera letra del primer elemento
print(next(ciudades_devueltas))#Con el yield from se obtiene la segunda letra del primer elemento


