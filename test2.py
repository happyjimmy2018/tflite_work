import numpy as np
import cv2



#!/usr/bin/python3
from picamera2 import Picamera2
import cv2

cap = cv2.VideoCapture(0)

# Grab images as numpy arrays and leave everything else to OpenCV.

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    im = picam2.capture_array()
    # Our operations on the frame come here
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
