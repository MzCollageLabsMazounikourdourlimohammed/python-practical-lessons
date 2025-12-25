import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 
x3 = [1, 2, 3, 4, 5]
y3 = [2, 3, 5, 7, 11]

plt.plot(x3, y3, color='purple', linewidth=2, linestyle='--', marker='o', markersize=8)
plt.title("Customized Line Plot")
plt.grid(True)  # إظهار شبكة الرسم
plt.show()

