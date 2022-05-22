import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\fujitsu\\Desktop\\Yeni_klasor\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    _,img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        X = x+w//2
        Y = y+h//2

        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)
        cv2.circle(img,(x+w//2,y+h//2),2,(0,0,255),3)
        cv2.putText(img, str("KORDINATLAR") ,(20,30),cv2.FONT_HERSHEY_COMPLEX,  1,(0,255,255),2,cv2.LINE_AA)
        cv2.putText(img, str("X=") ,(20,60),cv2.FONT_HERSHEY_COMPLEX,  1,(0,255,255),2,cv2.LINE_AA)
        cv2.putText(img, str(X) ,(70,60),cv2.FONT_HERSHEY_COMPLEX,  1,(0,255,255),2,cv2.LINE_AA)
        cv2.putText(img, str("Y=") ,(20,90),cv2.FONT_HERSHEY_COMPLEX,  1,(0,255,255),2,cv2.LINE_AA)
        cv2.putText(img, str(Y) ,(70,90),cv2.FONT_HERSHEY_COMPLEX,  1,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()