import requests
from bs4 import BeautifulSoup
from selenium import webdriver

 
def getSoup(url,post_data=None,headers=None):   
    '''
    取得soup物件
    ''' 
    soup=None
    try:
        if post_data!=None:
            resp=requests.post(url,data=post_data)
        elif headers!=None:
            resp=requests.get(url,headers=headers)
        else:
            resp=requests.get(url)
        
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'lxml')    
    except:
        print('取得soup物件失敗...')
    
    return soup

    
def getChrome(url,path=r'C:\webdriver\chromedriver',hide=False):
    '''
    取得網頁Chrome物件
    '''
    chrome=None   
    try:
        options=webdriver.ChromeOptions()  
        if hide:
            options.add_argument('--headless')

        chrome=webdriver.Chrome(path,options=options)
        chrome.implicitly_wait(10)
        chrome.get(url)          
    except:
        print('取得chrome物件失敗...')

    return chrome

def getSoupWithChrome(url,path='c:/webdriver/chromedriver',hide=False):  
    option=webdriver.ChromeOptions()     
    if hide:        
        option.add_argument('--headless') 

    try:
        chrome=webdriver.Chrome(path,options=option)
        chrome.implicitly_wait(10)
        chrome.get(url)        
    except:
        return 'get webdriver error.'
     
    soup=None
    if chrome!=None:
        soup=BeautifulSoup(chrome.page_source,'lxml')    
        chrome.quit()
    return soup  
    


if __name__ == "__main__":
    pass
    URL='https://www.yahoo.com.tw/'   
    print(getSoup(URL))
    #sendEmail('iiiplay001@gmail.com',"test1","test2");