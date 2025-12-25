import matplotlib.pyplot as plt
#مكتبة لتعامل مع الرسوم البيانية والمخططات 
#يمكن رسم الخطوط نقاط اعمدة دوائر وهناك الكثير 

x4 = [1, 2, 3, 4, 5]
y4 = [1, 4, 9, 16, 25]
y5 = [2, 3, 5, 7, 11]

plt.plot(x4, y4, label='Squares')  # خط 1
plt.plot(x4, y5, label='Primes')   # خط 2
plt.legend()                      # إظهار وسوم الخطوط
plt.title("Multiple Lines Example")
plt.show()
