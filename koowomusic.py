#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:25:33 2020

@author: lu
"""

import requests as r
import os
import json
from fake_useragent import UserAgent


class KooWoMusic():
    def __init__(self):
        self.ua=UserAgent()
        self.headers={"User-Agent":self.ua.firefox,
                      "Cookie":"_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P",
                      "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
                      "csrf": "HYZQI4KPK3P"}

    def seach_music(self):
        self.seach=input("请输入要下载音乐:\n")
        self.url='http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(self.seach)
        try:
            self.response=r.get(url=self.url,headers=self.headers)
        except Exception as e:
            print(e)
        
        self.json_html=json.loads(self.response.text)
        self.rid=[]
        self.artist=[]
        print('\n可以下载的歌曲有:\n')
        for i in range(len(self.json_html['data']['list'])):
            self.rid.append(self.json_html['data']['list'][i]['rid'])
            self.artist.append(self.json_html['data']['list'][i]['artist'])
            print(i,str(self.json_html['data']['list'][i]['name'])+'--'+str(self.json_html['data']['list'][i]['artist']))
            
        
    def get_music_url(self):
        self.index=input('请输入下载序号:')
        if self.index in ('0','1','2','3','4','5','6','7','8','9','10','11',
                          '12','13','14','15','16','17','18','19','20',
                          '21','22','23','24','25','26','27','28','29'):
            self.json_music_url ='http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3'.format(self.rid[int(self.index)])
            self.response2=r.get(self.json_music_url,headers=self.headers)
            self.music_url=json.loads(self.response2.text)['url']
            
    def save(self):
        self.path='/home/lu/music/kuwomusic'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        with open(self.path+'/{0}--{1}.mp3'.format(self.seach,self.artist[int(self.index)]),'wb') as f:
            f.write(r.get(self.music_url,headers=self.headers).content)
        f.close()
        
    def main(self):
        self.seach_music()
        KooWoMusic.get_music_url(self)
        self.save()

  
if __name__=='__main__':
    kw=KooWoMusic()
    kw.main()