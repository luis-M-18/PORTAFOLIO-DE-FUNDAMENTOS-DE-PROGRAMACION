
#Como hemos comentado, las tuplas son tipos inmutables, lo que significa que una vez asignado su valor, no puede ser modificado.
# Si se intenta, tendremos un TypeError.
tupla = (1, 2, 3)
tupla[0] = 5 
#[output]
# Error! TypeError

#Al igual que las listas, las tuplas también pueden ser anidadas.

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       
print(tupla[2][0]) 
#[output]
#(1, 2, ('a', 'b'), 3)
#a

#También es posible convertir una lista en tupla haciendo uso de al función tuple().
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) 
print(tupla)   
#[output]
##<class 'tuple'>
#(1, 2, 3)