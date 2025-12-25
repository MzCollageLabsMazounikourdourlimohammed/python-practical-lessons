import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 

x1 = [5, 7, 8, 7, 2, 17, 2, 9]
y1 = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x1, y1, color='red', marker='+')
  # رسم نقاط
plt.title("Scatter Plot ")
plt.show()