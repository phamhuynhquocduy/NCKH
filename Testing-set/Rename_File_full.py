import PIL
from PIL import Image
import glob
import matplotlib.pyplot as plt
import numpy as np
import os

path_rename = "Full/Rename"
image_folder = "Full"
filename_abnormal = "AnBinh_Dataset_abnormal_"
filename_normal = "AnBinh_Dataset_normal_"
if not os.path.exists(path_rename):
    os.makedirs(path_rename)
i = 1;
j = 1;
for filename in glob.glob(image_folder+"/*.jpg"):
    print (filename)
    line_i = os.path.splitext(filename)[0].split("_")
    last = line_i[-1]
    print(line_i)

    #x = len(line_i) - 2
    
    im=Image.open(filename)
    
    if(line_i[2] == 'abnormal'):
        im.save('./'+path_rename+'/'+filename_abnormal+str(i)+'_full.jpg')
        i = i+1;
    else:
        im.save('./'+path_rename+'/'+filename_normal+str(j)+'_full.jpg')
        j = j+1;
    
