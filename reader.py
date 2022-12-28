import  csv
f=open('Python.csv','r')
########################################################################################################
#simple reading code#
red=csv.reader(f)
for row in red:
    for object in row:
        print(object)
############################################################################################################
#DELIMITER#
#red=csv.reader(f,delimiter='|')
#for row in red:
    #for object in row:
       # print(object)
#DICT READ#
#reader = csv.DictReader(f)
    
#for row in reader:
 #   print(row)
  #  for object in row['sensor1_x']:
   #     print(object)