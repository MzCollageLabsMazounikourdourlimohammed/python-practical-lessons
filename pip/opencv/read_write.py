import cv2
import matplotlib.pyplot as plt
import numpy as np

# # تحميل الصورة من ملف
img = cv2.imread("C:/mz/learn/python_course/pip/opencv/n.png")  # ضع هنا مسار الصورة


#     # # عرض الصورة في نافذة
# cv2.imshow("Image", img)
    
#     # # الانتظار حتى تضغط أي زر
# cv2.waitKey(0)




# # #==============

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #cv2.cvtColor ==> دالة تحول الصورة من الوان الى صيغة اخرى 
# #img  صورة الاصلية 
# #cv2.COLOR_BGR2GRAY = هنا تحويل من الالوان الى رمادي 
# #صورة تتحول من الوان 0-255 لبى ابيض والاسود 

# # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("Gray Image", gray)
# # cv2.imshow("Gray Image", rgb)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()


# plt.imshow(img)
# plt.title("RGB Image for Matplotlib")
# plt.show()



# #=================
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower_red1 = np.array([0,0,70])

# upper_red1 = np.array([10,255,255])

# #اذا كان ضمن النطاق يبقى اذا كان خارج النطاق يتحول لاى الاسود
# mask = cv2.inRange(hsv, lower_red1, upper_red1)
# result = cv2.bitwise_and(img, img, mask=mask)
# #اي  ماسك فيه 255 يبقى اخر يتحول 

# cv2.imshow("Red Color", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#=========



# # تحويل الصورة من BGR إلى HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# #h الون الاساسي 
# #s التشبع 
# #v السطوع 

# # تحديد نطاق اللون الأحمر في HSV
# # lower_red1 = np.array([0, 120, 70])
# # upper_red1 = np.array([10, 255, 255])
# lower_Blue1 = np.array([0, 150, 70])
# upper_Blue1 = np.array([255, 255, 255])



# # عمل قناع للون الأحمر


# mask = cv2.inRange(hsv, lower_Blue1, upper_Blue1)
# # تغيير اللون: إنشاء نسخة صفرية

# h, s, v = cv2.split(hsv)
# # 0red 30yellow 60green 120Blue 150Purple
# # تحويل الأحمر إلى أصفر/أخضر
# h[mask > 0] = 150  # تقريبًا لون أصفر مخضر
# s[mask > 0] = 0  # تشبع كامل
# v[mask > 0] = 0  # سطوع كامل

# # دمج القنوات مرة أخرى
# hsv_new = cv2.merge([h, s, v])

# # تحويل HSV إلى BGR للعرض
# img_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)

# cv2.imshow("Original", img)
# cv2.imshow("New Image", img_new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#==============



#==============

# مستطيل أخضر
# cv2.rectangle(img, (50,50), (200,200), (0,255,0), 3)
# # cv2.rectangle(image, pt1, pt2, color, thickness)
# # image → الصورة التي تريد الرسم عليها.
# # pt1 → النقطة العليا اليسرى للمستطيل (x1, y1).
# # pt2 → النقطة السفلى اليمنى للمستطيل (x2, y2).
# # color → لون المستطيل (B, G, R) (OpenCV يستخدم BGR).
# # thickness → سمك الخط.
# # إذا كانت - → المستطيل مملوء بالكامل.

# # دائرة زرقاء
# cv2.circle(img, (300,300), 50, (0,0,255), 1) 
# # cv2.circle(image, center, radius, color, thickness) 
# # image → الصورة التي تريد الرسم عليها.
# # center → مركز الدائرة (x, y).
# # radius → نصف قطر الدائرة بالبيكسل.
# # color → لون الدائرة (B, G, R) لأن OpenCV يستخدم صيغة BGR.
# # thickness → سمك الخط:
# # إذا كانت -1 → الدائرة مملوءة بالكامل.
# # أي رقم موجب → سمك حدود الدائرة.

# # خط أحمر
# cv2.line(img, (0,0), (400,400), (0,0,255), 5)
# # cv2.line(image, pt1, pt2, color, thickness)


# cv2.imshow("Shapes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#==============

# captur = cv2.VideoCapture(0)
#   # 0 = الكاميرا الافتراضية
#   #اذا كانت 1 كاميرا ثانية 

# while True:
#     ret, frame = captur.read() 
#     # إذا تمت قراءة يخرجها 
#      # قراءة إطار
#     if not ret:
#         break

#     cv2.imshow(" Camera", frame)

#     if cv2.waitKey(1) & 0xFF == ord('0'):
#         #انتظار ثانية لكسر 
#         #لضمان التوافق مع انظمة مختلفة
#         #اذا قام المستخدم على صفر 
#         break

# captur.release()  # تحرير الكاميرا
# cv2.destroyAllWindows()

#===================
# face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# #ملف جاهز يحتوي على كشف القوالب الوجه
# captur = cv2.VideoCapture(0)

# while True:
#     ret, frame = captur.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# #تبحث عن الوجوه في الصورة 
# #تكبير لتعرف على وجوه باحجام مختلفة 
# #عدد المربعات لتكيد الوجوه
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

#     cv2.imshow("Face", frame)
#     if cv2.waitKey(1) & 0xFF == ord('0'):
#         break

# captur.release()
# cv2.destroyAllWindows()



#==============
# import cv2
# import numpy as np

# captur = cv2.VideoCapture(0)

# while True:
#     ret, frame = captur.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)

#     # تحويل الصورة إلى رمادية
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # عكس الألوان لتصبح اليد مضيئة والخلفية داكنة (مثل الأشعة)
#     inverted = cv2.bitwise_not(gray)

#     # تحويل الصورة إلى BGR لعرضها في OpenCV
#     # xray_effect = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
#     xray_effect = cv2.convertScaleAbs(inverted, alpha=0.5, beta=0)
#     cv2.imshow("X-ray Hand", xray_effect)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# captur.release()
# cv2.destroyAllWindows()
