nombre_lista=["Maria","Pepe","Marta","Antonio"]

print(nombre_lista[1:3])
print(nombre_lista[2:])
nombre_lista.append("Sandra")##Agrega el elemento al final
nombre_lista.insert(2,"Ligia")##Agrega el elemento en el índice indicado
print(nombre_lista[:])
nombre_lista.extend(["Ana","Lucía","Berta"])##Agrega varios elementos al final de la lista
print(nombre_lista[:])
print(nombre_lista.index("Maria"))##Me muestra el índice del elemento que se especifica
print("Pepe" in nombre_lista)##Indica si un elemento se encuentra en mi lista
print("Jairo" in nombre_lista)
nombre_lista.extend([0,3,4,True])##En Python se pueden agregar datos de diferente tipo en una misma lista
print(nombre_lista[:])
nombre_lista.remove(0)##Elimina datos de la lista
print(nombre_lista[:])
nombre_lista.pop()##Elimina el último dato de la lista
print(nombre_lista[:])

miLista = ["Ramiro","Hector"]
miListaSuma= nombre_lista + miLista ##Suma los elementos de dos listas o más en otra
print(miListaSuma[:])
print(len(miListaSuma))