num = [10, 20, 30]
name = ["Labs", "Collage", "MZ"]
mix = [1, "text", 3.5, True]
print(f"{name}\n{num}\t{mix}")

# #استعمالها مع عناصر اخرى 
# students = [
#     {"name": "Ali", "age": 20},
#     {"name": "Sara", "age": 22}
# ]
# print(students)
#==============
# Letters = ["A", "B", "C"]

# # print(Letters[0])   # A
# # print(Letters[2])   # C
# # print(Letters[-2])  # C (من النهاية)

# # Letters[2]="10"
# # # print(Letters)

# # # #غضافة عنصر في نهاية 
# # Letters.append("mazouni")
# # print(Letters)

# # # إضافة عنصر في موقع محدد 
# # Letters.insert(1, "new items")
# # print(Letters)


# # دمج القوائم 
# Letters.extend(mix)
# print(Letters)

# # #حذف عناصر
# # Letters.remove("A")
# # x = Letters.pop(1)  
# # # del Letters[0]

# print(Letters)
# print(len(Letters))


# #بحث داخل الدالة
# print(3.5 in Letters)   


# #حلقات مع قوائم والمصفوفات

# items = [10, 20, 30]
# for i in items:
#     print(i)

# #الترتيب العناصر 

# Numbers = [3, 1, 2,5 ,47]
# Numbers.sort()
# print(Numbers)   

# Numbers.reverse()
# print(Numbers)   


# #تتبع والطباعة احتياجات القائمة 
# c = [1, 2, 3, 4, 5]

# print(c[1:5])   # [2, 3, 4] 
# print(c[0:2])   # [1, 2 ,3]

# print(c[:3])    # [1, 2, 3]
# print(c[:2])    # [1 ,2]
# print(c[2:])    # [3, 4, 5]
# print(c[0:])    # [1 ,2 ,3 ,4 ,5]
# print(c[::4])   # [3, 4, 5]

# # # ===========
# print(sum(c))     # 15
# print(max(c))     # 5
# print(min(c))     #1
