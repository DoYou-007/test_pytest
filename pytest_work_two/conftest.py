#通过fixture的方式来控制打印"开始计算"和"结束计算",使用的是conftest文件的方式
import pytest


@pytest.fixture(scope="function")
def print_news():
    print("开始计算")
    yield
    print("结束计算")