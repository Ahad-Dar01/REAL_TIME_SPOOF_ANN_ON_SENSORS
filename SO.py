import datetime
import time
from suds.client import Client
dateStart = datetime.datetime.now() 
client = Client('http://127.0.0.1:8080/ScadaBR/services/API?wsdl')

#print ('######################################')
#print ('describing the service:')
#print (client)
#print ('######################################')
#types are created as follows:
#browseTagsOptions = client.factory.create('ns3:BrowseTagsOptions')
#note the type 
#print ('BronseTagsOptions')
#print (browseTagsOptions)
#set BrowseTagsParams
#browseTagsOptions.maxReturn = 2
#itemsPath = 'type'
#calling browseTags(xs:string itemsPath, ns3:BrowseTagsOptions options, )
#BrowseTagsResponse = client.service.browseTags(itemsPath,browseTagsOptions)
#rint ('browse tag counterProduct')
#print (BrowseTagsResponse)
#all tags
#print ('ALL TAGS')
#print (client.service.browseTags())
#print ('######################################')
############### FOR READING THE DATA SOURCE ######################
################################################################
def read_thread(x):
  while(1):
    itemPathList = ['Sensor1x','Sensor1y']
    #'Sensor2x','Sensor2y']
    readDataOptions = client.factory.create('ns3:ReadDataOptions')
    readDataOptions.maxReturn = 5
    readDataResponse = client.service.readData(itemPathList , readDataOptions )
    a=readDataResponse.itemsList[0]["value"]
    b=readDataResponse.itemsList[1]["value"]
    #c=readDataResponse.itemsList[2]["value"]
    #d=readDataResponse.itemsList[3]["value"]
    return {'s11':a,'s12':b}
    #'s21':c,'s22':d}
  ########################################################################### 
  #####################  Write DATA  ######################################
##############################################################################
def write_thread(s):
 while(1):
    writeDataOptions = client.factory.create('ns3:WriteDataOptions')
    writeDataOptions.returnItemValues = True
    itemStringList= client.factory.create('ns5:ItemStringValue')
    dataType = client.factory.create('ns2:DataType')
    quality = client.factory.create('ns2:QualityCode')
    itemStringList.itemName = 'Write'
    itemStringList.dataType = dataType.FLOAT
    itemStringList.value = s
    itemStringList.quality =quality.GOOD
    itemStringList.timestamp = datetime.datetime.now()
    writeStringDataResponse=client.service.writeStringData(itemStringList,writeDataOptions )
    print ('writing on the tag counterProduct')
    print  (writeStringDataResponse)
    print ('######################################')
    time.sleep(1)
