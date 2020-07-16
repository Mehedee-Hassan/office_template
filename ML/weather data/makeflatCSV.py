"""
Created on Tue Jun  9 14:15:06 2020

    @author: mehedee
    @Description : 
        
    Make file to read csv and make a flat csv file to 
    input in the algorihm as feature
    the only weather features are given here

"""

import json
import pandas as pd


class Config:

    _path="C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\"
    _file = 'C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\weater_data_miyazaki_shi_2016-1to2020-7.csv'
    _flatFileName =  'weather_data_flat_16-1to-20-7.csv'
    _csvTitle = "date,hour,temperature,rainfall"
    
    attribute_flat_file_name = 'flat_file_name'
    attribute_csv_title = 'csv_title'
    attribute_file = 'file'
    attribute_path = 'path'
    
    
    def getConfig (self):
        return { "path":self._path,"file" : self._file,'csv_title':self._csvTitle,'flat_file_name':self._flatFileName}
    
class Fields:
    
    """
        Purpose: Fields of the csv file
                        
        
    """
    
    date = 'date'
    hour = 'hour'
    temperature = 'temperature'
    rainfall = 'rainfall'
    _title = 'date,temp0h,temp300h,temp600h,temp900h,temp1200h,temp1500h,temp1800h,temp2100h,rain0h,rain300h,rain600h,rain900h,rain1200h,rain1500h,rain1800h,rain2100h'
    _key_list = ["date","temp0h","temp300h"
                 ,"temp600h","temp900h","temp1200h"
                 ,"temp1500h","temp1800h","temp2100h"
                 ,"rain0h","rain300h","rain600h"
                 ,"rain900h","rain1200h","rain1500h"
                 ,"rain1800h","rain2100h"]
    #"date,hour,temperature,rainfall"

    def getKeyList(self):
        return self._key_list
    
    def getTitle(self):
        return self._title
    
    def getDocumentation(self):
        return 'This class is to define the fields of csv file. _key_list: each field of the new csv file;_title: fields name in string'


def addToTempList(tempList
                  ,index1=-1,index1Val=-1
                  ,index2=-1,index2val=-1
                  ,index3=-1,index3val=-1
                  ,closeblock=[-1,-1,-1]):
    
    if closeblock[0] == -1: #can add to block 1,index1
        
        tempList[index1] = index1Val                                       # added date field 1 time
       
    if closeblock[1] == -1:                                                #can add to block 2,index2
        tempList[index2] = index2val                                       # added temperatures 1 time
      
    if closeblock[2] == -1:                                                #can add to block 3,index3
        tempList[index3] = index3val                                       # added rainfall  1 time
      
        
    
    
    return tempList


def writeToFlatFile(tempList,tempStringToWrite,flat_file_writer):
    l = len(tempList)
    tempStringToWrite = ''
   
    for element in range(0,l):
        if element != l-1:
            tempStringToWrite += str(tempList[element])+","
        else:
            tempStringToWrite += str(tempList[element])+"\n"

    flat_file_writer.write(tempStringToWrite)


