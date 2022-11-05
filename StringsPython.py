cadena="hola Mundo"
cadenaMin=cadena.lower()#Este método se utiliza para pasar todas las letras a mínuscula
cadenaMay=cadena.upper()#Convierte todas las letras a mayúsculas
cadenaPrimMay=cadena.capitalize()#Convierte la primera letra del String en mayúscula

print(cadenaMin)
print(cadenaMay)
print(cadenaPrimMay)

edad="22"
print(edad.isdigit())#El isdigit nos devuelve si un String es un entero, nos devuelve un valor booleano 

cadena="Pepito Perez se comió un gusanito"
print(cadena.count("Pe"))#count nos cuenta cuantas veces aparece un caracter o cadena de caracteres
print(cadena.find("se"))#find nos indica el índice en el que aparece un caracter o cadena de caracteres, solo nos indica la primera vez que aparece

cadena="34332manchita"
print(cadena.isalnum())#Nos dice si el String es alfanumérico, si hay un espacio deja de contar
print(cadena.isalpha())#Nos dice si el String solo tinen letras, lo mismo de los espacios cuenta aquí

cadena="oh my"
print(cadena.split())#Nos devuelve una lista con los elementos separados por un espacio, es decir los que se encuentran separados por un espacio se ven como distintos elementos de una lista
palabra=cadena.split()#Esto puede servir para contar palabras en un String
print(len(palabra))#Aquí se nos devuleve el número de palabras que hay en un String
cadena="This is a string"
print(cadena.split("s"))#En este caso los elementos se ven separados por la aparición de la s minúscula, es decir ahora se dividen por la aparición de la s y esta no se muestra
print(cadena.split(maxsplit=1))#Le indica cuantas veces debe hacer la separación, en este caso por el espacio, y por lo tanto como es 1 no lo va a repetir, generándonos solo dos elementos en la lista de ejemplo
#https://www.youtube.com/watch?v=-yzfxeMBe1s

cadena=" hola mundo "
print(cadena.strip())#Este método borra los espacios sobrantes al comienzo y al final

cadena="jaula"
nombre=cadena.replace("j","p")#Esto nos sustituye la letra j por la letra p
print(nombre)

cadena="abcde"
print(cadena.rfind("e"))#Nos indica el indice en el que aparece la palabra o letra

