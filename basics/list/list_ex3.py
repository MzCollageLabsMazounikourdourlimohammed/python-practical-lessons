Letters = ["A", "B", "C"]
mix = [1, "text", 3.5, True]

print(Letters[0])   # A
print(Letters[2])   # C
print(Letters[-2])  # C (من النهاية)

Letters[2]="10"
print(Letters)

# # # #غضافة عنصر في نهاية 
Letters.append("mazouni")
print(Letters)

# # # إضافة عنصر في موقع محدد 
Letters.insert(1, "new items")
print(Letters)


# # دمج القوائم 
Letters.extend(mix)
print(Letters)

# # #حذف عناصر
# # Letters.remove("A")
# # x = Letters.pop(1)  
# # # del Letters[0]

print(Letters)
print(len(Letters))


# #بحث داخل الدالة
print(3.5 in Letters)   
