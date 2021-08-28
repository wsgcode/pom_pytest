#coding: utf8
#auth:wsg

from selenium import webdriver


class BasePage:

    # 相同属性
    # 获取浏览器对象
    def __init__(self,driver):
        self.driver = driver

    # 相同的行为
    def location(self,loc):
        '''元素定位方法：支持各种定位方式'''
        return self.driver.find_element(*loc)

    #输入
    def send_key_(self,loc,value):
        self.location(loc).send_keys(value)

    # 点击
    def click_(self,loc):
        self.location(loc).click()

    # 获取项目地址
    def getURL(self,url):
        self.driver.get(url)



