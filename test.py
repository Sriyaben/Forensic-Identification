import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import os
from os.path import dirname
import cv2

dataset = pd.read_csv("temp.csv",nrows=3200)
dataset = dataset.values

for i in range(len(dataset)):
    name = dataset[i,0]
    fname = os.path.basename(name)
    parent = os.path.basename(dirname(name))
    print(name+" "+fname+" "+parent)
    image = cv2.imread(name)
    cv2.imwrite('mine/'+parent+"/"+fname,image)


