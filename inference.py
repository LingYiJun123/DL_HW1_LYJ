#REMEMBER to note the augmentation parameters, and MODEL USED during training
from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
#REMEMBER TO CHANGE FILPATH AND MODEL_FT

from os import listdir
from os.path import isfile, join
import copy
import re
from PIL import Image


#images=glob.glob("/root/data/amz//train_small/*jpg")
#for image in images:
#img = Image.open(image)
#trans = transforms.ToPILImage()
#trans1 = transforms.ToTensor()
#plt.imshow(trans(trans1(img)))

modelfilepath = "./models/model8.pt"
testpath = "./testing_img_order.txt"
classespath = "./classes.txt"
device = torch.device("cuda:1")

model_ft = models.resnet101()
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 200)
model_ft = model_ft.to(device)
model_ft.load_state_dict(torch.load(modelfilepath))
model_ft.eval()

listoclasses = []

with open(classespath) as f:
    listoclasses = f.readlines()
    

#transform definition

datatransform = transforms.Compose([
        transforms.Resize((320, 320)),
        #transforms.RandomResizedCrop(500,(1,1)),
        #transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])



with open(testpath, 'r') as f:
  
  #lines = f.readline()
  #while lines:
   for lines in f:
    imagefldrpath = "./testing_images/"
    imagepath = os.path.join(imagefldrpath, lines.strip())
    image = Image.open(imagepath)
    image = datatransform(image)
    image = image[None, :].to(device)
 
    outputs = model_ft(image)
    predval, predslbl = torch.max(outputs, 1)  #pred lbl is here
    with open('answer.txt', 'a') as fi:
      fi.write(lines.strip() + " " + listoclasses[predslbl])






#model = torch.load(PATH)
#model.eval()
## Load
#model = Net()
#model.load_state_dict(torch.load(PATH))
#model.eval()