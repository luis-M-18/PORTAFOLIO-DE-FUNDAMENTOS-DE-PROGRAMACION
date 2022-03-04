
#Se puede acceder a sus elementos con"[]" o también con la función get()
d1 = {
    "Nombre" : "Luis",
    "Edad" : 18,
    "Documento" : 1003882
}
print(d1["Nombre"])       #Luis
print(d1.get("Nombre"))   #Luis

#Para modificar un elemento basta con usar "[]" con el nombre del "key" y asignar 
#el valor que queremos

d1["Nombre"] = "Enrique"
print(d1)
#[output] {"Nombre" : "Enrique", "Edad" : 18, "Documento" : 1003882}

#Si el "key" al que accedemos no existe se añade automáticamente
d1["Dirección"] = "Solar 11"
print(d1)
#[output] {'Nombre': 'Enrique', 'Edad': 18, 'Documento': 1003882, 'Dirección': 'Solar 11'}
