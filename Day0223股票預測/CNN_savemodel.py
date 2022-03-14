from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense

(train_feature, train_label), (test_feature , test_label) = mnist.load_data()
train_feature_vector = train_feature.reshape(len(train_feature),28,28,1).astype('float32')
test_feature_vector = test_feature.reshape(len(test_feature),28,28,1).astype('float32')
train_feature_normalize = train_feature_vector/255
test_feature_normalize = test_feature_vector/255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

model = Sequential()
model.add(Conv2D(filters=10,
                 kernel_size=(5,5),
                 padding='same',
                 input_shape=(28,28,1),
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=20,
                 kernel_size=(5,5),
                 padding='same',
                 activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=10,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

model.fit(x=train_feature_normalize, y=train_label_onehot,
          validation_split=0.2, epochs=10, batch_size=200, verbose=2)
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print('\n準確率=', scores[1])
model.save('Mnist_cnn_model.h5')
print("\nMnist_cnn_mode.h5 模型儲存完畢")