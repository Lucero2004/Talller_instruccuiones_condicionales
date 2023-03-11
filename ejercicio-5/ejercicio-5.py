#Ejercicio-5
#programa para clacular el gasto de agua de una vivienda

CG=int(input("Ingrese la cantidad de agua gastada en (m^3):"))
CF= 10000
if CG<49:
    print("E concumo de agua es de:  "+str(CF))
if 50<CG<=200:
    print("El consumo de agua es de: "+str(CF+(CG-50)*2000))
if  CG>200:
    print("El consumo de agua es de: "+str(CF+(CG-50)*3000))    
