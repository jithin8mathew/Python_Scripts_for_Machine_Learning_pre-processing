from glob import glob
from PIL import Image
import os
from tqdm import tqdm

file_path = "path to image files"

images = glob(file_path+"\\"+"*.png")

for _ in tqdm(images):    
    im1 = Image.open(_)
    im1.save(os.path.join(os.path.dirname(_),os.path.basename(_).split('.')[0]+'.jpg'))
