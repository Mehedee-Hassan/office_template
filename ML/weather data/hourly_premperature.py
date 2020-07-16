    # -*- coding: utf-8 -*-
    """
    Created on Tue Jun  9 14:15:06 2020
    
    @author: mehedee
    @description:
        this file will read all weather data from a perticular directory 
        and make a complete csv file 
    
    @purpose:
        collect all data from online url and save it to a directory as different 
        files for each moth weather data
        The purpose is to read those data and make a csv file for all weather data
    
    @Proceduere:
        1. read files frod dir
        2. make csv to
        
    
    """
    
    import json
    import pandas as pd
    
    
    class Config:
        
        _path="C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\read\\"
        _file = "weather_data_miazaki_2016-1.json"
        _writefile = 'C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\weater_data_miyazaki_shi_2016-1.csv'
        _csvFile = 'C:\\Users\\mehedee\\Documents\\data\\weatherdata\\miyazaki_shi\\weater_data_miyazaki_shi_2016-1.csv'
        _csvTitle = "date,hour,temperature,rainfall"
        
        def getConfig (self):
            return { "path" : self._path, "file" : self._file,"writefile" : self._writefile,'csv_title':self._csvTitle,'csv_file':self._csvFile }
        
        
    
    
    
    
    
    
    
    # =============================================================================
    #   read the json file 
    #  -> constructor 
    # =============================================================================
    
    class JsonReader:
        import json
        _jsonObject = ''
        _start = False
        _nowLine = ''
        _saveddate = ''
        __config = ''
        _file = ''
        _path = ''
        _writefile = ''
        _titleOfCsv = ''
        
        
        def __init__(self,jsonObject):
            _jsonObject = jsonObject
            self.__config = (Config()).getConfig()
            self._path = self.__config['path']
            self._file = self.__config['file']
            self._writefile = self.__config['writefile'] 
            self._titleOfCsv = self.__config["csv_title"]
        
        
        def writeFile(self ,path,writefile,text):
        # open the file in append mode as we will add line in each time
            toWriteToFile = open(path+writefile,'a+')
            toWriteToFile.write(text)
            toWriteToFile.close()
            
        
        
        def print_loop(self ,aList,key):
            
            pass
        
        def writelinetoCSV(self,nowLine):
            # write line to csv file
            print("now line ##= ",nowLine)
            
            self.writeFile('',
                           self._writefile,
                           nowLine)
            
            return
    
        def substringUpToLastComma(self,nowLine,upToTheLastOfCharX):
            
            length = len(nowLine)
            
            i = length-1
            lastIndex = -1
            
            while i > 0:
                
                if nowLine[i] == upToTheLastOfCharX:
                    lastIndex = i
                    break
                
                i-=1
                
            
            return lastIndex
            pass
    
        # this is the recursion funciton 
        # iterate every call
        
        def print_recursion(self,aList,key):
            
            if type(aList) == list:
               # print('list')
               for anElement in aList:
                    #print("list=",anElement)
                    self.print_recursion(anElement,key)
        
        
        
            elif type(aList) == dict:
                # print('dict')
        
                for akey,avalue in aList.items():
                    
                    # print("dict= ",akey,avalue)
                    # if key == 'hourly':
                    self.print_recursion(avalue, akey)
        
        
            else:
                if key == 'date':
                    
                    # delete old date and save first date
                    self._saveddate = aList
                    # write old lien as new line will begin
                    self._nowLine = self._nowLine[:-1]
                    
                    lastComma=self.substringUpToLastComma(self._nowLine,"\n")
                    
                    self.writelinetoCSV(self._nowLine[:lastComma]+'\n')
                    # set line to null as new line will start
                    self._nowLine = ''
                    self._nowLine += aList+","
                    
                    
                    # write to csv file
                    
                    
                    
                    # print("normal print = ",key," val = ",aList)
               
                elif key == 'tempC':
                     self._nowLine += aList+","
                     # print("normal print = ",key," val = ",aList)
                elif key == 'time':
                     self._nowLine += aList+","
                     # print ("normal time  = ", key , ' val = ',aList)
                elif key == 'precipMM':
                     self._nowLine += aList+"\n"+self._saveddate+","
                     # print('normal rainfall = ',key , 'val = ', aList)
                     
    
    
    
    
    
    # =============================================================================
    #   pre process csv file
    #   CONSTRUCTOR:
    #   -> no argument
    #   -> create config : path csv
    #   FEATURES:
    #   -> sort the data on date
    #   -> make data flat  
    # =============================================================================
    
    class CSVPreProcess:
        
        _path = ''
        _file = ''
        _writefile = '' 
        _titleOfCsv = ''
        _csv_file=''
        __config=''
                
        
        def __init__(self):
            self.__config = (Config()).getConfig()
            self._path = self.__config['path']
            self._file = self.__config['file']
            self._writefile = self.__config['writefile'] 
            self._titleOfCsv = self.__config["csv_title"]
            self._csv_file = self.__config['csv_file'] 
        
        def __readCsvForMe(self):
            data = pd.read_csv(self._csv_file)
            
            return data
        
        
        def __writeDftoCSVforMe(self,df):
            df.to_csv(self._csv_file)
        
        def sortBYDateAndHour(self):
            data = self.__readCsvForMe()
            df=pd.DataFrame(data)
            
            df.sort_values(["date",'hour'], axis = 0, ascending = True,inplace = True, na_position ='last') 
            
            self.__writeDftoCSVforMe(df)



    # =============================================================================
    # main funciton 
    # =============================================================================
    """
    @process:
        1. read all json file in a directory
        2. make a csv file for full data
    """
    def __main__():
        
    
        
        config = (Config()).getConfig()
        # see what's inside
        # print(config)
        path = config['path']
        file = config['file']
        writefile = config['writefile'] 
        titleOfCsv = config["csv_title"]
        
        print(path+writefile)
        
        toWriteToFile = open(writefile,'w+')
        toWriteToFile.write(titleOfCsv)
        toWriteToFile.close()
        
        import glob  
        tempPath = path+"*.json"
        allfilePathList = [x for x in glob.glob(tempPath)]
  
        for fileElement in allfilePathList:
            with open(fileElement) as f:
              data = json.load(f)
        
            json_reader = JsonReader(data) 
          
            
            for anElement in data['data']['weather']:
                # print (anElement)
                # anElement = json.load(anElement)
                json_reader.print_recursion(anElement, 'hourly')
                #print("this element",anElement)
        
        
        csvProcessor =  CSVPreProcess()
        csvProcessor.sortBYDateAndHour()
        
        
        
    __main__()
    
        
    # =============================================================================
    #     
    # key and there explanation
    # rain :precipMM
    # hourly : hourly list
    # tempC : temperature
    # 
    # =============================================================================
    
    
    
      
    
