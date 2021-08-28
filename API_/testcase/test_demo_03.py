# coding: utf8
# auth:wsg
import pytest


@pytest.fixture()
def my_fixture():
    print('\n' + '前置')
    yield
    print('\n' + '后置')


class TestCase03():
    @pytest.mark.smoke
    def test_03(self,my_fixture):
        print('这是第三个用例')

    def test_02(self):
        print('这是第2个用例')

    @pytest.mark.run(order=1)
    def test_04(self):
        print('这是第4个用例')
