# -*- coding: utf-8 -*-


import requests
from urllib.parse import urlencode#构成完整的URL
from pyquery import PyQuery as pq

host = 'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' % host
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36'

headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/p/index?containerid=2304131878136331_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2302831878136331',
    'User-Agent': user_agent
}


# 按页数抓取数据
def get_single_page(page):
    params = {
        'type': 'uid',
        'value': 1665372775,
        'containerid': 2304131878136331,
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('抓取错误', e.args)


# 解析页面返回的json数据
def parse_page(json):
    items = json.get('data').get('cards')
    for item in items:
        item = item.get('mblog')
        if item:
            data = {
                pq(item.get("text")).text() # 仅提取内容中的文本
            }

            yield data#生成器

if __name__ == '__main__':
    for page in range(1, 10):  # 抓取前十页的数据
        json = get_single_page(page)
        results = parse_page(json)
        with open('get_content.txt', 'w') as f:
            for data in results:
                f.write(str(data))