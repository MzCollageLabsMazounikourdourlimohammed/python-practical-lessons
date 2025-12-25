

import numpy as np

# العمليات على المصفوفات ثنائية الأبعاد
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("Matrix multiplication:\n", A @ B)  # الضرب المصفوفي
# 1*5+2*7 1*6+2*8  3*5+4*7  3*6+4*8  
print("Element-wise multiplication:\n", A * B)  # ضرب عناصر بعناصر
# 1*5 2*6 7*3 4*8 
