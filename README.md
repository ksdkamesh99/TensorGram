A realtime remote service to get the keras callbacks to the telegram including the details of metrics 

## Features:-

1. It helps by getting the updates of your model including metrics and loss function graphs which help user the view and get to a statistical conclusion about the model remotely.
2. It is a biggest advantage for the users who need not spend hours and hours infront of system for watching the updates of the model.
3. Updates you get are from a telegram bot.

## Installation:-

You can easily install this telegram using following command.
```
pip install tensorgram
```
## Dependencies/Requirements:-

1. Keras
2. Tensorflow
3. Requests
4. Matplotlib

#### Works on python>=3.7

## How to use:-

1. Create a nueral network in keras.The sample code is as follows.
```
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np 
import keras

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(8, input_dim=2))
model.add(Activation('tanh'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

sgd = SGD(lr=0.1)
model.compile(loss='binary_crossentropy', optimizer=sgd,metrics=['accuracy'])

```

2. Now go to Telegram app and search for @tensorgram_bot and join the channel by clicking on the chat.
<center><img src="Images/start.jpeg" width=200px></center>
3. This application send you the data based on the unique chat id for every user in telegram. So to get your chat id you need to go to search and type @chatid_echo_bot and click on start to get your unique chat id.
<center><img src="Images/chatid.jpeg" width=200px></center>


4. Store it safely as it will be required later

5. Now we need to import the TensorGram from tensorgram library using following code.

```
from tensorgram import TensorGram
```

6. Now we need to create a object of TensorGram by specifying the following attributes like model name and chat id which you obtained before.

```
tf=TensorGram("model-name","123456789")
```

7. Now you can start training the model and specify the object in the callbacks.

```
model.fit(X, y, batch_size=1, epochs=10,callbacks=[tf],verbose=1)
```

8. Now if you open the telegram app you will find the updates as follows.


## Licence:-

This code is licensed under the MIT license, see LICENSE.txt.

