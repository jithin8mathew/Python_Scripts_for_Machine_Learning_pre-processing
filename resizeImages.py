# Resize image with PIL with image height proportional to the new width
# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

from PIL import Image
from glob import glob
import sys

basewidth = 1024

inpath = sys.argv[1]
outpath = sys.argv[2]
print(inpath)
print(outpath)


images = glob(inpath+"\\"+"*.jpg")

count=0
for _ in images:
    img = Image.open(_)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(outpath+"\\"+str(count)+'.jpg')
    count+=1