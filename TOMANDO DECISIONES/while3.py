#Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente SI (en mayúsculas y sin tilde)
def main():
    print("DIGA SI PARA TERMINAR")
    respuesta = input("¿Desea terminar el programa?: ")

    while respuesta != "SI":
        respuesta = input("¿Desea terminar el programa?: ")

    print("¡Hasta la vista!")


if __name__ == "__main__":
    main()

#[output]
#DIGA SI PARA TERMINAR
#¿Desea terminar el programa?: no
#¿Desea terminar el programa?: xd
#¿Desea terminar el programa?: SI
#¡Hasta la vista!