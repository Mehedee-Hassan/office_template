# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:55:03 2020

@author: mehedee
"""

special_sale_product_list = ['49838893','45161261','4901111307544','4903050168286','4903050502974','4901033631307','4930726100219','4903050502967','4901033631307','4930726100349','4903050502974','4930726100349','45161261','4901033631307','4930726100318','4901005202313','49838893','4930726100318','4901033631307','4901577450754','49838893','4903050168286','4903050100781','0021000615506','4903050502967','4930726100349','4930726100233','0021000615506','49838893','49838893','4903050502967','4903050502967','0021000615506','4901033631307','4930726100219','49838893','4903050502967','4903050502974','4903050168286','4903050502950','4930726100318','4930726100318','49838893','4930726100349','4903050502950','4902388057019','4930726100219','4903050502967','4903308030327','4903050502950','4903050502950','4903050502950','49838893','4903050502967','0021000615506','4930726100318','4903050502967','0021000615506','4930726100233','4903050502950','0021000615506','4903050502967','4903050502974','4903050168286','4901001102648','4930726100233','4930726100349','4903050502967','4902201424035','4903050502967','4903050502967','4903050502974','4903050100781','4901033631307','4903050502950','4901033631307','4903050168279','4903050502974','4901111308176','4901033631307','4903050502950','4902388057057','4930726100318','45161261','4901033631307','0021000615506','4903050502967','4902388057033','49838893','4903050100781','4903050502950','4903050168279','4903050100781','0021000615506','4901111308916','4930726100219','4930726100233','4903050502974','4903050502950','4903050502950','4930726100233','4901577031137','4903308030310','4903050168279','4930726100233','4903050100781','4901033631307','4930726100233','4903050168279','4930726100349','49838893','0021000615506','4903050502974','4903050502950','4901001198870','4903050168279','4930726100219','8001200044209','4901001000333','4903050502950','0021000615506','4902201420785','4903050100781','45161261','4930726100318','0021000615506','4903050502967','4930726100349','4901033631307','4903050100781','4903050502950','4903050502974','4903050502950','4903050502950','4930726100219','4903050168286','4902087155122','4903050502950','4903050502967','4903050502967','4903050502967','0021000615506','4903050502950','49720761','4903050502974','4901005202306','49838893','4903050502950','4903080120261','4930726100219','4930726100219','4902388057026','4903050502967','4901033631307','4930726100349','4930726100233','4902388057040','4903050502967','4902110320664','4930726100318','45161261','4903050100286','4930726100349','4903050502967','4903050502950','49838893','4903050502967','4903050168279','4930726100318','4903050100781','4903050502950','49838893','4903050502974','4903050502950','4930726100349','0021000615506','4901033631307','4901033631307','4903050502974','4903050502967','4930726100349','4903050100781','4903050168279','4903050502950','4930726100349','4903050168279','4930726100318','4903050100781','4903050168279','4903050168286','4930726100318','4901033631307','4930726100233','4901033631307','4930726100318','49838893','49838893','49838893','4903050502974','4930726100219','4903050168279','4903050100781','0021000615506','4903050168286','4903050168286','4902201424509','4903050502974','4903050502967','0021000615506','4903050100781','4930726100233','4903050168279','4930726100318','4903050502950','4903050168279','49838893','4903050168286','4930726100219','4901001258703','4930726100349','0021000615506','49838893','4903050168279','4901001000364','4903050502950','4903050502967','4903050100286','4903050168279','4903050502967','4901033631307','4903050100781','4903050168286','4903050502974','49838893','4930726100233','4903050168279','49838893','4973918157363','4903050168286','4903050502974','4930726100233','4903050168286','4903050502974','4930726100318','4902201420761','4903050502967','4930726100233','4930726100219','4902720123211','4903050502974','4903050502967','4930726100349','4901001000388','4903050502967','4903050100286','4901033631307','4903050168286','4903050502950','4902201420778','4903050502950','4903050100781','4930726100233','4903050502974','4903308030235','4903050502950','4901001258697','4903050502967','4930726100349','4901001000531','0021000615506','4903050502950','4903050502967','4903050168279','49838893','0021000615506','45161261','4903050502950','4903050168286','4903050168286','0021000615506','0021000615506','4930726100219','4901033631307','4903050168279','4903050502967','4930726100219','4903050168279','0021000615506','4902380135975','4930726100219','4903050168286','4902087155665','4901001099733','4901033631307','0021000615506','4901033631307','4930726100318','4930726100233','4903050168286','4903050168279','4903050502950','4930726100219','49838893','4903050168286']



import sys
import os
import psycopg2
import math

from catboost import CatBoostRegressor


import pandas as pd

import sys
import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime as dtdt
import seaborn as sns
import xgboost as xgb
from xgboost import plot_importance, plot_tree
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import GridSearchCV
from scipy.stats import pearsonr
import pandas as pd

corr_list = []

product_id = '4901160041307'
shop_id = '013'


#


def get_TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY(product_id="",shop_id='',DEBUG=False):
    temppo_code = shop_id
    shouhin_code = product_id

    TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY = """
    WITH
        prodcut_id AS (VALUES ('{0}')),
        store_id AS (VALUES ('{1}'))

    select to_date(売上日,'YYYYMMDD') as 売上日 , 売上点数
        from 店舗売上単品日計_201112

    where 店舗コード=(table store_id)
    and 商品コード=(table prodcut_id)

    UNION ALL

    select to_date(売上日,'YYYYMMDD') as 売上日 , 売上点数
        from 店舗売上単品日計_200710_dtaka

    where 店舗コード=(table store_id)
    and 商品コード=(table prodcut_id)
    and 売上日 < (select 売上日 from 店舗売上単品日計_201112 where 店舗コード=(table store_id) and 商品コード=(table prodcut_id) order by 売上日 asc limit 1)


    order by 売上日 asc , 売上点数

    """.format(shouhin_code,temppo_code)

    if DEBUG == True:
            print ("DEBUG # product sale count from multiple table :",TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY)

    return TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY





# print(get_TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY(product_id="4901002148935",shop_id='013'))


# ### PRODUCT SELECT DB REQ





product_list =[]
DEBUG = True


def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues



def connectProductSale(product_list  = None,_path=None,shop_id = ''):
    mydataframe = pd.DataFrame()
    for product_id in product_list:
        conn = None
 

        try:
            if DEBUG ==True:
                print('Connecting to PostgreSql database...')


            conn = psycopg2.connect(host='172.16.3.28' ,dbname="920088", user="kenpin", password="kenpin")
            
            
            cur = conn.cursor()


            if DEBUG ==True:
                print('PostgreSQL database vestion:')


            cur.execute(get_TENPOURIAGE_TANPINNIKKEI_COMBINED_ALLDAY(product_id,shop_id))
            data = cur.fetchone()

            while data is not None:
                
                new_row = {'date':data[0],'count':data[1]}
                mydataframe = mydataframe.append(new_row, ignore_index=True)
                
                data = cur.fetchone()

            cur.close()


        except (Exception ,psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

                print('DB CLOSED')
                
        return mydataframe



def specialSale(pid,sid):
    
    SPECIAL_SALE_Q = """

    WITH
        prodcut_id AS (VALUES ('{0}')),
        store_id AS (VALUES ('{1}'))

    select  
           --ts.商品コード,
           to_date(tk.販売開始日,'YYYYMMDD') as 販売開始日,
           to_date(tk.販売終了日,'YYYYMMDD') as 販売終了日

            --,abs(DATE_PART('day', to_date(tk.納品終了日,'YYYYMMDD')::timestamp - to_date(tk.納品開始日,'YYYYMMDD')::timestamp)) as days
           from 特売商品 ts,特売企画 tk
           where ts.店舗コード = (table store_id)
           and ts.商品コード in (select 商品コード	from 発注勧告商品補助	where 店舗コード = (table store_id) and 削除フラグ='0'	and 自動発注区分='2' )
           and ts.店舗コード = tk.店舗コード
           and ts.特売企画コード = tk.特売企画コード
           and tk.削除フラグ='0'
           and tk.ＥＯＳ区分='1'
           and ts.削除フラグ='0'
           and ts.停止フラグ='0'

           and 
	       abs(DATE_PART('day', to_date(tk.販売終了日,'YYYYMMDD')::timestamp - to_date(tk.販売開始日,'YYYYMMDD')::timestamp))<=7           and 
            (tk.特売種別<>'1' and tk.特売種別<>'2')


           and 商品コード in ((table prodcut_id))
           order by  ts.商品コード,tk.販売開始日

    """.format(pid,sid)

    return SPECIAL_SALE_Q

def connectSpecialSale(product_list  = None,_path=None,shop_id = ''):
    mydataframe = pd.DataFrame()
    for product_id in product_list:
        conn = None
 

        try:
            if DEBUG ==True:
                print('Connecting to PostgreSql database...')
            conn = psycopg2.connect(host='172.16.3.28' ,dbname="920088", user="kenpin", password="kenpin")
            
            
            cur = conn.cursor()


            if DEBUG ==True:
                print('PostgreSQL database vestion:')


            cur.execute(specialSale(pid=product_id,sid=shop_id))
            data = cur.fetchone()

            while data is not None:
                
                new_row = {'datestart':data[0],'dateend':data[1]}
                mydataframe = mydataframe.append(new_row, ignore_index=True)
                
                data = cur.fetchone()

            cur.close()


        except (Exception ,psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

                print('DB CLOSED')
                
        return mydataframe


def maxsalecount(pid,sid):

    maxcount = """
    WITH
        prodcut_id AS (VALUES ('{0}')),
        store_id AS (VALUES ('{1}'))

    select max(t1) from
    (select max(売上点数) as t1
        from 店舗売上単品日計_201112

    where 店舗コード=(table store_id)
    and 商品コード=(table prodcut_id)

    UNION ALL

    select max( 売上点数) as t1
        from 店舗売上単品日計_200710_dtaka
	
    where 店舗コード=(table store_id)
    and 商品コード=(table prodcut_id)
    and 売上日 < (select 売上日 from 店舗売上単品日計_201112 where 店舗コード=(table store_id) and 商品コード=(table prodcut_id) order by 売上日 asc limit 1)
	) t
    limit 1
    """.format(pid,sid)

    try:
        if DEBUG ==True:
            print('Connecting to PostgreSql database...')
        conn = psycopg2.connect(host='172.16.3.28' ,dbname="920088", user="kenpin", password="kenpin")


        cur = conn.cursor()


        if DEBUG ==True:
            print('PostgreSQL database vestion:')


        cur.execute(maxcount)
        data = cur.fetchone()

        while data is not None:

            new_row = data[0]
            

            data = cur.fetchone()

        cur.close()


    except (Exception ,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

            print('DB CLOSED')
    return new_row




for pid in special_sale_product_list:
    try:
        dd = connectProductSale(product_list  = [pid],_path=None,shop_id = shop_id)
        df = dd.copy()
        dd = dd.set_index('date')
        df [ 'date'] =pd.to_datetime(df['date'])


        df2 = df[df['date'] >='2017-05-01']
        df2=df2[df2['date']<='2020-08-01']






        product_list =[]
        DEBUG = True







        dd2 = connectSpecialSale(product_list  = [pid],_path=None,shop_id = shop_id)




        special_datelist = set()
        for index,row in dd2.iterrows():

            #print(row['datestart'],row['dateend'])
            datelist = pd.date_range(start=row['datestart'], end=row['dateend'])


            for a in datelist:
                special_datelist.add(str(a.date()))






        # special_datelist


        # ### MAXIMUM SALE COUNT AS TOP OF SPECIAL SALE






        m = maxsalecount(pid  = pid,sid = shop_id)








        datelist = pd.date_range(start='2017/5/1', end='2020/9/1')

        dataarray = []


        for a in datelist:
            if str(a.date()) in special_datelist:
        #         print(1)
                dataarray.append({'date': str(a.date()), 'spflag': int(m/2)})
            else:

                dataarray.append({'date': str(a.date()), 'spflag': 0})


        # print(dataarray)


        df_sp = pd.DataFrame(dataarray)




        df_sp['date'] = pd.to_datetime(df_sp['date'])

        tograph = pd.merge(df_sp,df2,how='left',left_on=['date'],right_on=['date'])

        tograph['count'] =tograph['count'].fillna(0)

        start_date_special_sale = df_sp[df_sp['spflag']>0]

        tograph = tograph[tograph['date']>=str(start_date_special_sale.iloc[0].date.date())]



        tograph['spflag']=np.array(tograph['spflag'].tolist()).astype(int)
        tograph['count']=np.array(tograph['count'].tolist()).astype(int)


        print('CORR---##',pid)
        corrarray = tograph.corr()
        print(corrarray)
        corr_list.append({'id':pid,'rel':corrarray['count'][0],'pval':calculate_pvalues(tograph)['count'][0]})
        print(corr_list)
    except Exception as e:
        print("ERROR#",e)

print(corr_list)


# ### PREPARE FOR GRAPH



"""x = tograph['date']
y= tograph['spflag']
y2 = tograph['count']



plt.figure()

plt.plot(x, y)
plt.plot(x, y2)
plt.title('linear')
plt.grid(True)


"""




