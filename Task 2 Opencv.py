import cv2
import numpy as np

cap = cv2.VideoCapture('input.mp4')
fps=30
frame_width = 843
frame_height = 480

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if cap.get(cv2.CAP_PROP_POS_FRAMES) % 4 == 0:
        resized_frame = cv2.resize(frame, (frame_width, frame_height))
        out.write(resized_frame)
    else:
        blank_image = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        out.write(blank_image)

cap.release()
out.release()
