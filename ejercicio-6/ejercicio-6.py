#ejercicio-6
# programa para determinar las raices de un ecuación cuadratica de coeficientes reales
from  math import sqrt
import cmath
 
#input
a =float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))

#Procesing
discriminante=b**2-4*a*c
if a==0:
    print("No es una ecuación cuadratica")
if discriminante==0:
    x1=-b/(2*a)
    Rta=(x1,x1)
elif discriminante >0:
    x1=(-b+sqrt(discriminante))/(2*a)
    x2=(-b-sqrt(discriminante))/(2*a)
    Rta=(x1,x2)
else:
    x1=(-b+cmath.sqrt(discriminante))/(2*a)  
    x2=(-b+cmath.sqrt(discriminante))/(2*a)      
    Rta=(x1,x2)
           
print("-------------------------------------")
print("Las raices son:"+str(Rta))
print("--------------------------------")