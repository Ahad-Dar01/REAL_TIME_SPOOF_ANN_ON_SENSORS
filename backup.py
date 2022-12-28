import tensorflow as tf
import pandas as pd
import threading
import Utility as ul
from main import SO
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data=pd.read_csv('MLS_APPLICATION.csv')
model=tf.keras.models.load_model("SENSOR_ANN.h5")
X = data.iloc[:,1:-1].values
b=sc.fit(X)
sensor1x=[]
sensor2x
while(1): 
    for
    Burhan=[SO.read_thread(1)['s11'],SO.read_thread(1)['s12']]
    #,SO.read_thread(1)['s21'],SO.read_thread(1)['s22']]
    a=sc.transform([Burhan])
    prediction=model.predict(a)
    print (prediction)
    SO.write_thread(int(prediction*10000))
