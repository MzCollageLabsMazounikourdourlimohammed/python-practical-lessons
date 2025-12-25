import cv2
import numpy as np

captur = cv2.VideoCapture(0)

while True:
    ret, frame = captur.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # تحويل الصورة إلى رمادية
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # عكس الألوان لتصبح اليد مضيئة والخلفية داكنة (مثل الأشعة)
    inverted = cv2.bitwise_not(gray)

    # تحويل الصورة إلى BGR لعرضها في OpenCV
    # xray_effect = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
    xray_effect = cv2.convertScaleAbs(inverted, alpha=0.5, beta=0)
    cv2.imshow("X-ray Hand", xray_effect)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captur.release()
cv2.destroyAllWindows()
