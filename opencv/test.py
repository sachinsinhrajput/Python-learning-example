import cv2
http="http://eyc.synology.me:10001/mjpg/video.mjpg"
cap=cv2.VideoCapture(http)
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit() 
else:
    while True:
        
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        else:
            cv2.imshow("",frame)
            resize=cv2.resize(frame,(880,640))
            cv2.imshow("Video Frame",resize)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()