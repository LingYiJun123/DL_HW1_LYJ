from __future__ import print_function, division

import time
import os
import copy
import shutil

trainlabelspath = '../training_labels.txt'
src_path = '../training_images'
dst_path ='./'

#os.path.join(data_dir, x)

with open(trainlabelspath, 'r') as f:
  
  lines = f.readline()
  while lines:
    lines = f.readline()
    image, classn = lines.split(' ')
    classno, _ = classn.split('.')
    print(image)
    print(classno)
    print('-------')
    shutil.copy(os.path.join(src_path, image), os.path.join(dst_path, classno))