# ejercicio-9
print("--------------------------------------------------------------------")
print("Programa para determinar si un triangulo es obtuso,recto o agudo ")
print("-------------------------------------------------------")

a=float(input("Ingrese el valor del lado 1: "))
b=float(input("Ingrese el valor del lado 2: "))
c=float(input("Ingrese el valor del lado 3: "))
print("---------------------------------")

if (c**2)==(a**2)+(b**2):
   print("Es un triangulo Recto")
if (c**2)>(a**2)+(b**2):
   print("Es un triangulo obtuso")
if (c**2)<(a**2)+(b**2):
   print("El triangulo es agudo ")
