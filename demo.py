from calorie import calories
from cnn_model import get_model
import os  
import cv2
import numpy as np

IMG_SIZE = 400
LR = 1e-3
no_of_fruits=7

MODEL_NAME = 'Fruits_dectector-{}-{}.model'.format(LR, '5conv-basic')

model_save_at=os.path.join("model",MODEL_NAME)

model=get_model(IMG_SIZE,no_of_fruits,LR)

model.load(model_save_at)
labels=list(np.load('labels.npy'))

test_data='test_image.JPG'
img=cv2.imread(test_data)
img1=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
model_out=model.predict([img1])
result=np.argmax(model_out)
name=labels[result]
cal=round(calories(result+1,img),2)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.title('{}({}kcal)'.format(name,cal))
plt.axis('off')
plt.show()