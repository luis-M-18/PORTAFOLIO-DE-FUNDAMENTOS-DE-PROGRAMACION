#En este ejemplo escribiremos un prgrama que permita crear una lista de palabras. Para ello, el programa
#tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
#programa tiene que escribir la lista.

def main():
    numero = int(input("Cuántas palabras tiene la lista: "))

    if numero < 1:
        print("ERROR")
    else:
        lista = []
        for i in range(numero):
            palabra = input(f"Dígame la palabra {i + 1}: ")
            lista += [palabra]
        print(f"La lista creada es: {lista}")

if __name__=="__main__":
    main()
#[output]
#Cuántas palabras tiene la lista: 3
#Dígame la palabra 1: Luis
#Dígame la palabra 2: Maria
#Dígame la palabra 3: pedro
#La lista creada es: ['Luis', 'Maria', 'pedro']