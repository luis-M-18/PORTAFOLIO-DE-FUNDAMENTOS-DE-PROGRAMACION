
#También se pueden indexar las cadenas, como si de una lista se tratase.

x = "abcde"
print(x[0])
print(x[-1])
#[output]
#a
#e

#Del mismo modo, se pueden crear cadenas más pequeñas partiendo de una grande, usando indicando
#el primer elemento y el último que queremos tomar

x = "abcdefgh"
print(x[0:3])
#[output]
#abc

# Si no se indica ningún valor a la derecha de los ":" se llega hasta el final

x = "abcdefghijk"
print(x[3:])
#[output]
#defghijk