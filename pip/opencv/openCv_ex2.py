import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.cvtColor ==> دالة تحول الصورة من الوان الى صيغة اخرى 
#img  صورة الاصلية 
#cv2.COLOR_BGR2GRAY = هنا تحويل من الالوان الى رمادي 
#صورة تتحول من الوان 0-255 لبى ابيض والاسود 

# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Gray Image", gray)
# cv2.imshow("Gray Image", rgb)
cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.imshow(img)
plt.title("RGB Image for Matplotlib")
plt.show()

