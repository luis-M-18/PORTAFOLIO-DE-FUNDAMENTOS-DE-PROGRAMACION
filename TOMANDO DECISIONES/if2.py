
#Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible para 400. Escribe un programa 
#que lea un año y duvuelva si es bisiesto o no.

num1 = int(input("Ingrese el año: "))

if (num1 % 4 != 0) :
    print("No es bisiesto")

elif (num1 % 4 == 0 and num1 % 100 != 0 ) :
    print("Es bisiesto")

elif (num1 % 4 == 0 and num1 % 100 == 0 and num1 % 400 != 0) :
    print("No bisiesto")

elif (num1 % 4 == 0 and num1 % 100 == 0 and num1 % 400 == 0) :
    print("Es bisiesto")
print("...")

#[output]
#Ingrese el año: 2003
#No es bisiesto
#...