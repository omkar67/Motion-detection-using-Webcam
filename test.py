import cv2
import pandas as pd
from datetime import datetime

# Initialize the video capture
vid = cv2.VideoCapture(0)

status_list = [None, None]
moment_list = []
df = pd.DataFrame(columns=['Start', 'End'])

# Initialize a background subtractor
fore_bg = cv2.createBackgroundSubtractorMOG2()

while True:
    check, frame = vid.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply background subtraction
    fore_mask = fore_bg.apply(gray)
    
    # Further noise reduction with erosion and dilation
    fore_mask = cv2.erode(fore_mask, None, iterations=2)
    fore_mask = cv2.dilate(fore_mask, None, iterations=2)
    
    # Find contours
    cntrs, _ = cv2.findContours(fore_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cntrs:
        if cv2.contourArea(contour) < 3000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        moment_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        moment_list.append(datetime.now())

    status_list = status_list[-2:]

    key = cv2.waitKey(1)
    
    if key == ord("k"):
        if status == 1:
            moment_list.append(datetime.now())
        break

    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Foreground Mask", fore_mask)

print(status_list)
print(moment_list)

if len(moment_list) % 2 == 1:
    moment_list.pop()

for i in range(0, len(moment_list), 2):
    df.loc[len(df)] = {"Start": moment_list[i], 'End': moment_list[i + 1]}

df.to_csv("times.csv")

vid.release()
cv2.destroyAllWindows()
