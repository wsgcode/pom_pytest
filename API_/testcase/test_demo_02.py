#coding: utf8
#auth:wsg

import random

import pytest

from .test_demo_03 import  my_fixture


def test_005():
    assert 1 == 1

def test_003():
    # 左开又闭
    x = random.randint(3,6)
    assert 5 == x
    print(x)

def test_004():
    assert 1 == 1

@pytest.mark.smoke
def test_006():
    assert 1 == 11

@pytest.mark.smoke
@pytest.mark.usermanage
def test_007(my_fixture):
    assert 1 == 1

@pytest.mark.run(order=1)
def test_0070():
    assert 1 == 1


