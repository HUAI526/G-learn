import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

sequence_length = 10
split = 0.95

pd.options.mode.chained_assignment = None
filename = 'twstock_all.csv'
df = pd.read_csv(filename, encoding = 'big5')
dfprice=pd.DataFrame(df['收盤價'])

data_all = np.array(dfprice).astype(float)
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)
data=[]
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i:i + sequence_length + 1])
reshaped_data = np.array(data).astype('float64')
x = reshaped_data[:, :-1]
y = reshaped_data[:, -1]
split_boundary = int(reshaped_data.shape[0] * split)
train_x = x[: split_boundary]
test_x = x[split_boundary:]
train_y = y[: split_boundary]
test_y = y[split_boundary:]

model = Sequential()
model.add(LSTM(input_shape=(sequence_length,1),units=256,unroll=False))
model.add(Dense(units=1))
model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])
model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1,verbose=2)

model.save('Stock_rnn_model.h5')
print("\nStock_rnn_mode.h5 模型儲存完畢")