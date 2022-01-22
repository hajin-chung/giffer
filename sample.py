import cv2 as cv
import numpy
import sys
import datetime
import math

def log(msg):
  now = datetime.datetime.now()
  timestamp = now.strftime("%H:%M:%S")
  print(f"[{timestamp}] ", end="")
  print(msg)

def videoTest():
  cap = cv.VideoCapture('test.mp4')
  width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
  frameCount = cap.get(cv.CAP_PROP_FRAME_COUNT)
  progressBarWidth = 10

  log(f"frame size {width}x{height}")
  log(f"frame count {frameCount}")

  frameIdx = 0
  while cap.isOpened():
    frameIdx += 1
    ret, frame = cap.read()

    if not ret:
      log("Can't recieve frame")
      break

    # draw video progress bar to frame
    cv.rectangle(
      frame, 
      (0, math.floor(height-progressBarWidth)), 
      (math.floor(width * frameIdx/frameCount), math.floor(height)),
      (0, 255, 0),
      -1
    )

    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
      log("video stop")
      break
    elif key == ord(' '):
      cv.waitKey(-1)
    # elif key == ord('a')
  
  cap.release()
  cv.destroyAllWindows()