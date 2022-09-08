#! /usr/bin/env /usr/bin/python3
#
# Gets all the frames in a video file and stores them as jpeg files in the images directory

import cv2

videofile='video.mp4'
imageDir='images'

video=cv2.VideoCapture(videofile)
#print(type(video))
#
# Video.read() returns a tuple containing a boolean=True and the next frame as a Nimpy array.  If there is no next frame the boolean is False and the frame is None
success, frame=video.read()
count=1
while success:
  cv2.imwrite(f'{imageDir}/{count}.jpg',frame)
  success, frame=video.read()
  count+=1