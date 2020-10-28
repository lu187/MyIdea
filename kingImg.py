#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:22:10 2020

@author: lu
"""


import requests as r
from selenium import webdriver 
import time
  
class Wz():
    """
    功能描述:王者荣耀图下载
    """
    def __init__(self):
        self.headers={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}
        self.driver=webdriver.Firefox()
        
    def go_home(self):
        self.url='https://pvp.qq.com/web201605/wallpaper.shtml'
        self.driver.get(self.url)
        time.sleep(10)
    
    def get_img_name_and_url_list(self):
        self.tuples1=('1024x768','1440x900','1920x1200','other')
        print('请选择下载图片的大小或退出:\n')
        for i in enumerate(self.tuples1):
            print(i)
            
        while 1:
            try:
                self.input1=input("请输入数字代表的像素值:")
                if self.input1 == str(0):
                    self.img_name_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/img')
                    self.img_url_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/a')
                    print('正在下载,请稍候.......')
                elif self.input1 == str(1):
                    self.img_name_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/img')
                    self.img_url_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/ul/li[4]/a')
                    print('正在下载,请稍候.......')
                elif self.input1 == str(2):
                    self.img_name_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/img')
                    self.img_url_list=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/ul/li[6]/a')
                    print('正在下载,请稍候.......')
                else:
                    break
            except Exception:
                print('图片的网站或名字获取不到!!!!')
                continue
            break
    def save_img(self):
        self.l=[]
        for i in self.img_name_list:
            self.l.append(i.get_attribute('alt')) 
        for i in range(len(self.img_name_list)):
            b=self.img_url_list[i].get_attribute('href')
            f=open('/home/lu/kingPicture/{}.jpg'.format(self.l[i]),'wb')
            f.write(r.get(b, headers=self.headers).content)
        print('下载成功了')
    
    def next(self):
        self.Next=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[3]/a[12]')
        self.Next.click()
        
    def close(self):
        self.driver.close()
        


if __name__=='__main__':
    wz=Wz()
    wz.go_home()
    k=23
    while (k>0):
        wz.get_img_name_and_url_list()
        try:
            wz.save_img()
        except Exception:
            print('以退出下载')
            break
        wz.next()
        k-=1
    wz.close()
    
    
    
