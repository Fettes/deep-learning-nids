from DataProccess import DataProccess
from keras.optimizers import Adam
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Dropout, GRU
import keras 
import numpy as np
from keras.utils import np_utils
import time


# get and proccess data
data = DataProccess()
# x_train, y_train, x_test, y_test, x_test_21, y_test_21 = data.return_proccessed_data_multiclass()
x_train, y_train, x_test, y_test, x_test_21, y_test_21 = data.return_proccessed_data_binary()


# reshape input to be [samples, timesteps, features]
x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1])
x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1])
x_test_21 = x_test_21.reshape(x_test_21.shape[0], 1, x_test_21.shape[1])

# multiclass
# y_train=np_utils.to_categorical(y_train)
# y_test=np_utils.to_categorical(y_test)
# y_test_21=np_utils.to_categorical(y_test_21)

start = time.time()

model = Sequential()
model.add(GRU(30, input_shape = (x_train.shape[1],x_train.shape[2]), return_sequences=True))
model.add(Dropout(0.1))

model.add(GRU(30, return_sequences=True))
model.add(Dropout(0.1))

model.add(GRU(30, return_sequences=False))
model.add(Dropout(0.1))

# binary
model.add(Dense(1))
model.add(Activation('hard_sigmoid'))

# multiclass
# model.add(Dense(5))
# model.add(Activation('softmax'))

model.summary()

# optimizer
adam = Adam(lr=0.0001)

#binary
model.compile(optimizer = adam, loss = 'binary_crossentropy', metrics=['accuracy'])

#multiclass
# model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, batch_size=32)

# save the model
# model.save("model.hdf5")

print("--- %s seconds ---" % (time.time() - start))

loss, accuracy = model.evaluate(x_test, y_test, batch_size=32)
loss_21, accuracy_21 = model.evaluate(x_test_21, y_test_21, batch_size=32)

print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))
print("\nLoss 21: %.2f, Accuracy 21: %.2f%%" % (loss_21, accuracy_21*100))

y_pred = model.predict_classes(x_test)
y_pred_21 = model.predict_classes(x_test_21)

print("\nAnomaly in Test: ",np.count_nonzero(y_test, axis=0))
print("\nAnomaly in Prediction: ",np.count_nonzero(y_pred, axis=0))

print("\nAnomaly in Test 21: ",np.count_nonzero(y_test_21, axis=0))
print("\nAnomaly in Prediction 21: ",np.count_nonzero(y_pred_21, axis=0))