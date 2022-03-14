
from glob import glob
import os 

file_path = "path_to_image + annotation folder"

images = glob(file_path+"\\"+"*.jpg") #change the image file extension
xmls = glob(file_path+"\\"+"*.xml") #change the annotation file extension

images_ = set([os.path.basename(_).rstrip('.jpg') for _ in images])
xmls_ = set([os.path.basename(_).rstrip('.xml') for _ in xmls])

if images_ - xmls_ is not None:
    temp = images_ - xmls_
    for _ in temp:
        os.remove(file_path+"\\"+_+".jpg") #change the image file extension
        print(_+".jpg removed")
if xmls_ - images_ is not None:
    temp = xmls_ - images_
    for _ in temp:
        os.remove(file_path+"\\"+_+".xml") #change the xml file extension
        print(_+".xml removed")