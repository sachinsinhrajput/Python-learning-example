import cv2
import numpy as np
import matplotlib.pyplot as plt
face_cascade=cv2.CascadeClassifier("/home/raoinfotech/vscode/python/opencv/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier('/home/raoinfotech/vscode/python/opencv/haarcascade_eye.xml')
def adjusted_detect_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
        
    return face_img
def detect_eyes(img):
    eye_img = img.copy()
    eye_rect = eye_cascade.detectMultiScale(eye_img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
        
    return eye_img
img = cv2.imread('/home/raoinfotech/vscode/python/opencv/man.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

face = adjusted_detect_face(img_copy1)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))

cv2.imwrite('/home/raoinfotech/vscode/python/opencv/photo/face.jpg', face)
eyes = detect_eyes(img_copy2)
plt.imshow(cv2.cvtColor(eyes, cv2.COLOR_BGR2RGB))

cv2.imwrite('/home/raoinfotech/vscode/python/opencv/photo/eyes.jpg', eyes)