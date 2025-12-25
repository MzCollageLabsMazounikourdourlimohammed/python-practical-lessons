import cv2

captur = cv2.VideoCapture(0)
  # 0 = الكاميرا الافتراضية
  #اذا كانت 1 كاميرا ثانية 

while True:
    ret, frame = captur.read() 
    # إذا تمت قراءة يخرجها 
     # قراءة إطار
    if not ret:
        break

    cv2.imshow(" Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('0'):
        #انتظار ثانية لكسر 
        #لضمان التوافق مع انظمة مختلفة
        #اذا قام المستخدم على صفر 
        break

captur.release()  # تحرير الكاميرا
cv2.destroyAllWindows()
0