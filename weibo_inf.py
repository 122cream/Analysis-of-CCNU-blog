# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import requests
from lxml import etree
import random 
import time

header={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
       'cookie':'SUB=_2A25NvjMTDeRhGeNO7FAQ9SbIwj2IHXVvQV1brDV6PUJbktAKLXaskW1NTs89MEkIFcVqCXUDxa6RAsUrlG8NmDGt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFxKpHfIX3cQk-SdSKYu5lP5NHD95QfehMEeK-RSh.pWs4Dqcj1BNiLqgXLxKnL1K5LBo2t; _T_WM=66069018839; MLOGIN=1; XSRF-TOKEN=d8aba9; M_WEIBOCN_PARAMS=oid%3D4641795294105601%26lfid%3D100103type%253D1%2526q%253D%25E5%258D%258E%25E4%25B8%25AD%25E5%25B8%2588%25E8%258C%2583%25E5%25A4%25A7%25E5%25AD%25A6%26luicode%3D20000174',
       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
       }
url_new='https://weibo.cn/u/'
data=[]
count=0  
def  get_id(path):
	with open(path,'r') as f:
		user_list=f.readlines()
		user_id=np.char.rstrip(user_list,'\n')
		return user_id
    
def gethtml(url,header):
    r=requests.get(url,headers=header)
    if r.status_code==200:
        return r.text
    else:
        print('网络连接异常')
for user_id in get_id('user_id.txt'):
    try:
        url=url_new+user_id
        r_text=gethtml(url,header)
        html=etree.HTML(r_text.encode('utf-8'))
        user_name=html.xpath('//span[@class="ctt"]/text()')[0]
        inf=html.xpath('//span[@class="ctt"]/text()')[1]
        
        data.append([user_name,inf])
        count+=1
        print('第{}个用户信息写入完毕'.format(count))
        time.sleep(random.randint(1,2))
    except:
        print('用户信息不完全')
df=pd.DataFrame(data,columns=['user_id','inf'])
df.to_csv('weibo_user.csv',index=False,encoding='gb18030')
