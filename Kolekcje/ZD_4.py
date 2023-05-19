
table = [[0]*10 for n in range(10)]

for n in range(1,11):
    for m in range(1,11):
        table[n-1][m-1]=n*m
        print (table)