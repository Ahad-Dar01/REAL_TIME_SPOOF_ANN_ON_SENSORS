import pandas as pd
import numpy as np
df=pd.read_csv('data.csv')
sensor1x=df['x1']
sensor1y=df['y1']    
result=[]
kurt=[]
d_result=sensor1x+sensor1y
i=1
for object in enumerate(d_result):
    if (object[0]<i*200 and object[0]>=(i-1)*200) :
        kurt.append(sensor1x[object[0]])
print()