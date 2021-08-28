#coding: utf8
#auth:wsg
import os
import pytest

if __name__ == '__main__':
    # 运行一个.py文件中的一个方法用例
    # pytest.main(['-vs','./API_/testcase/test_demo.py::test_001'])
    # 用两个线程去运行
    # pytest.main(['-vs','./API_/testcase/test_demo.py','-n=2'])
    # 失败用例重跑，跑三次
    # pytest.main(['-vs','./API_/testcase/test_demo_02.py','--reruns=3'])
    # 只要有一个用例失败就不在运行其他用例
    # pytest.main(['-vs','./API_/testcase/test_demo_02.py','-x'])
    # --maxfail num:出现num个失败用例就停止。
    # pytest.main(['-vs', './API_/testcase/test_demo_02.py', '--maxfail=2'])
    # -k: 根据测试用例的部分字符串指定测试用例。
    # pytest.main(['-vs','./API_/testcase/test_demo_02.py','-k 07'])
    #   只运行标记smoke和usermanage的用例
    # pytest.main(['./API_/testcase/test_demo_02.py','-m smoke and usermanage'])
    # 生成html测试报告
    # pytest.main(['./API_/testcase/test_demo_02.py','--html=./report/report.html'])

    pytest.main(['-vs','./'])
    os.system('allure generate ./temp -o ./report --clean')