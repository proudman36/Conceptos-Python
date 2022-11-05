class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena)

class Moto(Vehiculo): #Se pone el nombre de la clase de la que se hereda
    hcaballito = ""
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenado: ",self.frena,"\n",self.hcaballito)#Esto es sobreescritura de métodos, para que funcione debe tener el mismo número de argumentos

moto=Moto("Honda", "CBR") ##Se deben poner los dos argumentos para que el constructor funcione
moto.caballito()
moto.estado()#La clase Moto hereda todos los atributos y métodos de la clase Vehiculo

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado == True:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

furgon=Furgoneta("Renault", "Kangoo")#Hay que poner los dos argumentos, pues Furgoneta hereda el constructor de Vehiculo
furgon.arrancar()
furgon.estado()
print(furgon.carga(True))#Hay que poner el argumento pues este se define en el método y es de tipo booleano

class VElectricos(Vehiculo):
    def __init__(self,marca_elec,modelo_elec):
        super().__init__(marca_elec,modelo_elec)
        autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class  BicicletaElectrica(VElectricos,Vehiculo):#Esto es herencia multiple. El constructor se toma de la clase que esté en el primer argumento.
    pass#Esta clase hereda tanto de VElectricos como de Vehiculo, pero toma preferencia el que esté como argumento más a la izquierda

bicicleta=BicicletaElectrica("Road","AM232")#No se pone ningún argumento, pues la clase de BicicletaElectrica hereda el constructor de VElectricos y este no tiene argumentos#Ahora con el super() si se pueden poner argumentos para darle una marca y un modelo

bicicleta.estado()
