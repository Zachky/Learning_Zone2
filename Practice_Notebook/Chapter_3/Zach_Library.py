import requests
from bs4 import BeautifulSoup

def getSoup(url):
  try:
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code == 200:
      return BeautifulSoup(resp.text,'lxml')
    else:
      return 'Error:Status_code'+ str(resp.status_code)

  except Exception as e:
    return e
  
#------Test Area-------
if __name__ == '__name__':
  url="https://tw.yahoo.com"
  print(getSoup(url))

