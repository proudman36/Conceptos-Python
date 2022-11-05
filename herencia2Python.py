class Persona():
    
    def __init__ (self, nom, edad,lug_res):
        self.nombre=nom
        self.edad=edad
        self.lugarRes=lug_res
    
    def descripcion(self):
        print("Nombre ",self.nombre,"Edad ",self.edad,"Lugar de Residencia ",self.lugarRes)

class Empleado(Persona):
    def __init__( self,sal,antigu,nom_empleado,edad_empleado,res_empleado):
        super().__init__(nom_empleado,edad_empleado,res_empleado)#Con esto se inicia el constructor de la clase padre y se le establecen los argumentos correspondientes
        self.salario=sal
        self.antiguedad=antigu
    
    def descripcion(self):#Cuando se llame al método descripcion desde una clase empleado, se llama a este método en lugar del de la clase padre
        super().descripcion()#Con esto se llama al descripcion de la clase padre y se ejecuta su código
        print("El salario es de ",self.salario,"La antigüedad del empleado es de ",self.antiguedad)
    
#mi_empleado=Empleado("Antonio",25,"España")No se puede pues el constructor de empleado pide tres parámetros (contando el self), y le estamos pasando cuatro
#mi_empleado.descripcion() No se puede llamar al método pues el constructor tiene argumentos diferentes

#mi_empleado=Empleado(1500, 15)#Con esto se llama al constructor de la clase Empleado y se le pasan los argumentos
#mi_empleado.descripcion()#Con el super() se puede llamar este método pues ya se iniciaron las variables del constructor de la clase padre

mi_empleado=Empleado(1500, 15,"Manuel",55,"Colombia")#Ahora que se han puesto argumentos extra en el constructor de la clase Empleado se pueden poner más datos para iniciar el constructor de la clase Persona
mi_empleado.descripcion()

print(isinstance(mi_empleado, Empleado))#Esto nos devuelve con un valor booleano si un objeto es una instancia de una clase en particular, en este caso si es de tipo Empleado
print(isinstance(mi_empleado, Persona))#Esto nos dice si es una instancia de la clase Persona, que lo es, porque Empleado hereda de Persona

mi_persona=Persona("Hector",35,"Bogotá")
print(isinstance(mi_persona, Empleado))#En este caso nos devuelve un False pues Persona no hereda de Empleado y aplicando lógica una persona no es necesariamente un empleado
