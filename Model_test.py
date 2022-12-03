import tensorflow as tf
import pandas as pd
import time
import random
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data=pd.read_csv('ML_APPLICATION.csv')
model=tf.keras.models.load_model("SENSOR_ANN.h5")
X = data.iloc[:,1:-1].values
b=sc.fit(X)
while(1): 
    Burhan=[random.gauss(100,10),random.gauss(200,10),random.gauss(300,10),random.gauss(400,10)]
    a=sc.transform([Burhan])
    prediction=model.predict(a)
    print (prediction)
    time.sleep(4)
