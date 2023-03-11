#Ejercicio-1
# Programa para determinar la posicion de un punto en el plano cartesiano

#input
X=(int(input("Digite el valor del punto en el eje x: ")))
Y=(int(input("Digite el valor del punto en el eje Y: ")))


if (X>0)and (Y>0):
    print("El punto se encuentra ubicado en el I cuadrante ")
if (X<0) and (Y>0):
    print("El punto se encuentra ubicado en el cuadrante II")
if (X<0) and (Y<0):
    print("El punto está ubicado en el cuadrante III")
if (X>0) and (Y<0):
    print("El punto se encuentra ubicado en el cuadrante IV")
if X==0:
    if Y==0:
     print("El punto está en el origen")
    else:
     print("El punto está en el eje y")




