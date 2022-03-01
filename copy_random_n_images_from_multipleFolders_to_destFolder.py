## code to copy 'n' random images from 'x' number of folder into a destination directory

import random as r
from glob import glob
import os
from shutil import copy

source_folders = ['folder1', 'folder2','folder3']


source_memory = [z for y in source_folders for z in glob(os.path.join(y+'\\'+"*.jpg"))]

dest_folder = "Destination_folder_location"
n=2000
i=0
temp_list = []

while i<=n:
    src = r.choice(source_memory)
    if src not in temp_list:
        temp_list.append(src)
        copy(src, os.path.join(dest_folder,str(i)+'.jpg'))
        i+=1
