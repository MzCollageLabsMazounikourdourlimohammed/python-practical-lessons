import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة


    # # عرض الصورة في نافذة
cv2.imshow("Image", img)
    
    # # الانتظار حتى تضغط أي زر
cv2.waitKey(0)

