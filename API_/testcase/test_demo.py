#coding: utf8
#auth:wsg
import os
from time import sleep

import pytest


@pytest.mark.parametrize('x,y',[(1,1),(1,2)])
def test_001(x,y):
    sleep(2)
    assert x == y


@pytest.mark.parametrize('x,y',[(1,1),(1,2)])
def test_002(x,y):
    sleep(2)
    assert x != y

# if __name__ == '__main__':
    # pytest.main(['./test_demo_02.py'])
    # pytest.main()
    # os.system('allure generate ./temp -o ./reports --clean')