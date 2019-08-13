#!/usr/bin/env python
# -*- coding:UTF-8 -*-

#词云一种数据呈现方式
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
import numpy as np
from PIL import Image
import random





func_list=[]
def run(func):
    func_list.append(func)
    return func

def run_func():
    for func in func_list:
        func()


#简单示例
def func1():
    #打开文本
    text=open('constitution.txt').read()

    #生成对象
    wc=WordCloud().generate(text)

    #显示词云
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    #保存文件
    wc.to_file('wordcloud1.png')


#中文词云 没有分词
def fun2():
    text=open('xyj.txt',encoding='utf8').read()
    #font_path='Hiragino.ttf' 加载中文字体，如果不加载将不能显示中文
    wc=WordCloud(font_path='Hiragino.ttf',width=800,height=400,mode='RGBA',background_color=None).generate(text)

    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wc.to_file('wordcloud2.png')


#中文词云，先进行分词
def fun3():
    text=open('xyj.txt',encoding='utf8').read()
    text=' '.join(jieba.cut(text))

    wc=WordCloud(font_path='Hiragino.ttf',width=800,height=400,mode='RGBA',background_color=None).generate(text)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wc.to_file('wordcloud3.png')

#使用蒙版，生成制定形状
def fun4():
    text=open('xyj.txt',encoding='UTF-8').read()

    mask=np.array(Image.open('color_mask.png'))
    wc=WordCloud(font_path='Hiragino.ttf',mask=mask,mode='RGBA',background_color=None,width=1000,height=800).generate(text)

    #显示词云
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wc.to_file('wordcloud4.png')


#词云颜色从蒙版中抽取
def fun5():
    text=open('xyj.txt',encoding='UTF-8').read()
    text=' '.join(jieba.cut(text))

    mask=np.array(Image.open('color_mask.png'))
    wc=WordCloud(mask=mask,font_path='Hiragino.ttf',mode='RGBA',background_color=None).generate(text)

    image_colors=ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors)

    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wc.to_file('wordcloud5.png')

#控制每一个词的颜色
def fun6():
    text=open('xyj.txt',encoding='UTF-8').read()
    text=' '.join(jieba.cut(text))
    mask=np.array(Image.open('color_mask.png'))
    wc=WordCloud(mask=mask,color_func=random_color,font_path='Hiragino.ttf',mode='RGBA',background_color=None).generate(text)

    #显示词云
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

@run
def fun7():

    text=open('xyj.txt',encoding='UTF-8').read()
    freq=jieba.analyse.extract_tags(text,topK=200,withWeight=True)
    freq={i[0]:i[1] for i in freq}

    mask=np.array(Image.open("color_mask.png"))
    wc=WordCloud(mask=mask,font_path='Hiragino.ttf',mode='RGBA',background_color=None).generate_from_frequencies(freq)
    image_colors=ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors)

    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

#颜色函数
def random_color(word,font_size,position,orientation,font_path,random_state):
    s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
    print(s)
    return s

if __name__ == '__main__':
    run_func()
