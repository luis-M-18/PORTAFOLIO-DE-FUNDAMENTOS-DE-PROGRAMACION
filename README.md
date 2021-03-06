# PORTAFOLIO-DE-FUNDAMENTOS-DE-PROGRAMACIÓN
# ¿Qué es Python?
Es un lenguaje de programación versátil multiplataforma y multiparadigma que se destaca por su código legible y limpio. Una de las razones de su éxito es que cuenta con una licencia de código abierto que permite su utilización en cualquier escenario. Esto hace que sea uno de los lenguajes de iniciación de muchos programadores siendo impartido en escuelas y universidades de todo el mundo. Sumado a esto cuenta con grandes compañías que hacen de este un uso intensivo. 
# ¿Qué es una variable?
Una variable es un nombre para representar un valor de un dato, por ejemplo, si tenemos un programa que suma dos número, necesitamos un nombre para identificar el valor1 y el valor2 (mira, esto mismo nos serviría como variables, valor1 y valor2 podrían ser el nombre de nuestras variables)
## Nombrando una variable
Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o números al principio.
```python
variable = 60
#donde la palabra "variable" es donde se guarda la información y el signo "=" nos indica cual es este valor, que en este caso es "60"
```
## Asignando valores a una variable
```python
variable = 10
vari = "Hola mundo"
#aqui el valor que esta despues del "=" es el valor asignado a nuestra variable
```
Tambien podemos asignar multiples variables en una sola linea
```python
x, y, z = 10, 20, 30
#donde segun el orden corresponde los valores de esta forma "x = 10", "y = 20" y "z = 30"
```
## Operadores básicos
Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.
```python
suma = +
resta = -
multiplicación = *
división = /
división = //
módulo = %
potenciación = **
```
### Suma
Para realizar una suma en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos un valor a cada una
num1 = 10
num2 = 3
#despues creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador suma
result = (num1 + num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado
[output] 13
```
### Resta
Para realizar una resta en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos valores
num1 = 20
num2 = 15
#después creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador resta
result = (num1 - num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado 
[output] 5
```
### Multiplicación
Para realizar una multiplicación en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos valores
num1 = 15
num2 = 3
#después creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador multiplicación
result = (num1 * num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado 
[output] 45
```
### División
Para realizar una división en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos valores
num1 = 48
num2 = 6
#después creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador división
result = (num1 / num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado 
[output] 8
```
### Módulo
Para realizar un módulo en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos valores
num1 = 15
num2 = 2
#después creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador módulo
result = (num1 % num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado 
[output] 1
```
### Potenciación
Para realizar una potenciación en Python seguimos los siguientes pasos:
```python
#primero creamos dos variables y les asignamos valores
num1 = 3
num2 = 4
#después creamos otra variable que sera donde se almacenara nuestro resultado
result = 0
#ahora presentamos las dos variables acompañados del operador potenciación
result = (num1 ** num2)
#por último presentamos un print para imprimir nuestro resultado
print(result)
#resultado 
[output] 81
```
# Tipos de datos en Python
En python un tipo de dato establece qué valores puede tomar una variable y qué operaciones se pueden realizar sobre la misma. Dentro de los mas reconocidos tenemos:
## Integer
Los números enteros son aquellos que no contienen decimales, pueden ser positivos o negativos además del cero. En Python, además de otros lenguajes de programación, se les conoce como de tipo int (interger, entero) o tipo long (de largo). La diferencia entre ambos es que el long permite almacenar números más grandes, por lo que también ocupa más espacio en un programa, así que es recomendable usarlo sólo en caso de ser necesario.
Ejemplo
```python
#variables de valor entero
x = 100
y = 3546
z = -345
```
## Float
El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales. Por lo tanto si declaramos una variable y le asignamos un valor decimal, por defecto la variable será de tipo float.
Ejemplo
```python
#variables de valor decimal
x = 12.5
y = 2.567
z = -3.45
```
También se puede utilizar notación científica, y añadir una e (de exponente) para indicar un exponente en base 10. Por ejemplo:
```python
x = 0.1e-3
```
sería equivalente a 0.1 x 10-3 = 0.1 x 0.001 = 0.0001
## String
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.
Ejemplo:
```python 
print("Hola Mundo")
```
## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro. Pero antes de nada, veamos los diferentes tipos de cast o conversión de tipos que se pueden hacer. Existen dos:

Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.

Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().

#### Conversión implícita
Esta conversión de tipos es realizada automáticamente por Python, prácticamente sin que nos demos cuenta. Aún así, es importante saber lo que pasa por debajo para evitar problemas futuros. 

El ejemplo más sencillo donde podemos ver este comportamiento es el siguiente:
```python 
a = 1   # <class 'int'>
b = 2.3 # <class 'float'>
a = a + b
print(a)       # 3.3
print(type(a)) # <class 'float'>
```
"a" es un int
"b" es un float. 
Pero si sumamos a y b y almacenamos el resultado en a, podemos ver como internamente Python ha convertido el int en float para poder realizar la operación, y la variable resultante es float

Sin embargo hay otros casos donde Python no es tan listo y no es capaz de realizar la conversión. Si intentamos sumar un int a un string, tendremos un error TypeError.
```python 
a = 1
b = "2.3"
c = a + b
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Si te das cuenta, es lógico que esto sea así, ya que en este caso b era "2.3", pero ¿y si fuera "Hola"? ¿Cómo se podría sumar eso? No tiene sentido.

#### Conversión explicita
Por otro lado, podemos hacer conversiones entre tipos o cast de manera explícita haciendo uso de diferentes funciones que nos proporciona Python. Las más usadas son las siguientes:

float(), str(), int()

##### Convertir float a int 
Para convertir de float a int debemos usar float(). Pero mucho cuidado, ya que el tipo entero no puede almacena decimales, por lo que perderemos lo que haya después de la coma.
```python
a = 3.5
a = int(a)
print(a)
# Salida: 3
```
##### Convertir float a string 
Podemos convertir un float a string con str(). Podemos ver en el siguiente código como cambia el tipo de a después de hacer el cast.
```python
a = 3.5
print(type(a)) # <class 'float'>
a = str(a)
print(type(a)) # <class 'str'>
```
##### Convertir string a float
Podemos convertir un string a float usando float(). Es importante notar que se usa el . como separador.
```python
a = "35.5"
print(float(a))
# Salida: 35.5
```
El siguiente código daría un error, dado que , no se reconoce por defecto como separador decimal.
```python
a = "35,5"
print(float(a))
# Salida: ValueError: could not convert string to float: '35,5'
```
Y por último, resulta obvio pensar que el siguiente código dará un error también.
```python
a = "Python"
print(float(a))
# Salida: ValueError: could not convert string to float: 'Python'
```
##### Convertir string a int 
Al igual que la conversión a float del caso anterior, podemos convertir de string a int usando int().
```python
a = "3"
print(type(a)) # <class 'str'>
a = int(a)
print(type(a)) # <class 'int'>
```
Cuidado ya que no es posible convertir a int cualquier valor.
```python
a = "Python"
a = int(a)
# ValueError: invalid literal for int() with base 10: 'Python'
```
##### Convertir int a string 
La conversión de int a string se puede realizar con str().
A diferencia de otras conversiones, esta puede hacerse siempre, ya que cualquier valor entero que se nos ocurra poner en a, podrá ser convertido a string.
```python
a = 10
print(type(a)) # <class 'int'>
a = str(a)
print(type(a)) # <class 'str'>
```
## List
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.

### Crear listas Python
Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.
```python
lista = [1, 2, 3, 4]
```
También se puede crear usando list y pasando un objeto iterable.
```python
lista = list("1234")
```
Una lista sea crea con [] separando sus elementos con comas ,. Una gran ventaja es que pueden almacenar tipos de datos distintos.
```python
lista = [1, "Hola", 3.67, [1, 2, 3]]
```
Algunas propiedades de las listas:

* Son ordenadas, mantienen el orden en el que han sido definidas.
* Pueden ser formadas por tipos arbitrarios.
* Pueden ser indexadas con [i].
* Se pueden anidar, es decir, meter una dentro de la otra.
* Son mutables, ya que sus elementos pueden ser modificados.
* Son dinámicas, ya que se pueden añadir o eliminar elementos.
## Tuple
Las tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables.

### Crear tupla Python
Las tuplas en Python o tuples son muy similares a las listas, pero con dos diferencias. Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
```python
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
```
También pueden declararse sin (), separando por , todos sus elementos.
```python
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)
```
### Operaciones con tuplas
Como hemos comentado, las tuplas son tipos inmutables, lo que significa que una vez asignado su valor, no puede ser modificado. Si se intenta, tendremos un TypeError.
```python
tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError
```
Al igual que las listas, las tuplas también pueden ser anidadas.
```python
tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a
```
Y también es posible convertir una lista en tupla haciendo uso de al función tuple().
```python
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)
```
## Dictionary
Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.

### Crear diccionario Python
Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.
```python
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
```
Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.
```python
d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])
print(d2)
#{'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}
```
También es posible usar el constructor dict() para crear un diccionario.
```python
d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882)
print(d3)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
```
Algunas propiedades de los diccionario en Python son las siguientes:

* Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
* Son indexados, los elementos del diccionario son accesibles a través del key.
* Y son anidados, un diccionario puede contener a otro diccionario en su campo value.
# Tomando decisiones

## Sentencia if
En la sentencia if sólo tienes un bloque de sentencias y este bloque se ejecuta sólo cuando la condición es True, se ignora cuando la condición es False.
A continuación se muestra la sintaxis de la declaración if en Python:
```python
if condition:
    statement(s)
```
El cuerpo de la declaración if en Python no está rodeado por llaves, sino que se usa la indentación. El final del cuerpo se indica con la primera línea no deseada.
Considere el siguiente ejemplo en el que se utiliza la sentencia if:
```python
a = 24
if a % 2 == 0:
    print(a, "es un número par")
[output] 24 es un número par
```
En este código, a la variable "a" se le asigna un valor primero y luego se evalúa la condición en la sentencia if. Comprueba si a es un número par o no tomando el módulo de "a" con 2 y si el resultado de % (mod) es 0 entonces el control enter en el cuerpo de if y la sentencia print se ejecuta.
### Sentencia if....else
La siguiente es la sintaxis de una declaración de if...else:
```python
if condition:
    block of statements
else:
    block of statements
```
En if...else, si el if la condición es True, se ejecuta el bloque correspondiente de declaraciones, de lo contrario se ejecutará el bloque de declaraciones de la parte else.
Ejemplo de declaración if...else
```python
a = 44
if a%2==0:
    print(a, "es un número par")
else:
    print(a, "es un número impar")
[output] 44 es un número par
```
Aquí si "a" es par, se imprimirá "a es un número par", de lo contrario se imprimirá "a es un número impar".
### Sentencia if...elif...else
La siguiente es la sintaxis de la frase if...elif...else:
```python
if condition:
    block of statements
elif condition:
    block of statements
else:
    block of statements
```
elif significa "else if" y puede ser usado varias veces en esta construcción if..elif..else.

Cuando la condición de if se convierte en False, la condición de elif será comprobada y así sucesivamente. Cuando todas las condiciones de if y elif son False, la parte de else será ejecutada.

Ejemplo sentencia if...elif...else
```python
a = -34
if a > 0:
    print("Número es Positivo")
elif a < 0:
    print("Número es Negativo")
else:
    print("Número es Cero")
[output] Número es Negativo
```
## Ciclo For
Los ciclos for permiten ejecutar una o varias instrucciones de forma iterativa, una vez por cada elemento en la colección.

Las colecciones pueden ser de varios tipos, el for puede recibir una colección predefinida o directamente de la salida de una función.

El siguiente fragmento de código es utilizado para iterar a través de un rango del 1 al 10.
```python
for contador in range(1,10):
     print contador,
[output] 1 2 3 4 5 6 7 8 9
```
Para iterar sobre una lista.
```
numeros = [0, 1, 2, 3, 4, 5]
 for numero in numeros:
     print numero,
[output] 0 1 2 3 4 5
```
## Ciclo While
El ciclo while permite ejecutar un bloque de instrucciones mientras se cumpla la condición dada. Primero comprueba que en efecto se cumple la condición dada y entonces, ejecuta el segmento de código correspondiente hasta que la condición no se cumpla.

Para imprimir una serie de números del 0 al 10.
```python
numero = 0
while numero <= 10:
     print numero
     numero += 1
[output]
0
1
2
3
4
5
6
7
8
9
10
```
## Break
En Python, la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

Veamos un ejemplo en el que se utiliza la instrucción break en un bucle for:
```python
number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')
[output]
Number is 0
Number is 1
Number is 2
Number is 3
Number is 4
Out of loop
```
En este pequeño programa, la variable number se inicia en 0. Luego, una instrucción for construye el bucle siempre que la variable number sea inferior a 10.

En el bucle for, existe una instrucción if que presenta la condición de que si la variable number es equivalente al entero 5, entonces el bucle se romperá.

En el bucle también existe una instrucción print() que se ejecutará con cada iteración del bucle for hasta que se rompa el bucle, ya que está después de la instrucción break.

Para saber cuándo estamos fuera del bucle, hemos incluido una instrucción print() final fuera del bucle for.
## Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

La instrucción continue se encuentra dentro del bloque de código abajo de la instrucción del bucle, generalmente después de una instrucción if condicional.

Usando el mismo programa de bucle for que en la sección anterior Instrucción break, emplearemos la instrucción continue en vez de la instrucción break:
```python
number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')
[output]
Number is 0
Number is 1
Number is 2
Number is 3
Number is 4
Number is 6
Number is 7
Number is 8
Number is 9
Out of loop
```
La diferencia al usar la instrucción continue en vez de una instrucción break radica en que nuestro código continuará a pesar de la interrupción cuando la variable number se evalúe como equivalente a 5.

Aquí, Number is 5 nunca aparece en el resultado, pero el bucle continúa después de ese punto para imprimir líneas para los números 6 a 10 antes de cerrarse.

Puede usar la instrucción continue para evitar código condicional profundamente anidado o para optimizar un bucle eliminando los casos frecuentes que desee rechazar.

La instrucción continue hace que un programa omita determinados factores que surgen dentro de un bucle, pero luego continuará con resto de este.
