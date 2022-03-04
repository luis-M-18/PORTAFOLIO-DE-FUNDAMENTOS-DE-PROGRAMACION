#Se puede iterar una tupla de la misma forma que se hacía con las listas.

tupla = [1, 2, 3]
for t in tupla:
    print(t)
#[output]
#1, 2, 3


#Y se puede también asignar el valor de una tupla con n elementos a n variables.

l = (1, 2, 3)
x, y, z = l
print(x, y, z)
#[output]
#1 2 3


#Aunque tal vez no tenga mucho sentido a nivel práctico, es posible crear una tupla de un solo elemento. Para ello debes usar , antes del paréntesis, porque de lo contrario (2) sería interpretado como int.

tupla = (2,)
print(type(tupla))
#[ouput]
 #<class 'tuple'>