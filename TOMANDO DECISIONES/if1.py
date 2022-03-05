
#Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado sera solido, 
#si es menor que 100 sera liquido y si es mayor que 100 será gas. Pedir al usuario valor de la temperatura.

num1 = int(input("Ingrese la temperatura del agua: "))

if num1 <= 0 :
    print("Estado solido")

elif num1 <= 100 :
    print("Estado liquido")

else:
    print("Estado gaseoso")

print("....")
#[output]
#Ingrese la temperatura del agua: -34
#Estado solido
#....
