class Coche():

    def __init__(self): #Constructor, en el constructor siempre se pone el self. antes del atributo

        self.__largoChasis=250 #Atributos
        self.__anchoChasis=120
        self.__ruedas=4 #Los dos guiones bajos son para encapsular el atributo. Es como el private en java
        self.__enmarcha=False


    def arrancar(self,arrancamos): #Métodos, todos requieren el self como argumento
        self.__enmarcha=arrancamos
        if self.__enmarcha==True:
            chequeo=self.__check()
        if self.__enmarcha==True and chequeo==True:
            return "El coche está en marcha"
        elif self.__enmarcha == True and chequeo==False:
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"
    
    def estado(self):
            print("El coche tiene "+ str(self.__ruedas)+ " ruedas. Un ancho de "+str(self.__anchoChasis)+" y un largo de "+ str(self.__largoChasis))

    def __check(self): #Con los dos guiones bajos se encapsula al método para que solo se pueda usar en la clase, de este modo no se podrá invocar el método por fuera de la clase ya que no tendría sentido en este caso (mirar vido 29 )
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="wrong"
        self.puertas="cerradas"
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False
ferrari = Coche()
print(ferrari.arrancar(True))#Con el método arrancar se puede acceder al atributo 
ferrari.estado()

print("--------------A continuación creamos el segundo objeto-------------------------")

tesla = Coche()
print(tesla.arrancar(False))
tesla.__ruedas=5 #Como el atributo no es accesible por fuera de la clase, pues está encapsulada, no se puede cambiar el valor de las ruedas por fuera de la clase 
tesla.estado()