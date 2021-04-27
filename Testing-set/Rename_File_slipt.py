import PIL
from PIL import Image
import glob
import matplotlib.pyplot as plt
import numpy as np
import os

foldername_left = "Left"
foldername_right = "Right"

name_abnormal_ab = "AnBinh_Dataset_abnormal_"
name_normal_ab = "AnBinh_Dataset_normal_"


if not os.path.exists(foldername_left):
    os.makedirs(foldername_left)
    
if not os.path.exists(foldername_right):
    os.makedirs(foldername_right)

#------xu ly du lieu benh vien AB--------
i = 1
j = 1
for a in range(1,51):
    location_abnormal = 'Split/'+name_abnormal_ab + str(a) +'_full'
    print(location_abnormal)
    for filename_1 in glob.glob(location_abnormal+"/*.jpg"):
        print (filename_1)
        line_1 = os.path.splitext(filename_1)[0].split("_")
        print(line_1)
        x = len(line_1) - 2
        im=Image.open(filename_1)

        if(line_1[x] == 'C1'):
            im.save(foldername_left+'/'+name_abnormal_ab+str(i)+'_left.jpg')
        else:
            im.save(foldername_right+'/'+name_abnormal_ab+str(i)+'_right.jpg')
    i = i + 1
    
for b in range(1,51):
    location_normal = 'Split/'+name_normal_ab + str(a) +'_full'
    for filename_2 in glob.glob(location_normal+"/*.jpg"):
        print (filename_2)
        line_2 = os.path.splitext(filename_2)[0].split("_")
        print(line_2)
        y = len(line_2) - 2

        im=Image.open(filename_2)

        if(line_2[y] == 'C1'):
            im.save(foldername_left+'/'+name_normal_ab+str(j)+'_left.jpg')
        else:
            im.save(foldername_right+'/'+name_normal_ab+str(j)+'_right.jpg')
    j = j + 1
