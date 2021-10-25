from __future__ import print_function, division

import time
import os
import copy

#for i in range(1,201):
#  print("{:03d}".format(i))

#dirName = 'tempDir2/temp2/temp'
## Create target directory & all intermediate directories if don't exists
#os.makedirs(dirName)  

for i in range(1,201):
  os.makedirs("{:03d}".format(i))
