import time
from datetime import datetime

while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/home/raoinfotech/Downloads/currenttime.txt", "w") as f:
        f.write(f"Current Time: {current_time}\n")
    time.sleep(20)

