import csv 
import time
import random 
import matplotlib.pyplot as plt  

num=[]
while(1):

    f=open('Python.csv', 'w')     
    fieldnames = ['sensor1_x', 'sensor1_y', 'sensor2_x','sensor2_y']    
    writer = csv.DictWriter(f, fieldnames=fieldnames)    
    writer.writeheader()    
    for i in range(10000):
     writer.writerow({'sensor1_x': random.gauss(100,15), 'sensor1_y': random.gauss(200,15), 'sensor2_x': random.gauss(300,15), 'sensor2_y':random.gauss(400,15)})    
    f.close()
    fr=open('Python.csv', 'r')     
    reader = csv.DictReader(fr)
    for row in reader:
        for object in row['sensor1_x']:
         num.append(object)   
    f.close()
    time.sleep(1)
    print(num)
    plt.hist(num) 
    plt.show()
print("Writing complete")    
#understand threading and wait time methods#
