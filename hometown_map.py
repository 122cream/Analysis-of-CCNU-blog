# -*- coding: utf-8 -*-

from pyecharts.charts import Map
from pyecharts import options as opts
import numpy as np
import pandas as pd

df=pd.read_csv('weibo_inf.csv',encoding='gbk')#读取数据
hometown=pd.DataFrame(df['hometown'].value_counts())#统计数据放入表

city=np.char.rstrip(list(hometown.index))#去除空白

map=Map(init_opts=opts.InitOpts(width="1200px",height="800px"))#设置画布大小
map.set_global_opts(
    title_opts=opts.TitleOpts(title="#华小诗粉丝地区分布#"),
    visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, #是否分段显示
    pieces=[
    {"max": 200, "min": 124, "label": ">123", "color": "#53868B"},
    {"max": 123, "min": 83, "label": "83-123", "color": "#43CD80"},
    {"max": 82, "min": 42, "label": "42-82", "color": "#00EE00"},
    {"max": 41, "min": 1, "label": "1-41", "color": "#00FA9A"},
    {"max": 0, "min": 0, "label": "0", "color": "#54FF9F"},
    ], ))  
Z=zip(city,hometown['hometown'])#city+数量
map.add("",[list(z) for z in Z],maptype='china')
map.render('hometown_map.html')