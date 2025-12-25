import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)       
  # لرسم خط يربط بين النقاط 
plt.xlabel("x axis")    
 #لتسمية الرسم والمحاور 
plt.ylabel("y axis")
plt.show()             # لعرض الرسم

# #========
# x1 = [5, 7, 8, 7, 2, 17, 2, 9]
# y1 = [99, 86, 87, 88, 100, 86, 103, 87]

# plt.scatter(x1, y1, color='red', marker='+')
#   # رسم نقاط
# plt.title("Scatter Plot ")
# plt.show()


# #===========
# categories = ['A', 'B', 'C', 'D']
# values = [5, 7,5, 10]

# plt.bar(categories, values, color='green') 
#  # رسم الأعمدة
# plt.title("Bar Chart ")
# plt.show()

# #===========

# sizes = [15, 30, 45, 10]
# labels = ['Orange', 'Banana', 'Apple', 'rasspbery']
# colors = ['orange', 'yellow', 'green', 'red']

# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f')
# plt.title("Chart Example")
# plt.show()


# #======

# x3 = [1, 2, 3, 4, 5]
# y3 = [2, 3, 5, 7, 11]

# plt.plot(x3, y3, color='purple', linewidth=2, linestyle='--', marker='o', markersize=8)
# plt.title("Customized Line Plot")
# plt.grid(True)  # إظهار شبكة الرسم
# plt.show()


# #========
# x4 = [1, 2, 3, 4, 5]
# y4 = [1, 4, 9, 16, 25]
# y5 = [2, 3, 5, 7, 11]

# plt.plot(x4, y4, label='Squares')  # خط 1
# plt.plot(x4, y5, label='Primes')   # خط 2
# plt.legend()                      # إظهار وسوم الخطوط
# plt.title("Multiple Lines Example")
# plt.show()


# ##==============


# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 3, 5, 7, 11]

# # إنشاء 1 صف و 2 عمود (side by side)
# fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10,4))

# ax1.plot(x, y1)
# ax1.set_title("Squares")

# ax2.plot(x, y2)
# ax2.set_title("Primes")

# ax3.plot(y1, y2)
# ax3.set_title("Mixes")
# plt.show()

# #===========



