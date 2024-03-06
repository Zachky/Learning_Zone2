import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as Chrome_Sev
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select 

def getSoup(url):
  '''
  Return html content with beautifulsoup format
  '''
  user_agent={
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

  try:
    resp=requests.get(url,headers=user_agent)
    resp.encoding='utf-8'
    if resp.status_code == 200:
      return BeautifulSoup(resp.text,'lxml')
    else:
      return 'Error: Status_code'+ str(resp.status_code)

  except Exception as e:
    return e

def ExportImage(Img_Url,Img_Name):
    strMsg = "Image Save Successfully!"
    try:

        #Create folder if necessary
        path='Output/Img_Library/'
        if not os.path.exists(path):os.makedirs(path)

        #Get Image Content (Binary string)
        Entity_Image = requests.get(Img_Url).content

        #Export Image
        with open(path+Img_Name+".jpg",'wb') as f:
            f.write(Entity_Image)

        return strMsg
    except Exception as e:
        
        strMsg = e
        
        return strMsg


def get_chrome(Url,DriverPath='C:\Web driver\Chrome\chromedriver.exe',hide=False):
    Test_Chrome = None
    options = WD.ChromeOptions()
    if hide:
      options.add_argument('--headless')
    try:
        ServiceChrome = Chrome_Sev(DriverPath)
        Test_Chrome = WD.Chrome(service=ServiceChrome,options=options)
        Test_Chrome.get(Url)
        
    except Exception as e:
        print('Error:',e)

    return Test_Chrome

def send_keys(element,key,delayTime=0.5):
   try:
      element.clear()
      time.sleep(delayTime)
      element.clear()
      time.sleep(delayTime)
      element.send_keys(Keys.ENTER)
      print(f'{key}輸入完成!')

   except Exception as e:
      print(e)

def find_elemental(chrome,xpath):
    element = None
    try:
      element=chrome.find_element(By.XPATH,xpath)
    except Exception as e:
       print('Error:', e)
    return element

def scroll_windows(chrome,start,end,step,delayTime=0.2):
    try:
        for i in range(start,end,step):
          chrome.execute_script(f"windows.scrollTo({i},{i+step})")
          time.sleep(delayTime)
        print(f'捲動到{end}完成!')
    except Exception as e:
       print(e)

# ------Test Area-------
if __name__ == '__name__':
  url="https://tw.yahoo.com"
  print(getSoup(url))

  ExportImage("http://www.atmovies.com.tw/photo101/fotw31435759/pl_fotw31435759_0002.jpg",'老狐狸 Old Fox')
  chrome = get_chrome('https://tw.yahoo.com',hide=True)
  print('chrome')
  chrome.quit()
  print('quit')




