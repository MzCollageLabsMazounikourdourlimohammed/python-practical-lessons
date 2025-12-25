import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 

sizes = [15, 30, 45, 10]
labels = ['Orange', 'Banana', 'Apple', 'rasspbery']
colors = ['orange', 'yellow', 'green', 'red']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f')
plt.title("Chart Example")
plt.show()
