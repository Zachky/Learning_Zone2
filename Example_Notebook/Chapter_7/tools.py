# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def save_pic(url,filename):
    try:
        with open(f"{filename}.jpg".replace(":","_"),"wb") as f:    
            resp=requests.get(url)
            if resp.status_code==200:
                f.write(requests.get(url).content)
                print(f'{filename}.jpg 儲存成功!')
            else:
                print(resp.status_code,'儲存失敗.')
    except Exception as e:
        print(e,'儲存失敗')


def get_soup(url):     
    """
    url:爬蟲的連結
    return:回傳BeautifulSoup物件 or None
    """	
    user_agent={
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    soup=None 
    try:
        resp=requests.get(url,headers=user_agent)          
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'lxml')
        else:
            print('網頁取得失敗',resp.status_code)
    except Exception as e:
        print('網址不正確!',e)
        
    return soup


def get_chrome(url,path=r'C:\webdriver\chromedriver.exe'):
    chrome=None
    try:
        service=Service(path)
        chrome=webdriver.Chrome(service=service)
        chrome.get(url)        
    except Exception as e:
        print('錯誤',e)
        
    return chrome

def send_keys(element,key,delayTime=0.5):
    try:
        element.clear()
        time.sleep(delayTime)
        element.send_keys(key)
        time.sleep(delayTime)
        element.send_keys(Keys.ENTER)
        print(f'{key}輸入完成!')
    except Exception as e:
        print(e)


def find_element(chrome,xpath):
    element=None
    try:
        element=chrome.find_element(By.XPATH,xpath)        
    except Exception as e:
        print('錯誤',e)    
    return element


def scroll_windows(chrome,start,end,step,delayTime=0.2):    
    print('網頁捲動中...')
    try:
        for i in range(start,end,step):       
            chrome.execute_script(f"window.scrollTo({i},{i+step})")
            time.sleep(delayTime)
        print(f'捲動到{end}完成!')
    except Exception as e:
        print(e)

# 測試
if __name__=='__main__':
    url='https://www.yahoo.com.tw'
    print(get_soup.__doc__)








