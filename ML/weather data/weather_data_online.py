# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:54:31 2020

@author: mehedee

read write online weather api data data 
curret api 
location : miyazaki -shi
time-period : 01-01-2016_01-06-2020

"""
# code for 11 months data

 
import json
import requests
i = 1
year = str(2020)



for month in range(1,6):
    URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=45a3a083c67f44beb2243215200506 &q=Miyazaki&format=json&extra=isDayTime&date=01/'+str(month)+'/'+year+'&enddate=01/'+str(month+1)+'/'+year+'&includelocation=yes'
    response = requests.get(URL) 
    # print(response.json())
    
    filename = 'weather_data_miazaki_'+year+'-'+str(month)+'.json'
    
    with open(filename, 'w') as json_file:
        json.dump(response.json(), json_file)


# code for only 12 month
import json
import requests
i = 1
year = str(2020)



#for month in range(1,6):
codepath = 'C:/Users/mehedee/Documents/Python Scripts/office/product_sale_count_prediction/dataprocess/'
month = 6
URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=45a3a083c67f44beb2243215200506 &q=Miyazaki&format=json&extra=isDayTime&date=01/'+str(month)+'/'+year+'&enddate=30/'+str(month)+'/'+year+'&includelocation=yes'
response = requests.get(URL) 
# print(response.json())

filename = 'weather_data_miazaki_'+year+'-'+str(month)+'.json'

with open(codepath+filename, 'w') as json_file:
    json.dump(response.json(), json_file)




# WEATHER DATA OF YEARS

URL_FULL_DATA = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=45a3a083c67f44beb2243215200506 &q=Miyazaki&format=json&extra=isDayTime&date=01/01/2016&enddate=16/07/2020&includelocation=yes'
URL_FULL_NEW = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=45a3a083c67f44beb2243215200506&q=31.9077&format=json&date=2016-01-01&enddate=2020-07-17&includelocation=yes'

try:
    
    response = requests.get(URL_FULL_NEW) 
    weatherfile =open('C:/Users/mehedee/Documents/Python Scripts/office/product_sale_count_prediction/dataprocess/weather_data_miazaki-shi_01-01-16_01-07-2020.json',mode="w",encoding="utf-8")
    weatherfile.write(str(response.json()))
        
    
except:
    print('file doesn\'t exists')
finally:
    print('file opend')
    weatherfile.close()
