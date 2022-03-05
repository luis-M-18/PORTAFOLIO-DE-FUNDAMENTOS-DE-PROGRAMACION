#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
def main():
    print("DIGA sí PARA CONTINUAR")
    respuesta = input("¿Desea continuar el programa?: ")

    while respuesta == "sí":
        respuesta = input("¿Desea continuar el programa?: ")

    print("¡Hasta la vista!")


if __name__ == "__main__":
    main()

#[output]
#DIGA sí PARA CONTINUAR
#¿Desea continuar el programa?: sí
#¿Desea continuar el programa?: sí
#¿Desea continuar el programa?: sí
#¿Desea continuar el programa?: no
#¡Hasta la vista!