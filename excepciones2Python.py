def divide():
    try:
        op1=float(input("Introduce el primer número. "))
        op2=float(input("Introduce el segundo número. "))
        print("La división es: "+str(op1/op2))
    except ValueError:                          #Se pueden capturar varios errores a la vez
        print("El valor introducido es erróneo")
    except ZeroDivisionError:                  # Este sería el segundo error a capturar
        print("No se puede dividir entre 0")
    ##except:
        ##print("Ha ocurrido un error") ##Esto es para capturar un error en general, pero no es muy recomendado
    finally:  #Este es código que se ejecuta si se da o no se da el error, es decir, siempre se ejecuta 
        print("Cálculo finalizado")

divide()