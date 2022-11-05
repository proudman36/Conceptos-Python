class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas.")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas.")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando sies ruedas.")

#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

def desplazamientoVehiculos(vehiculos):#Con el polimorfismo, el objeto vehiculos puede tener la capacidad de cambiar de forma y de comportarse de distinta forma dependiendo del contexto
    vehiculos.desplazamiento()#Vehiculos llama al método correspondiente del objeto del que toma la forma

miVehiculo=Camion()
desplazamientoVehiculos(miVehiculo)#Con esto se llama al método desplazamiento de la clase Camion pues el argumento de tipo objeto es un objeto de tipo Camion

miVehiculo2=Moto()
desplazamientoVehiculos(miVehiculo2)
