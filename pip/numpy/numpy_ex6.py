
import numpy as np


arr4 = np.arange(6)  # [0 1 2 3 4 5]
print(arr4)
# إعادة الشكل إلى 2x3
resh = arr4.reshape((2,3))
print("Reshaped array:\n", resh)

# # تحويل مصفوفة ثنائية الأبعاد إلى واحدة
flattened = resh.flatten()
# print("Flattened:", flattened)