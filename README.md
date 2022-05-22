# Face-Detection-with-Camera
Real time detect from a webcam.
<p align="center">
  <img width="683" height="352" src="https://user-images.githubusercontent.com/75435070/169713922-0ce654da-b00a-41ba-8ce0-04a36aa8fb7b.jpeg">
</p>

## Required Libraries
`` pip3 install opencv-python``

## If there is an error in the code, first follow the steps below       
* cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) <---- Select your camera as 0 or 1. On laptops, if you are using an external camera, disable the computer's own camera.
* face_cascade = cv2.CascadeClassifier("C:\\Users\\fujitsu\\Desktop\\Yeni_klasor\\haarcascade_frontalface_default.xml") <---- Check the location where the haarcascade_frontalface_default.xml file is located and type the ' \ '  sign correctly when typing the location.
* Press the 'q' key on the keyboard to close the pop-up screen



