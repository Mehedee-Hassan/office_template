# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:35:51 2020

@author: mehedee
"""

# IMPORTING NECESSARY

import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime as dtdt
import datetime as dt


# THIS CLASS IS TO HANDLE ALL THE DATA PREPROCESS FOR PREDICTION

class DataPreProcessHelper:
    global COUNTDEBUG     
    week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    
    __debug = False
    
    def __init__(self,DEBUG=False):
        COUNTDEBUG = 0
        print("##",COUNTDEBUG,' init()')
        self.__debug = DEBUG
    
    
    
    def avg(self,val,count):
        return val/count
    
    def n_days_avg(self,data,n_index,first,last,take_upto,fillup_data):
        previous_sum = 0
        # if not equal to -1
        after_sum = 0
        
    
        count_prev = 0
        count_after = 0
        prev_done_flag = False
        after_done_flag = False
        
        # take a big number # cahnge with the data size and if some day you need to change the size of average over 
        # 10000 ,
        tt = []
        for i in range(1,10000):
            
        #   print("only data",data.iloc[index-i])
            if n_index - i >= first:        
                
                if count_prev == take_upto:
                    prev_done_flag = True
                    
                else:
                    tempprev = data.iloc[n_index-i]['count']
                    if tempprev != fillup_data:
                        
                            
                #             print('prev',tempprev)
                        
                        if tempprev > 0:
                            previous_sum += tempprev
                            tt.append((tempprev,n_index-i))
                            
                            count_prev += 1
            else:
                prev_done_flag = True
                
                
                
            if n_index + i < last:        
                
                if count_after == take_upto:
                    after_done_flag = True
                    
                else:
                    tempafter = data.iloc[n_index+i]['count']
                #   print("now" ,tempafter)
                    
                    if tempafter != fillup_data:
                        
                    
                        if tempafter > 0:
                            after_sum += tempafter
                            tt.append((tempafter,n_index+i))
                            count_after += 1
                
            else:
                after_done_flag = True
            
            
            if prev_done_flag == True and after_done_flag == True :
                break
            
        print(tt)
        # if the after sum and previous sum is 0 handle here    
        if after_sum > 0 and previous_sum > 0:
            after_sum = after_sum / count_after
            previous_sum = previous_sum / count_prev
    
            return ((after_sum+previous_sum)/2)
        elif after_sum > 0:
            after_sum = after_sum / count_after
            return after_sum
        elif previous_sum > 0:
            previous_sum = previous_sum / count_prev
            return previous_sum
        return 0

#%%
    

    """
    @Description:
        a function to fill up missing date's data for particular field
    @params:
        @df_product_sale : the data frame to be processed
        @start_date: first date to start
        @end_date: process the upto the end date
        @do_avg_flag : True: if want ot average the past and future data to fill up the palce
        @days_to_avg : number of past and future day to average for filling up
        @fillup_custom_data_flag: True: will not fill up with anomalous data
        @fillup_data: custom data to fillup the empty spaces
        @fill_value_field_name: the field to fill up
    """
    
    def date_fillup(self,df_product_sale,start_date=-1,end_date=-1,do_avg_flag=True,days_to_avg=3,fillup_custom_data_flag=False,fillup_data = -100012349567890001,fill_value_field_name='count'):
        
        if self.__debug != False:
            print('DEBUG datefillup 1')     
        
        #IF start_date and end_date is not given ,take both from data frame        
        if start_date == -1:
            start_date = df_product_sale.iloc[0]['date']
                
        
        if end_date == -1:
            end_date = df_product_sale.iloc[len(df_product_sale)-1]['date']
            
        
        if self.__debug != False:
            print('DEBUG datefillup 2')            
        # anomalous data to fill the non existent value
        if fillup_custom_data_flag == False:
            fillup_data = -100012349567890001 # set up in parameter
    
        
        idx = pd.date_range(str(start_date), str(end_date))
        
        if self.__debug != False:
            print('DEBUG datefillup 3')    
        
        s = df_product_sale.copy()
        s.index = pd.DatetimeIndex(s.index)
        
     
        s = s.reindex(idx,fill_value=fillup_data)

        
        s = s.reset_index()
        s = s.rename(columns={'index': 'date'})
        
        
        firstpos = 0
        lastpos = len(s)
        
        # how much dates were null
        # IF: data is to fill with other data
        count = 0
        missingdates =[]
        print('change date entry =')

        if do_avg_flag == True:
            for index,row in s.iterrows():
          
                  if row[fill_value_field_name] ==fillup_data:
                    if do_avg_flag == True:
                        s.loc[index ,fill_value_field_name] = self.n_days_avg(s,index,firstpos,lastpos,days_to_avg,fillup_data)
                    missingdates.append(s.iloc[index])
                    count += 1
                    
        if self.__debug != False:
            print('DEBUG datefillup 4')    
                  
           
        
        return s            
        
        
        


#%%


       
    
    
    def getDayOfWeek(self,date):
        
        day=date.weekday()
        
        print(day)
        return self.week_days[day]
    
  
    
    # week of month 
    def get_week_of_month(self,date):
        return int(date.day / 7)
   
    
    # half of month
    def get_half_of_month(self,date):
        return int(date.day/15)
    
    
    # the salary week of month
    def get_salary_week(self,date):
        return int(date.day/23)
    

    # last day of year
    def get_is_end_of_year_day(self,date):
        tomorrow = date.date() + timedelta(days=1)
        
        if tomorrow.day == 1 and tomorrow.month == 1:
            return 1
        
        return 0
        
    
  
    
    # last day of month
    
    def get_is_end_of_month(self,date):
        tomorrow = date.date() + timedelta(days=1)
        
        if tomorrow.day == 1:
            return 1
        
        return 0
        
    
    # get week start day
    def get_week_startend_day(self,date):
        if date.weekday() == 4:
            return 1
        elif date.weekday() == 0:
            return 2
        return 0
    
 
    
    # week end day ,satday  = 1 ,sun_day =2
    def get_is_week_end(self,date):
        if date.weekday() == 6:
            return 2
        elif date.weekday() ==5:
            return 1
        
        return 0
    

      
    def get_list_dateprocessed(self,df):    
        
        # week of the month list
        week_of_months_list = []
        for date in df.index:
            week_of_months_list.append(self.get_week_of_month(date))
        
      
          
        # half of the month list
        
        half_of_months_list = []
        for date in df.index:
            half_of_months_list.append(self.get_half_of_month(date))
        
     
        
        # get salary week of the month
        
        salaryweek_of_months_list = []
        for date in df.index:
            salaryweek_of_months_list.append(self.get_salary_week(date))
        
     
    
        # end of month 
        
        lastday_of_months_list = []
        for date in df.index:
            lastday_of_months_list.append(self.get_is_end_of_month(date))
        
        
        # end of year
        
        lastday_of_year_list =[]
        for date in df.index:
            lastday_of_year_list.append(self.get_is_end_of_year_day(date))
        
    
        # week start flag list
           
        week_start_flag_list = []
        for date in df.index:
            week_start_flag_list.append(self.get_week_startend_day(date))
    
        weekend_flag_list = []
        
        for date in df.index:
            weekend_flag_list.append(self.get_is_week_end(date))
    
    
        
        return {'week_of_months_list':week_of_months_list
                ,'half_of_months_list':half_of_months_list
                ,'salaryweek_of_months_list':salaryweek_of_months_list
                ,'lastday_of_months_list':lastday_of_months_list
                ,'lastday_of_year_list':lastday_of_year_list
                , 'week_start_flag_list':week_start_flag_list
                ,'weekend_flag_list':weekend_flag_list
                }
        
        
    
    def get_date_regression_feature_date_index(self,df):
        
        date_features = self.get_list_dateprocessed(df.copy())
        # temp_df = pd.DataFrame([])
        temp_df = df.copy()
        temp_df["weekday"]=df.index.weekday
        temp_df["year"] = df.index.year
        temp_df["month"] = df.index.month
        temp_df["day"] = df.index.day
        temp_df['quarter'] =df.index.quarter
        temp_df['dayofyear'] = df.index.dayofyear
        temp_df['weekofyear'] = df.index.weekofyear
        temp_df['weekofmonth'] =date_features['week_of_months_list']
        temp_df['halfofmonth'] = date_features['half_of_months_list']
        temp_df['salaryweek'] = date_features['salaryweek_of_months_list']
        temp_df['lastdayofmonth'] = date_features['lastday_of_months_list']
        temp_df['latdayofyear'] = date_features['lastday_of_year_list']
        temp_df['weekstartday'] = date_features['week_start_flag_list']
        temp_df['weekendflag'] = date_features['weekend_flag_list']
        
        return temp_df
    
    
# %%
    
    # dateformat 'yyyy-mm-dd'
    def holiday_date_fillup(self,df,start_date=-1,end_date=-1):
        
        
        
        # temp_df = pd.DataFrame([])
        temp_df = df.copy()
        
        
        if start_date == -1:
            start_date = df.iloc[0]['date']
        else:
            start_date = str(dtdt.strptime(start_date,'%Y-%m-%d').date())
            
            
        if end_date == -1:
            end_date=df.iloc[len(temp_df)-1]['date']
        else:
            end_date = str(dtdt.strptime(end_date,'%Y-%m-%d').date())   
        
            
        temp_df = self.date_fillup(temp_df,start_date=start_date ,end_date=end_date
                    ,do_avg_flag=False
                    ,fillup_custom_data_flag=True
                    ,fillup_data = 0
                    ,fill_value_field_name='holiday')
        
        
        return temp_df
        
    
    
# %%    
    
    # special offer date fill up
    # dateformat 'yyyy-mm-dd'
    # @args expects date as index row 
    def special_sale_date_fillup(self,df,start_date=-1,end_date=-1,same_priority_offer=True):
        
        
        
        
        temp_df = df.copy()
        
        if same_priority_offer == True:
            temp_df['special_sale'] = [1]*len(temp_df)
        
        
        if start_date == -1:
            start_date = temp_df.iloc[0]['date']
        else:
            start_date = str(dtdt.strptime(start_date,'%Y-%m-%d').date())
            
            
        if end_date == -1:
            end_date=temp_df.iloc[len(temp_df)-1]['date']
        else:
            end_date = str(dtdt.strptime(end_date,'%Y-%m-%d').date())   
        
        
        # take only holidays I need
        temp_df=temp_df[temp_df.index >= start_date]
        temp_df=temp_df[temp_df.index <= end_date]
        
        temp_df = self.date_fillup(temp_df,start_date=start_date ,end_date=end_date
                    ,do_avg_flag=False
                    ,fillup_custom_data_flag=True
                    ,fillup_data = 0
                    ,fill_value_field_name='special_sale')
        
        
        return temp_df



    def fill_me_weather(self,df,df_weather):
        
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        c = 0
        last_index = 0
        totallen = len (df_weather)
        
        df_weather['date'] = pd.to_datetime(df_weather['date'])
        
        for index, row in df.iterrows():
            
        #     if c>10 : break;c+=1;print(index.date())
            
            for index2 in range(last_index,totallen):
                if index.date()==df_weather['date'][index2].date():
                    df.loc[index,'temp0h'] = df_weather.loc[index2 , 'temp0h']
                    df.loc[index,'temp300h'] = df_weather.loc[index2 , 'temp300h']
                    df.loc[index,'temp600h'] = df_weather.loc[index2 , 'temp600h']
                    df.loc[index,'temp900h'] = df_weather.loc[index2 , 'temp900h']
                    df.loc[index,'temp1200h'] = df_weather.loc[index2 , 'temp1200h']
                    df.loc[index,'temp1500h'] = df_weather.loc[index2 , 'temp1500h']
                    df.loc[index,'temp1800h'] = df_weather.loc[index2 , 'temp1800h']
                    df.loc[index,'temp2100h'] = df_weather.loc[index2 , 'temp2100h']
                    
                    # adding rain
                    df.loc[index,'rain0h'] = df_weather.loc[index2 , 'rain0h']
                    df.loc[index,'rain300h'] = df_weather.loc[index2 , 'rain300h']
                    df.loc[index,'rain600h'] = df_weather.loc[index2 , 'rain600h']
                    df.loc[index,'rain900h'] = df_weather.loc[index2 , 'rain900h']
                    df.loc[index,'rain1200h'] = df_weather.loc[index2 , 'rain1200h']
                    df.loc[index,'rain1500h'] = df_weather.loc[index2 , 'rain1500h']            
                    df.loc[index,'rain1800h'] = df_weather.loc[index2 , 'rain1800h']            
                    df.loc[index,'rain2100h'] = df_weather.loc[index2 , 'rain2100h']
        
                    
                    last_index = index2 
                    break
        
        return df



    def high_corr_to_consider(self,df,corr_val=0.1,corr_field_name = 'count',corr_method='pearson'):
        listofindex =dict(df.corr(corr_method)[corr_field_name])

        
        listofindexto_consider =[]
        for key,val in listofindex.items():
            print(key,val)
            
            if val > 0.1:
                listofindexto_consider.append(str(key))
        
        # why i did this line _!!!        
        listofindexto_consider = [i for a in listofindexto_consider ]
        
        
        
        return listofindexto_consider
    
    
    
    def mean_absolute_percentage_error(y_true, y_pred): 
        """Calculates MAPE given y_true and y_pred"""
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# %%

    
    def class_tester(self):
        print('DEBUG 1 :')
        print('DEBUG 2 :')
        print('DEBUG 3 :')
        
        print('DEBUG 4 :')
        print('DEBUG 5 :')
        print('DEBUG 6 :')
        
        # fill empty dataframe using [0]*len 
        temp_df = pd.DataFrame([])
        temp_df['date'] = [7,4,2,3,4,5,6,7,8,2]
        temp_df['holiday'] = [0]* len(temp_df)
        print(temp_df)
    
        # first and last item of a field of a dataframe
        temp_df.iloc[0]['date']
        temp_df.iloc[len(temp_df)-1]['date']
        
    