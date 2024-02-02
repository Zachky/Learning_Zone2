# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:02:30 2022

@author: USER
"""

import requests,os
from bs4 import BeautifulSoup
from datetime import datetime


def make_dirs(path):
    '''
    建立目錄
    path:目錄路徑
    return True or False
    '''
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return True
    except Exception as e:
        print('目錄路徑錯誤!',e)
        
    return False

def save_pic(url,file_name='temp.jpg'):
    try:
        resp=requests.get(url)        
        if resp.status_code==200:
            with open(file_name,'wb') as f:
                f.write(resp.content)
            print(f'{file_name} 儲存完畢')
       
    except Exception as e:
        print('圖片路徑錯誤!',e)  
		

def get_date2(hms=False):    
    now=datetime.now().strftime('%Y/%m/%d %H:%M:%S') if hms else\
    datetime.now().strftime('%Y/%m/%d')
    
    return now

def get_date(hms=False):    
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S') if hms else\
    datetime.now().strftime('%Y-%m-%d')
    
    return now

def get_soup(url,post_data=None):    
    try:
        if post_data is not None:
            resp=requests.post(url,post_data)
        else:
            resp=requests.get(url)
        resp.encoding='utf-8'
        print(resp.status_code)
        if resp.status_code==200:
            # 取得soup物件
            soup=BeautifulSoup(resp.text,'lxml')
            return soup
        else:
            print('取得網頁失敗',resp.status_code)            
    except Exception as e:
        print(e)
    # 失敗則回傳None
    return None


if __name__=='__main__':
    print('test!')
    url='https://www.yahoo.com.tw'
    print(get_date(hms=False))
    #soup=get_soup(url)
    #print(soup)
    
    if make_dirs('c:\temp\test'):
        print('建立成功!')
    else:
        print('建立失敗!')
