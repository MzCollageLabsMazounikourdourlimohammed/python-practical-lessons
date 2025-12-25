import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة

# تحويل الصورة من BGR إلى HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#h الون الاساسي 
#s التشبع 
#v السطوع 

# تحديد نطاق اللون الأحمر في HSV
# lower_red1 = np.array([0, 120, 70])
# upper_red1 = np.array([10, 255, 255])
lower_Blue1 = np.array([0, 150, 70])
upper_Blue1 = np.array([255, 255, 255])

# عمل قناع للون الأحمر

mask = cv2.inRange(hsv, lower_Blue1, upper_Blue1)
# تغيير اللون: إنشاء نسخة صفرية

h, s, v = cv2.split(hsv)
# 0red 30yellow 60green 120Blue 150Purple
# تحويل الأحمر إلى أصفر/أخضر
h[mask > 0] = 150  # تقريبًا لون أصفر مخضر
s[mask > 0] = 0  # تشبع كامل
v[mask > 0] = 0  # سطوع كامل

# دمج القنوات مرة أخرى
hsv_new = cv2.merge([h, s, v])

# تحويل HSV إلى BGR للعرض
img_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", img)
cv2.imshow("New Image", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()