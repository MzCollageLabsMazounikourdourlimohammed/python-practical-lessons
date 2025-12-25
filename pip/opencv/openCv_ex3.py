import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة



hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0,0,70])

upper_red1 = np.array([10,255,255])

#اذا كان ضمن النطاق يبقى اذا كان خارج النطاق يتحول لاى الاسود
mask = cv2.inRange(hsv, lower_red1, upper_red1)
result = cv2.bitwise_and(img, img, mask=mask)
#اي  ماسك فيه 255 يبقى اخر يتحول 

cv2.imshow("Red Color", result)
cv2.waitKey(0)
cv2.destroyAllWindows()