arr = [10, 20, 30, 40]
#matrix[row]

arr2= [ [10 ,20] ,
        [12,21],
        [11,78] ]

#matrix[row][col]
arr3= [
        [[12],[13]],
        [[20],[30]],
        [[54],[68]]
        ]


total = 0
for x2 in arr2:
    for z1 in x2:
        total += z1
        print(total)
    print(f"\t{x2}")