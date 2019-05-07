from lane import *
import cv2


video = cv2.VideoCapture('examples/project_video.mp4')
if not video.isOpened():
    quit()

ret, frame = video.read()
while ret:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
    img_undist, img_lane_augmented, lane_info = lane_process(frame)
    cv2.imshow('Augmented', img_lane_augmented)
    ret, frame = video.read()

video.release()
cv2.destroyAllWindows()
