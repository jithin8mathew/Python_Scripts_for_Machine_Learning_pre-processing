import cv2
import sys
import argparse
import os

# videoInPath = "F:\\ABEN\\Soy_pod_count_project\\raw_data\\PXL_20210925_191021944.mp4"
videoOutPath= sys.argv[2]

# print("inpath : "+sys.argv[1])
# print("outpath : "+videoOutPath)
# parser = argparse.ArgumentParser(description='Video frame extraction')
# parser.add_argument('--inpath', action="store", dest='videoInPath', default=0)
# parser.add_argument('--outpath', action="store", dest='videoOutPath', default=1)

# vidIn = parser.parse_args()
# vidOut = parser.parse_args()


vidcap = cv2.VideoCapture("F:\\ABEN\\Soy_pod_count_project\\raw_data\\PXL_20210925_191959963.mp4")
success,image = vidcap.read()
count = 0
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
while success:
    if count % 10 == 0:
        cv2.imwrite("F:\\ABEN\\Soy_pod_count_project\\raw_data\\PXL_20210925_191959963\\"+"frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
    count += 1

