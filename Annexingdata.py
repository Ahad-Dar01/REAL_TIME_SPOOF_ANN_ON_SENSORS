import pandas as pd
#fp=pd.read_csv("faulty2.csv")
#nfp=pd.read_csv("nonfaulty2.csv")
nf=pd.read_csv("MLF_28dec2022.csv")
f=pd.read_csv("MLF_nf28dec2022.csv")
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
f.drop('n', axis=1, inplace=True)
nf.drop('n', axis=1, inplace=True)
faulty_final=pd.concat([f,nf],axis=0)
#nonfaulty_final=pd.concat([nf,nfp],axis=0)
faulty_final.to_csv('28ANNEXEDFAULTY.csv')
#nonfaulty_final.to_csv('ANNEXEDNONFAULTY.csv')