# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:15:52 2018

@author: Administrator
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests
import re

#模拟浏览器去请求，获取图片
def download():
    startUrl='http://www.uustv.com/'
    #获取用户输入的姓名
    name=entry.get()
    #去空格
    name=name.strip()
    if name=='':
        messagebox.showinfo('提示','请输入姓名！')
    else:
        #模拟网页发送数据
        data={
                'word':name,
                'sizes':'60',
                'fonts':'jfcs.ttf',
                'fontcolor':'#000000'
        }
        result=requests.post(startUrl,data=data)
        #print(data)
        #中文乱码的解决方法
        result.encoding='utf-8'
        #获取网页源代码
        html=result.text
        #正则表达式 匹配出任意的图片地址  .*?匹配所有
        #<div class="tu">﻿<img src="tmp/153258882767905.gif"></div>  时间戳
        req='<div class="tu">﻿<img src="(.*?)"/></div>'
        imagePath=re.findall(req,html)
        #print(imagePath)
        #图片的完整的路径
        imgUrl=startUrl+imagePath[0]
        #print(imgUrl)
        #获取图片内容
        response=requests.get(imgUrl).content
        
        #保存图片  format字符串格式化
        f=open('{}.gif'.format(name),'wb')
        f.write(response)
        f.close()
        
        #显示图片
        bm=ImageTk.PhotoImage(file='{}.gif'.format(name))
        label2=Label(root,image=bm)
        #label2的背景图片为bm
        label2.bm=bm
        #图片定位  跨列合并两列columnspan
        label2.grid(row=2,columnspan=2)

#创建窗口
root=Tk()
#标题
root.title('签名设计')
#窗口大小 小写的x
root.geometry('600x300+300+200')

#标签控件
label=Label(root,text='签名',font=('华文行楷',20),fg='red')
#grid网格式的布局 pack place
label.grid(row=0,column=0)

#输入框
entry=Entry(root,font=('微软雅黑',20))
entry.grid(row=0,column=1)
#点击按钮
button=Button(root,text='设计签名',font=('微软雅黑',20),command=download)
button['width']=10
button['height']=1
#sticky 对齐方式  W E N S
button.grid(row=1,column=1,sticky=E)


#显示窗口 消息循环
root.mainloop()