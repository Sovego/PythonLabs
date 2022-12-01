import time
import cv2
import numpy as np


cap = cv2.VideoCapture(0);
FPS = 30
targetDelay = 1000 / FPS
cap.set(3, 1280)
cap.set(4, 720)

ret, frame1 = cap.read()
ret, frame2 = cap.read()
tick = 0
trigger = True
while cap.isOpened():
    Q_st = time.time()
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None,iterations=3)
    rg_layout = cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)
    rg_layout[dilated.astype(bool)] = [0, 0, 255]
    rg_layout[np.logical_not(dilated.astype(bool))] = [0, 255, 0]
    if trigger:
        frame_rg = cv2.addWeighted(frame1, 0.7, rg_layout, 0.8, 0)
        frame_rg = cv2.putText(frame_rg, "Red", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 255), 1)
    else:
        frame_rg = frame1.copy()
        frame_rg = cv2.putText(frame_rg, "Green", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 255), 1)
    cv2.imshow("frame1", frame1)
    cv2.imshow("ff", rg_layout)
    cv2.imshow('ww', frame_rg)
    frame1 = frame2
    ret, frame2 = cap.read()
    Q_end = time.time()
    timePerFrame = Q_end - Q_st
    delay = targetDelay - timePerFrame * 1000
    if delay < 0: delay = 1
    if cv2.waitKey(delay) == 27:
        break
    tick += 1
    if tick == 90:
        trigger = not trigger
        tick = 0
cap.release()
cv2.destroyAllWindows()
