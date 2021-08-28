#coding: utf8
#auth:wsg

import pytest
from selenium import webdriver

from pytest_pom.wbe.PageObject.login_page import Login_page


class TestCase_01:
    user_pwd = [('wsg','1233','登陆成功'),('wsg','123','登陆成功')]
    @pytest.mark.parametrize('username,pwd,expected_result',user_pwd)
    def test_01(self,username,pwd,expected_result):
        self.driver = webdriver.Chrome()
        Login_page(self.driver).login(username,pwd,expected_result)


