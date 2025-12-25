#مكتبة بايثون أساسية للتعامل مع المصفوفات والأعداد بكفاءة عالية.
import numpy as np
#اولوية  للاستدعاء للملفات الموجود مع البرنامج 


# a = np.array([1.2, 2.5, 34.1, 4.3])
# a2 = [1.2, 2.5, 34.1, 4.3]
# #لا تواجه مشكل مع الاعداد الحقيقية

# print(a*10) #عناصر في 10 
# print(a2*2) # عدد مرات التكرار 

#========
# مصفوفة أحادية البعد
# x = np.array([1, 2, 3, 4])
# print("Array x:", x)

# # # مصفوفة ثنائية البعد (2x3)
# x1 = np.array([[1, 2],  [3, 4]])
# print("Array x1:\n", x1)
# x11 = np.array([[1, 2, 3], [3, 4 ,1]])
# print("Array x1:\n", x11)

# # # # # مصفوفة أصفار
# z = np.zeros((3,3))
# #2 تمثل عدد الاسطر 
# #3 تمثل عدد الاعمدة
# print("Zeros:\n", z)


# # # # مصفوفة آحاد
# z1 = np.ones((3,2))

# print("Ones:\n", z1)


# # مصفوفة أعداد متتابعة
# z2 = np.arange(0, 10, 2) 
#  # من 0 إلى 10 بخطوة 2
# print("range:", z2)


# # # مصفوفة أعداد عشوائية
# z3 = np.random.rand(2,3)
#   # أعداد عشوائية بين 0 و1
# print("Random:\n", z3)

# z4=np.array([[[1,2,3],[2,3,4],[11,21,32],[32,33,34]], [[1,2,3],[2,3,4],[11,21,32],[32,33,34]],[[1,2,3],[2,3,4],[11,21,32],[32,33,34]] ])
# print(z4.size)
# print("Shape of x1:", x1.shape)  # شكل المصفوفة
# print("Dimensions of z3:", z3.ndim)  # عدد الأبعاد
# print("Size of z:", z.size)  # عدد العناصر الكلي
# print("Data type:", z2.dtype)  # نوع البيانات

# #=============
# ##عمليات على المصفوفات 
# e = np.array([1,2,3])
# y = np.array([4,5,6])

# # جمع وطرح وضرب وقسمة
# print("Add:", e + y)
# print("Sub:", e - y)
# print("Mult:", e * y)
# print("Div:", e / y)

# # العمليات على المصفوفات ثنائية الأبعاد
# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])
# print("Matrix multiplication:\n", A @ B)  # الضرب المصفوفي
# # 1*5+2*7 1*6+2*8  3*5+4*7  3*6+4*8  
# print("Element-wise multiplication:\n", A * B)  # ضرب عناصر بعناصر
# # 1*5 2*6 7*3 4*8 

# #========
arr4 = np.arange(6)  # [0 1 2 3 4 5]
print(arr4)
# إعادة الشكل إلى 2x3
resh = arr4.reshape((2,3))
print("Reshaped array:\n", resh)

# # تحويل مصفوفة ثنائية الأبعاد إلى واحدة
flattened = resh.flatten()
# print("Flattened:", flattened)