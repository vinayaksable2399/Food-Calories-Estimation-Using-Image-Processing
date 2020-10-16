# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:31:30 2019

@author:vinayak sable 
"""

import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
import glob
import cv2
from cnn_model import get_model

path = r'./FOODD'
IMG_SIZE = 400
LR = 1e-3
#Fruits_dectector-{}-{}.model
MODEL_NAME = 'Fruits_dectector-{}-{}.model'.format(LR, '5conv-basic')
no_of_fruits=7
percentage=0.3
no_of_images=100

def create_train_data(path):
    training_data = []
    folders=os.listdir(path)[0:no_of_fruits]
    for i in range(len(folders)):
        label = [0 for i in range(no_of_fruits)]
        label[i] = 1
        print(folders[i])
        k=0
        for j in glob.glob(path+"\\"+folders[i]+"\\*.jpg"):            
            if(k==no_of_images):
                break
            k=k+1
            img = cv2.imread(j)
            img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
            training_data.append([np.array(img),np.array(label)])
    np.save('training_{}_{}_{}.npz'.format(no_of_fruits,no_of_images,IMG_SIZE),training_data)
    shuffle(training_data)
    return training_data,folders

training_data,labels=create_train_data(path)
# training_data=np.load('training_{}_{}_{}.npz'.format(no_of_fruits,no_of_images,IMG_SIZE))
size=int(len(training_data)*percentage)
train = training_data[:-size]
test=training_data[-size:]

X = np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,3)
test_y = [i[1] for i in test]

model=get_model(IMG_SIZE,no_of_fruits,LR)

model.fit({'input': X}, {'targets': Y}, n_epoch=10, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model_save_at=os.path.join("model",MODEL_NAME)
model.save(model_save_at)
print("Model Save At",model_save_at)