
#Calcular e imprimir la tabla de multiplicar de un número cualquiera. Imprimir el multiplicando, 
#el multiplicador y el producto.

num = int(input("Ingrese numero: "))

for i in range(1, 12):
    print(f"{i} x {num} = {i * num}")

#[output]
#Ingrese numero: 2
#1 x 2 = 2
#2 x 2 = 4
#3 x 2 = 6
#4 x 2 = 8
#5 x 2 = 10
#6 x 2 = 12
#7 x 2 = 14
#8 x 2 = 16
#9 x 2 = 18
#10 x 2 = 20
#11 x 2 = 22