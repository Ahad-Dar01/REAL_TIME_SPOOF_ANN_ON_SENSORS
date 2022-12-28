import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
data=pd.read_csv('FINALE_28.csv')
Y = data.iloc[:,-1].values
X = data.iloc[:,1:-1].values
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.01,random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#Initialising ANN
ann = tf.keras.models.Sequential()
#Adding First Hidden Layer
ann.add(tf.keras.layers.Dense(units=10,activation="sigmoid"))
#ann.add(tf.keras.layers.Dense(units=14,activation="sigmoid"))
#ann.add(tf.keras.layers.Dense(units=23,activation="sigmoid"))
#Adding Second Hidden Layer
ann.add(tf.keras.layers.Dense(units=12,activation="sigmoid"))
#Adding Third Hidden Layer
#ann.add(tf.keras.layers.Dense(units=22,activation="sigmoid"))
#Adding Output Layer
ann.add(tf.keras.layers.Dense(units=1,activation="sigmoid"))
#Compiling ANN
ann.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])
#Fitting ANN
ann.fit(X_train,Y_train,batch_size=20,epochs = 50)
#Saving created neural network
ann.save("SENSOR_ANN.h5")