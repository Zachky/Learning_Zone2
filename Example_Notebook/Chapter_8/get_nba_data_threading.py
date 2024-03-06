# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:55:17 2021

@author: Jerry
"""

from datetime import date,timedelta
from queue import Queue
import threading,requests,json,time
import pandas as pd



def get_nba_data(date,q,show=False):
    api_url='https://tw.global.nba.com/stats2/scores/daily.json'
    params_data={
        'countryCode': 'TW',
        'gameDate': date,
        'locale': 'zh_TW',
        'tz': '+8'
    }
    
    resp=requests.get(api_url,params=params_data)
    nba_data=json.loads(resp.text)
    
    try:    
   
        games=nba_data['payload']['date']['games']

        teams=['awayTeam','homeTeam']
        datas=[]
        for game in games:
            for team in teams:
                team_name=game[team]['profile']['name']
                if show:
                    print(date,team_name,game[team]['score']['q1Score'],game[team]['score']['q2Score'],\
                        game[team]['score']['q3Score'],game[team]['score']['q4Score'])
                    print('-----------------------------------')

                datas.append([date,team_name,game[team]['score']['q1Score'],game[team]['score']['q2Score'],\
                    game[team]['score']['q3Score'],game[team]['score']['q4Score']])        

        q.put(datas)
        
    except:
        print(f'{date} 無比賽.')
        


if __name__=='__main__':
    
  
    start=date(2017,1,1)
    end=date.today()
    
    start_date=start.srtftime('%Y-%m-%d')
    
    print(f'{start}~{end}')   
    
    q=Queue()
    datas=[]
    threads=[]
    max_threads=20
    count=0
    
    while start<=end:
        try:
            day=start.strftime('%Y-%m-%d')
            print(day)
            start+=timedelta(1)
            
            threads.append(threading.Thread(
                target=get_nba_data,
                args=(day,q)))     
            
            count+=1
            #判斷是否到達最大數量
            if count%max_threads==0:
                for thread in threads:
                    thread.start()  
    
                for thread in threads:
                    thread.join()   
                
                threads=[]
                time.sleep(1)            
            
        except Exception as e:
            print(e)
            
    for thread in threads:
        thread.start()  
    
    for thread in threads:
        thread.join()    
        
    # 取資料
    for i in range(q.qsize()):
        datas+=q.get()
        
    file_name=f'nba_data-{start_date}~{end}.csv'
    pd.DataFrame(datas,columns=['date','team','q1','q1','q3','q4']).to_csv(
        file_name,encoding='utf-8-sig')
    
    print(f'{file_name} save ok.')       