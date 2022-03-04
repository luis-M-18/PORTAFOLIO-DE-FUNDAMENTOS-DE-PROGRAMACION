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

Conversión implícita.
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

Conversión explicita: 
Por otro lado, podemos hacer conversiones entre tipos o cast de manera explícita haciendo uso de diferentes funciones que nos proporciona Python. Las más usadas son las siguientes:

float(), str(), int()

Convertir float a int: 
Para convertir de float a int debemos usar float(). Pero mucho cuidado, ya que el tipo entero no puede almacena decimales, por lo que perderemos lo que haya después de la coma.
```python
a = 3.5
a = int(a)
print(a)
# Salida: 3
```
Convertir float a string: 
Podemos convertir un float a string con str(). Podemos ver en el siguiente código como cambia el tipo de a después de hacer el cast.
```python
a = 3.5
print(type(a)) # <class 'float'>
a = str(a)
print(type(a)) # <class 'str'>
```
Convertir string a float: 
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
Convertir string a int: 
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
Convertir int a string: 
La conversión de int a string se puede realizar con str().
A diferencia de otras conversiones, esta puede hacerse siempre, ya que cualquier valor entero que se nos ocurra poner en a, podrá ser convertido a string.
```python
a = 10
print(type(a)) # <class 'int'>
a = str(a)
print(type(a)) # <class 'str'>
```
## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
