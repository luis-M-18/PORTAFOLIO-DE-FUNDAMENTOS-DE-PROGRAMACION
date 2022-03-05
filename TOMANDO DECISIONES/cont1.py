j= 0
for i in range(10):
    j +=2
    print("i: ", i, "j: ", j)
    if j >= 2 and j <= 18:
         continue
    print("el valor de j: ", j)

#[output]
#i:  0 j:  2
#i:  1 j:  4
#i:  2 j:  6
#i:  3 j:  8
#i:  4 j:  10
#i:  5 j:  12
#i:  6 j:  14
#i:  7 j:  16
#i:  8 j:  18
#i:  9 j:  20
#el valor de j:  20