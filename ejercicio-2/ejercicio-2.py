# Ejercicio-2
#programa que permita realizar un préstamo bancario,teniendo en cuenta que el préstamo será otorgado solamente a personas con ingresos superiores a $945200 y que no posea ninguna otra deuda.

#input
n=int(input("Ingrese el valor de sus ingresos : "))

opcion=int(input("tiene alguna deuda bancaria elija una opción de las siguientes: Menu\n1.Si\n2.No\nfavor ingresar opcion: "))

#Pocesing
if (n>945200) and opcion>=2:
    print("El prestamo es concedido")
else:
    print("El prestamo no puede ser concedido")
    
    

    

    


