
#Calcular de la suma y la media aritmetica de N números reales. solicitar el valor N al usuario y cada uno 
#de los N números rales.

n = 2
suma = 0
for i in range(n):
    num = int(input("Ingrese número: "))
    suma  += num 
    media = suma/n
print("La suma es: ", suma)
print("La media es: ", media)

#[ouput]
#Ingrese número: 3
#Ingrese número: 4
#La suma es:  7
#La media es:  3.5