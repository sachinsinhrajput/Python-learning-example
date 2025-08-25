import cv2
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if ret:
        # Resize the frame to 880x640
        resized_frame = cv2.resize(frame, (880, 640))

        # Show resized frame
        cv2.imshow("Video Frame", resized_frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Stream ended or failed.")
        break