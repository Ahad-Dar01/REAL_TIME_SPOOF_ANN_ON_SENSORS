import pandas as pd
import csv
import numpy as np
sensor1x=[]
sensor1y=[]
def statistical(sensor11,sensor12):
 sensor1x=sensor11
 sensor1y=sensor12
 result=[]
 kurt=[]
 result2=[]
 #result2=[]
 kurt2=[] 
 #d_result=sensor1x+sensor1y
 i=1
 j=1
 for object in enumerate(sensor1x):
    if (object[0]<i*200 and object[0]>=(i-1)*200 ):
        result.append(sensor1x[object[0]])
        if (object[0]==(200*i-1)):
            fmean=np.mean(result)
            fmeanl=[]
            std=[]
            for ff in result:
                fmeanl.append(fmean)
                if (len(fmeanl)==200):
                 std=np.subtract(result,fmeanl)
                 stds=result-np.square(fmeanl)
                 std=np.square(std)
                 std=np.square(std)
                 stds=np.square(stds)
                 stdn=np.sum(std)
                 stdd=np.sum(stds)
                 kurt.append(200*np.divide(stdn,stdd))
                 result=[]
                 i=i+1

 for object in enumerate(sensor1y):
    if (object[0]<j*200 and object[0]>=(j-1)*200 ):
        result2.append(sensor1y[object[0]])
        if (object[0]==(200*j-1)):
            fmean=np.mean(result2)
            fmeanl=[]
            std=[]
            for ff in result2:
                
                fmeanl.append(fmean)
                if (len(fmeanl)==200):
                 std=np.subtract(result2,fmeanl)
                 stds=result2-np.square(fmeanl)
                 std=np.square(std)
                 std=np.square(std)
                 stds=np.square(stds)
                 stdn=np.sum(std)
                 stdd=np.sum(stds)
                 kurt2.append(200*np.divide(stdn,stdd))
                 result2=[]
                 j=j+1
 #print(kurt2)
#df.create_csv(0,"RESULT",kurt,True)
#df.to_csv('MLk_APPLICATION.csv')
#print(enumerate(d_result))
#f=open('Python22.csv', 'w')     
#fieldnames = ['sensor1_x_Kur','sensor1_y_Kur']    
#writer = csv.DictWriter(f, fieldnames=fieldnames)    
#writer.writeheader()    
#for i in range(100):
 #    writer.writerow({'sensor1_x_Kur': kurt[i],'sensor1_y_Kur': kurt2[i]})    
#f.close()
 return kurt,kurt2