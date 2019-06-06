import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("data/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("data/haarcascade_smile.xml")
# img = cv2.imread("img/test1.jpg")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img = cv2.bilateralFilter(src=img, d=0, sigmaColor=50, sigmaSpace=5)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # smile = smile_cascade.detectMultiScale(
        #     roi_gray,
        #     scaleFactor=1.16,
        #     minNeighbors=35,
        #     minSize=(25, 25),
        #     flags=cv2.CASCADE_SCALE_IMAGE,
        # )
        # for (x2, y2, w2, h2) in smile:
        #     cv2.rectangle(roi_color, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
        #     cv2.putText(img, "Smile", (x, y - 7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
