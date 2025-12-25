import cv2
face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#ملف جاهز يحتوي على كشف القوالب الوجه
captur = cv2.VideoCapture(0)

while True:
    ret, frame = captur.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#تبحث عن الوجوه في الصورة 
#تكبير لتعرف على وجوه باحجام مختلفة 
#عدد المربعات لتكيد الوجوه
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Face", frame)
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break

captur.release()
cv2.destroyAllWindows()
