import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 

categories = ['A', 'B', 'C', 'D']
values = [5, 7,5, 10]

plt.bar(categories, values, color='green') 
 # رسم الأعمدة
plt.title("Bar Chart ")
plt.show()