def __main__():
    # get all configurations
    _configInstance =Config() 
    config = _configInstance.getConfig()
    fields = Fields()
    
    data = df = None
    flat_file_writer = None
    
    
    # read csv files
    
    try:
        data= pd.read_csv(config['file'])
        df = pd.DataFrame(data)
    except:
        print("#DEBUG 0.1: cannot open csv file")
        
    
    print("#DEBUG 0.12 : is config ok :",config[_configInstance.attribute_path],config[_configInstance.attribute_flat_file_name])
    # file to write 
    try:
        flat_file_writer = open(config[_configInstance.attribute_path]+config[_configInstance.attribute_flat_file_name],'w+')
        flat_file_writer.write(fields._title+"\n")
    except:
        print('#ERROR -1 : file open problem')
    
    
    
    #get key list of new csv file
    key_list = fields.getKeyList()
    
    # TODO check if list not woring 
    tempDictionary = {   str(key_list[0]):'',str(key_list[1]):'',str(key_list[2]):'',str(key_list[3]):''
                  ,str(key_list[4]):'',str(key_list[5]):'',str(key_list[6]):'',str(key_list[7]):''
                  ,str(key_list[8]):'',str(key_list[9]):'',str(key_list[10]):'',str(key_list[11]):''
                  ,str(key_list[12]):'',str(key_list[13]):'',str(key_list[14]):'',str(key_list[15]):'',
                  str(key_list[16]):''}
    
    tempList = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    
    firstTimeDateAdded = False
    isFirst= False
    temperatureIndex = 1 # temperature per hour index start at 2
    rainfallIndex = 9   # rainfallIndex per hour index starts at 9
    
    newRowList = []
    newRowList.append(key_list)
    
    
    
    for index,row in df.iterrows():
        
        print("DEBUG -1: index ",index,df.iloc[index][fields.date])
        
        
        if isFirst == True:
            if df.iloc[index-1][fields.date] == row[fields.date]:
                print("DEBUG 0: index ",index-1,df.iloc[index-1][fields.date])
                # if this date is same to the previous
                # create the new data list for appending in a row
                
                
                
                
                if firstTimeDateAdded == False:                                         # if date already added as we group by date 
                    
                    addToTempList(tempList
                                  ,index1=0
                                  ,index1Val=row[fields.date]
                                  ,index2=temperatureIndex 
                                  ,index2val=row[fields.temperature]
                                  ,index3=rainfallIndex
                                  ,index3val=row[fields.rainfall])
                    
                    print("DEBUG 1: index ",rainfallIndex,temperatureIndex)
                    
                    firstTimeDateAdded = True                                           # yes date added this time  
                
                else:
                    print("DEBUG 2: index ",rainfallIndex,temperatureIndex)
                    addToTempList(tempList,index2=temperatureIndex,index2val=row[fields.temperature],index3=rainfallIndex,index3val=row[fields.rainfall],closeblock=[0,-1,-1])                                 # don't add the date : first block closed
                    
                
                temperatureIndex +=1                                                    # increment every time up to 6 times to set 6 rows in 6 fields 
                rainfallIndex+=1                                                        #                        "
                
                
            else:
                writeToFlatFile(tempList,'',flat_file_writer)
                newRowList.append(tempList)
                
                tempList =[]
                firstTimeDateAdded = False
                
                #empty array fro the field to fill up
                tempList = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
                temperatureIndex = 1                                                    # temperature per hour index start at 2, starting at 0 index
                rainfallIndex = 9                                                       # rainfallIndex per hour index starts at 10,starting at  0 index
                
                addToTempList(tempList,index1=0,index1Val=row[fields.date],index2=temperatureIndex,index2val=row[fields.temperature],index3=rainfallIndex,index3val=row[fields.rainfall])
                print("DEBUG 3: index ",rainfallIndex,temperatureIndex)
                
                temperatureIndex +=1                                                    # increment every time up to 6 times to set 6 rows in 6 fields 
                rainfallIndex+=1                                                      #                        "
                
                
            
            # list of flat fields created here 
            print('#DEBUG 4:=',tempList)
            
            

                
        else:
            # first time adding the date 
            # and adding the temperature ,rainfall
            
            tempList[0] = row[fields.date]                                              # added date field 1 time
            tempList[temperatureIndex] = row[fields.temperature]                        # added temperatures 1 time
            tempList[rainfallIndex] = row[fields.rainfall]                              # added rainfall  1 time
            
            temperatureIndex +=1                                                        # increment every time up to 6 times to set 6 rows in 6 fields 
            rainfallIndex +=1
            
            isFirst = True 
        
        
        
    try:
        flat_file_writer.close()
    
    except:
        print("#DEBUG 5: file closing problem.Cannot close the file")

        


    
    
if __name__ == "__main__":
    __main__()
    




# =============================================================================
#  working psudocode
#  1. read normalized data 
#      i. indented for each date
#      ii. 6 for each date
#  2. for each date group data
#  3. make new fields 
#  4. set indented data to new fields
#  
# =============================================================================

# =============================================================================
# 
# config = (Config()).getConfig()
# data = pd.read_csv(config['file'])
# df = pd.DataFrame(data)
#                 
# df.sort_values(["date",'hour'], axis = 0, ascending = True,inplace = True, na_position ='last') 
# 
# 
# =============================================================================


# make flat


"""
@ INPUT file format (.csv):
 

   
            date	hour	temperature	rainfall
        0	2016/1/1	0	7	0
        1	2016/1/1	300	6	0
        2	2016/1/1	600	6	0
        3	2016/1/1	900	8	0
        4	2016/1/1	1200	12	0
        5	2016/1/1	1500	13	0
        6	2016/1/1	1800	10	0
        7	2016/1/1	2100	9	0
        8	2016/1/2	0	8	0
        9	2016/1/2	300	8	0
        10	2016/1/2	600	9	0
        11	2016/1/2	900	11	0
        12	2016/1/2	1200	15	0
        13	2016/1/2	1500	17	0
        14	2016/1/2	1800	15	0.4
        15	2016/1/2	2100	14	0


@ OUTPUT (.csv):
       
date,temp0h,temp300h,temp600h,temp900h,temp1200h,temp1500h,temp1800h,temp2100h,rain0h,rain300h,rain600h,rain900h,rain1200h,rain1500h,rain1800h,rain2100h
2016-01-01, 7, 6, 6, 8,12,13,10,9,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
2016-01-02, 8, 8, 9, 11,15,17,15,14,0.0,0.0,0.0,0.0,0.0,0.0,0.4,0.0
    
"""