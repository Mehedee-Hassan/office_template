# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:06:35 2020

@author: mehedee
C:\Users\mehedee\Documents\Python Scripts\office\product_sale_count_prediction\DataPreProcessHelper.py

import sys
sys.path.append('./')

import src.main.util.utils
#or
from src.main.util.utils import json_converter 
"""


import sys
import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime as dtdt

sys.path.append('C:/Users/mehedee/Documents/Python Scripts/office/product_sale_count_prediction/')
sys.path.append('C:/Users/mehedee/Documents/Python Scripts/office/product_sale_count_prediction/')
import DataPreProcessHelper as DPPHelper



# ####### START PRE PROCESS ######## #
# #### READ FILE OF PRODUCT

datapath2 = 'C:\\Users\\mehedee\\Documents\\data\\office_projects\\product_count_prediction\\tenpo01\\poduct_sale\\' 
## == sale file data
datafile = 'sale_4968786112149.csv'
df_sale= pd.read_csv(datapath2+datafile,  parse_dates=[0])


##  == start and end date determination 
start_date=  str(df_sale.iloc[0]['date'].date())
end_date =  str(df_sale.iloc[len(df_sale)-1]['date'].date())


myDataProcessHelper = DPPHelper.DataPreProcessHelper(True)

len(df_sale)
df_sale2=df_sale.drop('money',axis=1)


df_sale2 = df_sale.set_index('date')



temp_sale_df = myDataProcessHelper.date_fillup(df_sale2,start_date=start_date,end_date=end_date,do_avg_flag=True,days_to_avg=7)
temp_sale_df_saved = temp_sale_df.copy()


   # def date_fillup(self,df_product_sale,start_date=-1,end_date=-1,do_avg_flag=True,days_to_avg=7,fillup_custom_data_flag=False,fillup_data = -100012349567890001,fill_value_field_name='count'):

temp_sale_df=temp_sale_df.drop('money',axis=1)


# make date features 
# ['count', 'weekday', 'year', 'month', 'day', 'quarter', 'dayofyear',
#       'weekofyear', 'weekofmonth', 'halfofmonth', 'salaryweek',
#       'lastdayofmonth', 'latdayofyear', 'weekstartday', 'weekendflag']

temp_sale_df = temp_sale_df.set_index('date')
new_temp_df=myDataProcessHelper.get_date_regression_feature_date_index(temp_sale_df)


# holiday fillup


# == read holiday data
holiday_datapath = 'C:/Users/mehedee/Documents/data/office_projects/'
holiday_filename = 'holidayjapan.csv'

df_holiday = pd.read_csv(holiday_datapath+holiday_filename,parse_dates=True)


"""
holiday file
           Date   weekday                      Name              Type
0      2016-1-1    Friday            New Year's Day  National holiday
1      2016-1-2  Saturday    January 2 Bank Holiday      Bank holiday
2      2016-1-3    Sunday    January 3 Bank Holiday      Bank holiday
3     2016-1-11    Monday         Coming of Age Day  National holiday
4     2016-2-11  Thursday   National Foundation Day  National holiday
"""

df_holiday['Date'] = pd.to_datetime (df_holiday['Date'])
df_holiday = df_holiday.set_index('Date')

df_holiday = df_holiday[df_holiday['Type'] == 'National holiday']
df_holiday = df_holiday.drop('weekday' ,axis=1)
df_holiday = df_holiday.drop('Name',axis=1)
df_holiday = df_holiday.drop('Type',axis=1)
df_holiday['holiday'] =[1]*len(df_holiday) 


new_temp_df2 = myDataProcessHelper.holiday_date_fillup(df_holiday,start_date = start_date,end_date=end_date)
new_temp_df2 = new_temp_df2.set_index('date')

# concat 


if len(new_temp_df2) != len(new_temp_df):
    print("ERROR # not equal length!")

if new_temp_df2.index[0] != new_temp_df.index[0] or new_temp_df2.index[len(new_temp_df2)-1] != new_temp_df.index[len(new_temp_df)-1] :
    print("ERROR # not equal date length!")


new_temp_df['holiday'] = new_temp_df2['holiday']

# spectial sale 
# == special sale data

special_sale_path = 'C:/Users/mehedee/Documents/data/office_projects/product_count_prediction/tenpo01/special_sale/'
path_special_sale = special_sale_path+'special_sale_data_4538151297025.csv'
special_sale_df = pd.read_csv(path_special_sale,date_parser=[0])


"""
    sale_start_date sale_end_date
0         2020/3/30     2020/3/30
1         2020/3/29     2020/3/29
2         2020/3/28     2020/3/28
3         2020/3/22     2020/3/22
4         2020/3/21     2020/3/21

"""

print(special_sale_df) # sale_start_date sale_end_date



special_sale_df=special_sale_df.sort_values(by=['sale_start_date'])
special_sale_df['sale_start_date']=pd.to_datetime(special_sale_df['sale_start_date'])

special_sale_df=special_sale_df.set_index('sale_start_date')
special_sale_df['special_sale'] =[1]*len(special_sale_df) 
special_sale_start_date = str(special_sale_df.index[0].date())
special_sale_end_date = str(special_sale_df.index[len(special_sale_df)-1].date())


temp_special_sale_df = myDataProcessHelper.special_sale_date_fillup(special_sale_df,start_date = start_date,end_date=end_date)


temp_special_sale_df = temp_special_sale_df.set_index('date')

if len(temp_special_sale_df) != len(new_temp_df):
    print("ERROR # not equal length!")

if temp_special_sale_df.index[0] != new_temp_df.index[0] or temp_special_sale_df.index[len(temp_special_sale_df)-1] != new_temp_df.index[len(new_temp_df)-1] :
    print("ERROR # not equal date length!")


new_temp_df['special_sale'] = temp_special_sale_df['special_sale']


# weather data 


"""
           date  temp0h  temp300h  ...  rain1500h  rain1800h  rain2100h
0    2016-01-01       7         6  ...        0.0        0.0        0.0
1    2016-01-02       8         8  ...        0.0        0.4        0.0
2    2016-01-03      14        15  ...        0.0        0.2        0.0
3    2016-01-04      14        13  ...        0.0        0.0        0.0
4    2016-01-05       8         8  ...        0.0        0.0        0.0
"""


# IMPORTANT# we have all weather data so we will set 
# weather data to our sale data

## == weather file read

weather_file_path = 'C:/Users/mehedee/Documents/data/weatherdata/miyazaki_shi/'
weather_file_name = 'weather_data_flat_16-20.csv'

df_weather =pd.read_csv(weather_file_path+weather_file_name, parse_dates=[0])


df_weathe_processed = myDataProcessHelper.fill_me_weather(df=temp_sale_df_saved,df_weather = df_weather)

try:
    df_weathe_processed = df_weathe_processed.drop('count',axis=1)
    df_weathe_processed = df_weathe_processed.drop('money',axis=1)
except:
    print('already deleted')



if len(df_weathe_processed) != len(new_temp_df):
    print("ERROR # not equal length!")

if df_weathe_processed.index[0] != new_temp_df.index[0] or df_weathe_processed.index[len(df_weathe_processed)-1] != new_temp_df.index[len(new_temp_df)-1] :
    print("ERROR # not equal date length!")


result = pd.concat([new_temp_df, df_weathe_processed.reindex(new_temp_df.index)], axis=1)


processed_sale_save_file_path = datapath2
processed_sale_save_file_name = 'featured_sale_4968786112149.csv' 


result.to_csv(processed_sale_save_file_path+processed_sale_save_file_name, encoding='utf-8')
# ####### END PRE PROCESS ######## #
