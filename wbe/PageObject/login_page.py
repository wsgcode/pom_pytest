#coding: utf8
#auth:wsg
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest_pom.wbe.Base.basePage import BasePage


class Login_page(BasePage):

    # 属性
    url = "http://127.0.0.1:8000/student/login/"
    username = [By.XPATH,"//input[@name='uname']"]
    pwd = [By.XPATH, "//input[@name='pwd']"]
    submit = [By.XPATH,"//input[@type='submit']"]

    # 方法

    def login(self,username,pwd,expected_result):
        # 浏览器打开网址
        self.getURL(url=self.url)
        # 输入用户名
        self.send_key_(loc = self.username,value=username)
        # 输入密码
        self.send_key_(loc=self.pwd, value=pwd)
        # 点击登录
        self.click_(loc=self.submit)

        # # 做断言用
        fect_result = self.location([By.TAG_NAME,'body']).text
        assert expected_result == fect_result



if __name__ == '__main__':
    driver = webdriver.Chrome()
    a = Login_page(driver)
    username = 'wsg'
    pwd = '123'
    a.login(username,pwd,'登陆成功')