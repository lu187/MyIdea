#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:43:44 2020

@author: lu
"""


import requests as r
import json
from lxml import etree as le
import os
from fake_useragent import UserAgent
import random


class DpcqCartoon():
    def __init__(self):
        self.user_agent_list=[]
        for i in range(100):
            self.ua=UserAgent()
            self.user_agent_list.append(self.ua.firefox)
            
        self.get_title_and_chapter_id_url='https://comic.mkzcdn.com/chapter/?comic_id=49733'# 会更新
        self.header={'User-Agent':random.choice(self.user_agent_list)}
    def get_title_and_chapter_id(self):
        self.respones=r.get(self.get_title_and_chapter_id_url,headers=self.header)
        self.json_dict=json.loads(self.respones.text)# 将json数据转为字典
        self.title_list=[]
        self.chapter_id_list=[]
        for i in range(871,871):# 控制爬取节章,870对应868话
            self.title_list.append(self.json_dict['data'][i]['title'])# 获取文件夹名
            self.chapter_id_list.append(self.json_dict['data'][i]['chapter_id'])# 获取构造网址的必备参数chapter_id
        
    def get_img_url_and_save(self):
        for num in range(len(self.chapter_id_list)):
            self.home_img_url='https://www.mkzhan.com/49733/{}.html'.format(int(self.chapter_id_list[num]))#构造网址
            self.respones1=r.get(self.home_img_url,headers=self.header)
            self.html=le.HTML(self.respones1.text)# 构造解析对象
            self.src=self.html.xpath('/html/body/div[2]/div[2]/div/img/@data-src')# 获取所有图片地址,type:列表
            for urlnum in range(len(self.src)):
                self.save_path=r'/home/lu/cartoon/斗破苍穹/{}'.format(self.title_list[num])
                if not os.path.exists(self.save_path):# 判断目录师是否存在,不存在就创建
                    os.makedirs(self.save_path)
                with open(self.save_path+'/{}.jpg'.format(urlnum),'wb') as file:# 保存图片
                    file.write(r.get(self.src[urlnum], headers=self.header).content)

if __name__=='__main__':
    dp=DpcqCartoon()
    dp.get_title_and_chapter_id()
    dp.get_img_url_and_save()
