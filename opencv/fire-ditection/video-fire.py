import cv2
import numpy as np
import os

def detect_fire(frame, frame_count, save_path="captured_fire"):
    fire_img = frame.copy()
    hsv = cv2.cvtColor(fire_img, cv2.COLOR_BGR2HSV)

    # Fire color range (orange/yellow flames)
    lower = np.array([18, 100, 100]) 
    upper = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # threshold to avoid noise
            fire_detected = True
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(fire_img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(fire_img, "FIRE", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

    # Save frame if fire is detected
    if fire_detected:
        os.makedirs(save_path, exist_ok=True)
        filename = os.path.join(save_path, f"/home/raoinfotech/vscode/python/opencv/fire-ditection/fire_frame_{frame_count}.jpg")
        cv2.imwrite(filename, fire_img)
        print(f"🔥 Fire captured: {filename}")

    return fire_img, mask
# Load video
cap = cv2.VideoCapture("/home/raoinfotech/vscode/python/opencv/fire-ditection/fire-video.mp4")

if not cap.isOpened():
    print("❌ Error: Could not open video file.")
    exit()

frame_width = 640
frame_height = 480
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ End of video or cannot read frame.")
        break

    frame_count += 1
    frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)

    fire_detected, mask = detect_fire(frame, frame_count)

    cv2.imshow("Fire Detection", fire_detected)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()