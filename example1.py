# -*- coding: utf-8 -*-
"""example1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fRWM1bAMhgwW1jLsPLWwG9f07JlWJsGh
"""

import numpy as np
from numpy import asarray

data = [[3,3,2,1,0],
        [0,0,1,3,1],
        [3,1,2,2,3],
        [2,0,0,2,2],
        [2,0,0,0,1]]
data = np.asarray(data)
data = data.reshape(1,5,5,1)

kernel = [[[[0]],[[1]],[[2]],
          [[2]],[[2]],[[0]],
          [[0]],[[1]],[[2]]]]
weights = [asarray(kernel), asarray([0.0])]

from keras.models import Sequential
from keras.layers import Conv2D
#create model
model = Sequential()
model.add(Conv2D(1, (3,3), input_shape=(5,5,1)))
model.summary()

