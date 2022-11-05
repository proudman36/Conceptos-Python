edad=input("Ingrese su edad ")
while edad.isdigit()==False:
    edad=input("Ingrese una edad adecuada ")

if int(edad)<18:
    print("No puedes pasar")
else:
    print("Puedes pasar")