# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('dark_background')
plt.rcParams['font.sans-serif']=['YouYuan']
df=pd.read_csv('weibo_inf.csv',encoding='gbk')#读取数据
gender=pd.DataFrame(df['gender'].value_counts())#统计数字放入表

plt.pie(gender['gender'],
        labels=['女','男'],
        colors=['#fe8e9c','#8cebff'],
        shadow=True,
        autopct='%1.2f%%',
        textprops={'fontsize': 20, 'color': 'white'},
       )
plt.legend(loc='upper right')
plt.title('#华小诗粉丝性别占比#')
plt.axis('equal') #标准圆 
plt.show()