edad = int(input("Ingrese una edad: "))

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad incorrecta")

salarioPresidente=int(input("Introduce salario presidente: "))
print("Salario presidente: "+str(salarioPresidente))
salarioDirector=int(input("Introduce salario director: "))
SalarioJefeArea=int(input("Introduce salario jefe área: "))
print("Salario jefe área: "+str(SalarioJefeArea))
salarioAdministrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo: "+str(salarioAdministrativo))
if salarioAdministrativo<SalarioJefeArea<salarioDirector<salarioPresidente:
	print("Los salarios están acorde al cargo")
else:
	print("Los salarios no cuadran")
