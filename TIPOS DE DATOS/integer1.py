
#En este ejemplo hemos asignado un número decimal a una variable, pero también es posible asignar
#valores en "binario", "hexadecimal" y "octal"

x = 0b100 
y = 0x18   
z = 0o720
print(x, type(x))     #[output] 4 <class 'int'>
print(y, type(y))     #[output] 24 <class 'int'>
print(z, type(z))     #[output] 464 <class 'int'>


#El prefijo "0b" indica que lo que viene a continuación sera interpretado como un número binario
#El prefijo "0x" indica que lo que viene a continuación sera interpretado como un número hexadecimal
#El prefijo "0o" indica que lo que viene a continuación sera interpretado como un número octal