#!/usr/bin/env python3

import random
from random import randint
import os
from time import sleep

video_dir = '/home/pi/videos/'
video_list = []

for file in os.listdir(video_dir):
  if file.endswith('.mp4'):
    video_list.append(file)
if not video_list:
  print ("No videos found in", video_dir, "can't continue...")
  exit()

print("Found the following videos in", video_dir, ":", video_list)

# Trick to blank the screen between videos
ScreenOff = ("/opt/vc/bin/tvservice -o")
ScreenOn = ("/opt/vc/bin/tvservice -p")
os.system(ScreenOff)
sleep(2)
os.system(ScreenOn)


# for i in video_list:
while True: 
  PlayVideoString="omxplayer -s --aspect-mode fill /home/pi/videos/%s" % random.choice(video_list)
  print (PlayVideoString)
  os.system(PlayVideoString)
  holdon = (randint(0,3))
  print("Randomly waiting for:", holdon ,"seconds..")
  sleep(holdon)
