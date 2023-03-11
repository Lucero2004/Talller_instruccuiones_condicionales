#ejercicio-3
#programa para determinar el valor de un producto de venta

PC=int(input("Ingrese el costo del articulo en venta: "))


if PC<3000:
    print("El producto cuesta: "+str(PC+0.15))
if 3000<PC<6000:
    print("El producto cuesta:" +str(PC+500))
if PC>6000:
    print("El producto cuesta: "+str(PC+0.25))