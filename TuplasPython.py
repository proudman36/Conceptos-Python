##En las tuplas no se puede eliminar, añadir, mover o cualquier otra acción similar con los elementos
##Se permite extraer porciones, pero la extracción es una tupla nueva.
##Sí se permite comprobar si hay un elemento en la tupla
nombreTupla=("Juan", 12,1,1995,12)
miLista=list(nombreTupla) ##Crea una copia como lista de la tupla
print(miLista[:])##Se nota que es una lista porque se muestra en corchetes en la consola
print(nombreTupla[2])
miListaEjm=["Ramiro",2,4,1997]
miTupla=tuple(miListaEjm)##Crea una copia como tupla de una lista
print(miTupla)##Se nota que es una tupla porque se muestra entre paréntesis
print("Juan" in nombreTupla)##Nos dice si un elemento se encuentra en la tupla
print(nombreTupla.count(12))##Cuenta cuantas veces se encuentra un elemento en la tupla
print(len(nombreTupla))##Nos imprime el largo de la tupla
tuplaUnitaria=("Robert",)##Se pueden crear tuplas unitarias pero se debe incluir una coma para que sea tupla
print(len(tuplaUnitaria))##Nos dice que la tupla solo tiene un elemento
tuplaEmpaquetada = "Juan", 13,1,1995 ##Se puede escribir una tupla sin los paréntesis, a esto se le conoce como empaquetado de tupla
print(tuplaEmpaquetada)
nombre,dia,mes,agno=tuplaEmpaquetada##Nos permite almacenar los valores de tupla en las diferentes variables que se han declarado a esto se le conoce como desempaquetado de tupla
print(nombre)
print(dia)
print(agno)
print(mes)