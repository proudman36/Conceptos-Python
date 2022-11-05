miDiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
print(miDiccionario["España"])##Nos muestra el elemento guardado con esa clave
print(miDiccionario)##Nos muestra todo el diccionario
miDiccionario["Italia"]="Florencia" ##Esto agrega un nuevo elemento al diccionario
miDiccionario["Italia"]="Roma" ##Esto sobreescribe la clave con el nuevo valor que se le ha asignado
print(miDiccionario)
del miDiccionario["Reino Unido"] ##Esto elimina un elemento del diccionario
print(miDiccionario)
dicNuev={23:"Jordan","Mosqueteros":3}##Se pueden almacenar datos de distinto tipo en un mismo diccionario
print(dicNuev["Mosqueteros"])
miTupla=("Colombia","Ecuador","Brasil","Argentina")
dicTupla={miTupla[0]:"Bogotá",miTupla[1]:"Quito",miTupla[2]:"Brasilia",miTupla[3]:"Buenos Aires"}
print(dicTupla["Colombia"]) ##Con el código anterior se le asigno un valor a cada clave que forma parte de la tupla
dicTupla1={"Anillos":(1991,1992,1993,1996,1997,1998)}##Con este código se añade una tupla completa con la calve anillos
print(dicTupla1)
print(dicTupla1.keys())##Nos devuelve todas las claves que pertencen al diccionario
print(dicTupla1.values())##Nos imprime todos los valores que contienen las claves
print(len(dicTupla1))##Nos devuelve el número de parejas que contiene el diccionario