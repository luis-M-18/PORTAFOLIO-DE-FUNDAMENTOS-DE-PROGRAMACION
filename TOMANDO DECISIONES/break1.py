contador = 0
for i in range(5):
    for j in range(5):
        contador += 1
        print("i:",i ,"j:",j)
        if contador > 10:
            break

print("contador:",contador)

#[output]
#i: 0 j: 0
#i: 0 j: 1
#i: 0 j: 2
#i: 0 j: 3
#i: 0 j: 4
#i: 1 j: 0
#i: 1 j: 1
#i: 1 j: 2
#i: 1 j: 3
#i: 1 j: 4
#i: 2 j: 0
#i: 3 j: 0
#i: 4 j: 0
#contador: 13