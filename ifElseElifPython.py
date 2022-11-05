print("Verificación de acceso")
edad=int(input("Introduce tu edad por favor: "))
if edad<18:
	print("No puedes pasar")
elif edad>120:
	print("Edad incorrecta")
else:
	print("Puedes pasar")
print("El programa ha finalizado")

nota=int(input("Ingrese una nota por favor: "))
if nota<5:
	print("Insuficiente")
elif nota<6:
	print("Suficiente")
elif nota<7:
	print("Bien")
elif nota<9:
	print("notable")
elif nota<11:
	print("Sobresaliente")
else:
	print("Nota incorrecta")
