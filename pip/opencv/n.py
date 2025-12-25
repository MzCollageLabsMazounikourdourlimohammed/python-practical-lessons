import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    #يجعل الكاميرا مث لمراة

    roi = frame[100:400, 100:400]
    cv2.rectangle(frame, (100,100), (400,400), (0,255,0), 2)

    # تحويل إلى YCrCb
    ycrcb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCrCb)
# YCrCb = أفضل نموذج لتمييز لون البشرة:
# Y = الإضاءة
# Cr = كمية اللون الأحمر
# Cb = كمية اللون الأزرق

    # عزل لون البشرة
    lower_skin = np.array([0, 135, 85], np.uint8)
    upper_skin = np.array([255, 180, 135], np.uint8)
    mask = cv2.inRange(ycrcb, lower_skin, upper_skin)

    mask = cv2.GaussianBlur(mask, (5,5), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#العثور على الأشكال البيضاء داخل الـ mask.
    if contours:
        cnt = max(contours, key=cv2.contourArea)

        # رسم الكونتور
        cv2.drawContours(roi, [cnt], -1, (255, 0, 0), 2)
#يوضح مكان اليد في الصورة.

# يغطي شكل اليد بالكامل 
        hull = cv2.convexHull(cnt)
        cv2.drawContours(roi, [hull], -1, (0, 0, 255), 2)

#فراغات بين الاصابع 
        hull2 = cv2.convexHull(cnt, returnPoints=False)

        if len(hull2) > 3:
            defects = cv2.convexityDefects(cnt, hull2)
            if defects is not None:
                count = 0

                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])

                    #                  s   = نقطة بداية 
                    # e = نقطة نهاية 
                    # f = أعمق نقطة بينهما
                    # d = عمق 

                    a = math.dist(start, end)
                    b = math.dist(start, far)
                    c = math.dist(end, far)
 #تشكل مثلث نحتاجها لحساب الزوايا 
                    angle = math.degrees(np.arccos((b*b + c*c - a*a) / (2*b*c)))

                    if angle < 60 and d > 10000:
                        count += 1
                        cv2.circle(roi, far, 5, (0, 255, 0), -1)

                cv2.putText(frame, f"Fingers: {count+1}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()