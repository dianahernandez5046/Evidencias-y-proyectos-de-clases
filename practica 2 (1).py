print ("CONTADOR QUE VA EN AUMENTO")
contador = 0
print (contador)
contador = contador + 1
print (contador)
contador = contador + 1
print (contador)
contador = contador + 1
print (contador)

print ("---------------espacio de separacion----------------")

print ("DATOS PERSONALES")
nombre = ("wawa")
edad = ("2234567 años")
ciudad = ("narnia")
print (nombre, edad, ciudad)

print ("---------------espacio de separacion----------------")

print("CONVERSION DE PULGADAS A CENTIMETROS")
PULGADAS_A_CM = 2.54
pulgadas = 20
print ("inches:"), print (pulgadas)
pulgadas * 2.54
print ("cm:"), print (pulgadas * 2.4)

print ("---------------espacio de separacion----------------")

print ("AREA Y PERIMETRO DE UN RECTANGULO")
base = 300
altura = 600
print ("area de un rectangulo de 300 x 600")
print (base * altura)
print ("y el perimetro de este mismo es:")
print (base + altura *2)

print ("---------------espacio de separacion----------------")

print ("CALCULO DE IVA 1")
precio = 700
IVA = 0.16
print ("este es el valor")
print (precio)
print ("este es el iva")
print (precio * IVA)
print ("este es el precio total")
print (precio + precio * IVA)

print ("---------------espacio de separacion----------------")

print ("CALCULO DE IVA 2")
precio = 350
print ("este es el valor")
print (precio)
print ("este es el iva")
print (precio * IVA)
print ("este es el precio total")
print (precio + precio * IVA)

print ("--------------espacio--------------")

print ("INTERCAMBIO DE VALORES")
variable1 = 20
variable2 = 40
auxiliar = 10
print ("variables:"), print (variable1, variable2)
print ("variables intercambiadas")
print (variable2 - auxiliar*2)
print (variable1 + auxiliar*2)

print ("--------------espacio--------------")

print ("VARIABLES Y SUS TIPOS")
raton = 10,type(int)
jirafa = 4.5,type(float)
abeja = True,type(bool)
perro = ("gato"),type(str)
print(str, bool,float, int)
print(raton, int)
print (jirafa, float)
print (abeja, bool)
print(perro, str)