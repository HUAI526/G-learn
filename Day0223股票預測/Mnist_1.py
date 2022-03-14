import numpy as np
from keras.utils import np_utils
from Day0223.grapManage import train_feature_normalize
from IPython.core.pylabtools import activate_matplotlib
np.random.seed(10)
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense

(train_feature, train_label), (test_feature , test_label) = mnist.load_data()
train_feature_vector = train_feature.reshape(len(train_feature),784).astype('float32')
test_feature_vector = train_feature.reshape(len(train_feature),784).astype('float32')
train_feature_normalize = train_feature_vector/255
test_feature_normalize = test_feature_vector/255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(train_label)

model = Sequential()
model.add(Dense(units=256, 
                input_dim = 784,
                kernel_initializer='normal',
                activation='relu'))
model.add(Dense(units=10, 
                kernel_initializer='normal',
                activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

model.fit(x=train_feature_normalize, y=train_label_onehot,
          validation_split=0.2, epochs=10, batch_size=200, verbose=2)
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print('\n準確率=', scores[1])
