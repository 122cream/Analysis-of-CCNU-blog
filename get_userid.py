# -*- coding: utf-8 -*-

import requests
import random
import re
#import json



def get_userid(url):#用户代理
    header_list = [
        "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
        "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
        "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
        "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
        "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
    ]
    header = {
        'user-agent': random.choice(header_list)
    }

    with open('c:/Users/86153/Desktop/user_id.txt', 'w') as f:
        for page in range(1,251):
            try:
                print(url)
                r = requests.get(url, headers=header)#获取页面信息
                all_user = r.json()['data']['cards'][0]['card_group']#获取页面的json数据
                print(all_user)
                since_id = r.json()['data']['cardlistInfo']['since_id']
                for user in all_user:
                        f.write(str(user.get('user')['id'])+'\n')
                url = re.sub('since_id=(.*)', 'since_id='+str(since_id), url)#翻页
                
            except Exception as e:
                print(e)


if __name__ == '__main__':
    start_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_1878136331&luicode=10000011&lfid=1076031878136331&since_id=21'
    get_userid(start_url)
    
'''测试是否获取'''    
'''
url='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_1878136331&luicode=10000011&lfid=1076031878136331&since_id=21'
r = requests.get(url).text
r1 = json.loads(r)
all_user = r.json()['data']['cards']

#print(a1)'''