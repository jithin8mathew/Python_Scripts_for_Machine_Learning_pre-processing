# python code to copy a set of files (eg: *.txt) from folder A to folder B based on the filenames in folder A  
from glob import glob
import os
from shutil import copy

txtFolder = "path to folder A"
jpgFolder = "path to folder B"

txts= glob(txtFolder+'*.txt')
jpgs = glob(jpgFolder+'*.jpg')

db = [os.path.basename(_) for _ in txts]

for x in jpgs:
    if os.path.basename(x).split('.')[0]+".txt" in db:
        copy(os.path.join(txtFolder,os.path.basename(x).split('.')[0]+".txt"), os.path.join(jpgFolder,os.path.basename(x).split('.')[0]+".txt"))
        
    