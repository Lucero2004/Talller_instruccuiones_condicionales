#ejercicio-4
#prograama para determinar el indice de masa corporal y el estado de una persona

p=float(input("Ingrese el valor de su peso en (Kg): "))
a=float(input("Ingrese el valor de su altura en(m): "))
print("------------------------------------------------")
IMC=p / a**2
print("Su IMC es de:"+ str(IMC))
print("--------------------------------------------")
if IMC<16:
    print("su criterio es de ingreso al hospital")
if 16<IMC<17:
    print("Su estado es: infrapeso")
if 17<IMC<18:
    print("Su estado es: Bajo de peso")
if 18<IMC<25:
    print("Su estado es: Saludable")
if 25<IMC<30:
    print("Su estado es: obesidad grado 1")
if 30<IMC<35:
    print("Su estado es: obesidad grado 2")
if 35<IMC<40:
    print("Su estado es: obesidad grado 3")
if IMC>40:
    print("Su estado es: obesidad grado 4")
print("------------------------------------------")    