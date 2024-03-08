# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:16:54 2021

@author: Jerry
"""

from datetime import datetime
import hashlib,requests,os,sqlite3,time,sched
import pandas as pd

md5_file='md5.txt'
db_file='ubike.db'

#檢查db是否存在
def create_db():
    sqlstr='''create table if not exists data(
        id	integer PRIMARY KEY AUTOINCREMENT,
        date text,
        sno integer,
        sna text,
        tot integer,
        sbi integer,
        bemp integer,
        act integer
    );'''
    
    if not os.path.exists(db_file):
        with sqlite3.connect('ubike.db') as connect:
            cursor=connect.cursor()
            cursor.execute(sqlstr)
            print('資料庫(表)建立完成.')
            

def get_md5(text):
    m=hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def write_md5(md5_code):
    with open(md5_file,'w') as f:
        f.write(md5_code)
        print('寫入md5.')

def convert_date(date):
    return '-'.join([date[:4],date[4:6],date[6:8]])+\
    " "+ ':'.join([date[8:10],date[10:12],date[12:]])
    

def is_md5_update(text):   
    old_md5=''
    if os.path.exists(md5_file):
        old_md5=open(md5_file).read()               
   
    new_md5=get_md5(text)    
    if new_md5==old_md5:
        print('資料重複')
        return False
     
    write_md5(new_md5)
    
    return True                 

def crawler_youbike_tosql(sec=None,s=None):    
    try:
        print(datetime.now())
        url='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/file'
          
        # 檢查資料不重複才寫入
        if is_md5_update(requests.get(url).text):            
            df=pd.read_csv(url)
            df['date']=df['mday'].astype(str).apply(convert_date)
            df1=df[['date','sno','sna','tot','sbi','bemp','act']]

            with sqlite3.connect('ubike.db') as connect:
                df1.to_sql('data', connect, if_exists='append', index=False) 

            print('資料庫寫入成功!')
            
    except Exception as e:
        print(e)        
        
    if sec:    
        s.enter(sec,0,crawler_youbike_tosql,argument=(sec,s))  
        
        
        
if __name__=='__main__':
    create_db()
    print(datetime.now(),'youbike資料擷取中.....')
    
    # s = sched.scheduler(time.time, time.sleep) 
    # #測試 60s
    # s.enter(0,0,crawler_youbike_tosql,argument=(60,s))   
    # s.run()