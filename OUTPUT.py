import pandas as pd
df=pd.read_csv('Python.csv')
sensor1x=df['sensor1_x']
sensor2x=df['sensor2_x']
sensor1y=df['sensor1_y']
sensor2y=df['sensor2_y']    
result=[]
d_result=(sensor1x+sensor1y+sensor2x+sensor2y)>1000
for object in d_result:
    result.append(int(object))
df.insert(4,"RESULT",result,True)
print(df)
df.to_csv('ML_APPLICATION.csv')
