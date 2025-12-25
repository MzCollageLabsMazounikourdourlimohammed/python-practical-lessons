import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 3, 5, 7, 11]

# إنشاء 1 صف و 2 عمود (side by side)
fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10,4))

ax1.plot(x, y1)
ax1.set_title("Squares")

ax2.plot(x, y2)
ax2.set_title("Primes")

ax3.plot(y1, y2)
ax3.set_title("Mixes")
plt.show()




