
#solicitar al usuario una fecha (dd:mm:aa) y comprobar si es correcta.

dia= int(input("Ingrese día: "))
mes= int(input("Ingrese mes: "))
anho= int(input("Ingrese año: "))

if mes <= 0 or mes > 12 or dia <= 0 or dia > 31 or anho < 0:
    print("La fecha es incorrecta")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("La fecha es correcta")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia <= 30:
    print("La fecha es correcta")
elif mes == 2 and dia <= 29:
    if(anho % 4 == 0 and anho % 100 != 0 or anho % 400 == 0):
        print("La fecha es correcta")
    elif dia <= 28: 
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")
else:
    print("La fecha es incorrecta")

#[output]
#Ingrese día: 15
#Ingrese mes: 5
#Ingrese año: 2004
#La fecha es correcta