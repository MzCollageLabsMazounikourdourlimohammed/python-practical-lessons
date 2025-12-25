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

# #matrix[var1][var2][varA]

print(f"\n{arr}\n{arr2}\n{arr3}")
# # تنطبق عليها خصائص القوائم كاملة

# print(arr[1])
# print(arr2[0][0])
# print(arr3[2][0][0])

# #اضافة للمصفوفة 
# arr.append([10, 11, 12])
# arr2.append([10, 11, 12])
# arr3.append([10, 11, 12])
# print(f"\n{arr}\n{arr2}\n{arr3}")

#اضافة 0 لجميع عناصر المصفوفة
# for i in arr3:
#     i.append(0)
#     print(i)


# # # تكرار كل عنصر في الصف 
# for x1 in arr2:
#     for z in x1:
#         print(f"\t{z}")

#مثال عملية في مصفوفة 
total = 0
for x2 in arr2:
    for z1 in x2:
        total += z1
        print(total)
    print(f"\t{x2}")