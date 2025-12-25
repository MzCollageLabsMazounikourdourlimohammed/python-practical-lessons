import numpy as np
x = np.array([1, 2, 3, 4])
x1 = np.array([[1, 2],  [3, 4]])
z = np.zeros((3,3))
z3 = np.random.rand(2,3)
z2 = np.arange(0, 10, 2) 


z4=np.array([[[1,2,3],[2,3,4],[11,21,32],[32,33,34]], [[1,2,3],[2,3,4],[11,21,32],[32,33,34]],[[1,2,3],[2,3,4],[11,21,32],[32,33,34]] ])
print(z4.size)
print("Shape of x1:", x1.shape)  # شكل المصفوفة
print("Dimensions of z3:", z3.ndim)  # عدد الأبعاد
print("Size of z:", z.size)  # عدد العناصر الكلي
print("Data type:", z2.dtype)  # نوع البيانات
