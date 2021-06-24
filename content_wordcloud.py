# -*- coding: utf-8 -*-


import jieba
import wordcloud
import imageio


f = open(r"C:\Users\86153\Desktop\关于华师官微的分析\output.txt", "r",encoding='ANSI')
t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)

pac_mask = imageio.imread(r'C:\Users\86153\Desktop\关于华师官微的分析\龙猫.jpg')

w=wordcloud.WordCloud(font_path='msyh.ttc',background_color='white',stopwords={'华中师范大学','\n','n','你','我','的','在','呢','吧','做','里','是'},max_words=1000,mask=pac_mask)
w.generate(txt)
w.to_file('content_wordcloud.jpg')