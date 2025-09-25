import cv2
import math

# Open video file
cap = cv2.VideoCapture("/home/raoinfotech/Downloads/video.mp4")  

fps = int(cap.get(cv2.CAP_PROP_FPS))              # Frames per second
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
duration = frame_count / fps                      # Total duration in seconds

frame_interval =1* fps                         # Frames to skip (30 sec)

frame_no = 0
saved_no = 0

while frame_no < frame_count:
    # Set the video position to the frame we want
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    if not ret:
        break

    # Save the frame
    cv2.imwrite(f"/home/raoinfotech/Pictures/Fire2/frame37_{saved_no:03d}.jpg", frame)
    saved_no += 1

    # Jump 30 seconds ahead
    frame_no += frame_interval
cap.release()
print("Frames saved")