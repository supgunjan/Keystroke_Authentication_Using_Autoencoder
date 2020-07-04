from data_loader import loader
from model import Models
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
import numpy as np
import sys

load_data = loader()    
x_data, y_data, w = load_data.load()
print(x_data[:3])
w = w + w - 1 #no. of features
# print(w)
h = 1
model = Models(h, w)
auto_encoder = model.encode_decoder()
model.encode_decoder()

print(model.encode_decoder().summary())

print(x_data.shape)
# train_x,test_x,train_y,test_y=train_test_split(x_data,y_data,test_size=0.1,random_state=30)

train_x = x_data[:50]
train_y = train_x.copy()
test_x = x_data[50:]
test_y = test_x.copy()


model.fit(train_x, train_y, test_x, test_y)

model.save()

