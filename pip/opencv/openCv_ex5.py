
import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة

# مستطيل أخضر
cv2.rectangle(img, (50,50), (200,200), (0,255,0), 3)
# cv2.rectangle(image, pt1, pt2, color, thickness)
# image → الصورة التي تريد الرسم عليها.
# pt1 → النقطة العليا اليسرى للمستطيل (x1, y1).
# pt2 → النقطة السفلى اليمنى للمستطيل (x2, y2).
# color → لون المستطيل (B, G, R) (OpenCV يستخدم BGR).
# thickness → سمك الخط.
# إذا كانت - → المستطيل مملوء بالكامل.

# دائرة زرقاء
cv2.circle(img, (300,300), 50, (0,0,255), 1) 
# cv2.circle(image, center, radius, color, thickness) 
# image → الصورة التي تريد الرسم عليها.
# center → مركز الدائرة (x, y).
# radius → نصف قطر الدائرة بالبيكسل.
# color → لون الدائرة (B, G, R) لأن OpenCV يستخدم صيغة BGR.
# thickness → سمك الخط:
# إذا كانت -1 → الدائرة مملوءة بالكامل.
# أي رقم موجب → سمك حدود الدائرة.

# خط أحمر
cv2.line(img, (0,0), (400,400), (0,0,255), 5)
# cv2.line(image, pt1, pt2, color, thickness)


cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
