import requests
import os
from bs4 import BeautifulSoup

def getSoup(url):
  '''
  Return html content with beautifulsoup format
  '''
  try:
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code == 200:
      return BeautifulSoup(resp.text,'lxml')
    else:
      return 'Error:Status_code'+ str(resp.status_code)

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

#------Test Area-------
if __name__ == '__name__':
  url="https://tw.yahoo.com"
  print(getSoup(url))

  ExportImage("http://www.atmovies.com.tw/photo101/fotw31435759/pl_fotw31435759_0002.jpg",'老狐狸 Old Fox')

