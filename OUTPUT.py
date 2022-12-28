import pandas as pd
#df=pd.read_csv('PythonKURT28DECNON.csv')
#sensor1x=df['sensor1_x_Kur']
#sensor1y=df['sensor1_y_Kur']    
#df2=pd.read_csv('PythonKURT28DEC.csv')
#sensor1x2=df2['sensor1_x_Kur']
#sensor1y2=df2['sensor1_y_Kur']   
#result=[]
#result2=[]
#d_result=sensor1x+sensor1y
#d_result2=sensor1x2+sensor1y2
#for object in enumerate(d_result):
    #if (object[0]>99):
 #       result.append(0)
  #  result.append(0)
 #   #else:
     #   result.append(0)
#df.insert(2,"RESULT",result,True)
#df.drop('n', axis=1, inplace=True)
#for object in enumerate(d_result2):
   # if (object[0]>99):
 #      result2.append(1)
  #  result2.append(1)
 #   #else:
     #   result.append(0)
#df2.insert(2,"RESULT",result2,True)
#df.drop('n', axis=1, inplace=True)
#print(df)
#a=pd.concat([df,df2],axis=0)
#df.to_csv('MLFF_nf28dec2022.csv')
#df2.to_csv('MLFF_f28dec2022.csv')

nf=pd.read_csv("MLFF_nf28dec2022.csv")
f=pd.read_csv("MLFF_f28dec2022.csv")
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
#f.drop('n', axis=1, inplace=True)
#nf.drop('n', axis=1, inplace=True)
faulty_final=pd.concat([f,nf],axis=0)
#nonfaulty_final=pd.concat([nf,nfp],axis=0)
faulty_final.to_csv('FINALE_28.csv')

#print(enumerate(d_result))

