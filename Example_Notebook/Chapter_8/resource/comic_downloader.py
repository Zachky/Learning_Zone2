import requests
import csv
import os
import threading

# =============================================================================
# 使用requests.get() 取得content
# =============================================================================
def downPic(url,file_name):  
    html = requests.get(url)    
    #以byte的形式將圖片數據寫入
    with open(file_name,'wb') as file:        
        file.write(html.content)
        file.flush()   
        #file.close()
    print(file_name+ ' 儲存完畢!')
    


with open('comic.csv',encoding='utf-8-sig') as f:
    reader=csv.reader(f)
    header=next(reader)   
    datas=list(reader)


folder_path ='comic_pic/'    
#判斷資料夾是否存在
if (not os.path.exists(folder_path)): 
    os.makedirs(folder_path) 


count=0
thread=[]
for data in datas[:2]:   
    for i in range(int(data[-1])):
        url=data[3]+str(i+1)+'.jpg'
        #print(url)
        t=threading.Thread(target=downPic,args=(url,folder_path+data[0]+str(i+1)+'.jpg'))
        t.start()
        thread.append(t)        
        count+=1      
        
        if count%5==0:           
            for t in thread:
                t.join()                
         
            thread=[]              
       
    
  
    for t in thread:
        t.join()
                
        
print('down!')
    