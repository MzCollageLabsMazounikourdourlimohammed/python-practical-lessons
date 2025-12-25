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
