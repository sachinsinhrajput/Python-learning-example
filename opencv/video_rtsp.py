import cv2

rtsp_url = "http://eyc.synology.me:10001/mjpg/video.mjpg"
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
else:
    print("Video opened successfully.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Resize the frame to 640x480
        resized_frame = cv2.resize(frame, (880, 640))

        # Show resized frame
        cv2.imshow("Video Frame", resized_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Stream ended or failed.")
        break

cap.release()
cv2.destroyAllWindows()