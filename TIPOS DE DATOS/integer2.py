
#Con el siguiente ejemplo vemos como Python asigna diferente número de "bits" a las variables 
#en función del número que quiere representar.

import sys
x = 5 ** 10000
y = 10

#La función getsizeof() devuelve el tamaño de una variable en memoria
print(sys.getsizeof(x), type(x))
print(sys.getsizeof(y), type(y))
#[output]
#3120 <class 'int'>
#28 <class 'int'>