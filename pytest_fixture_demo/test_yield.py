import pytest

#作用域：是在模块之前执行，之后执行。
@pytest.fixture(scope="module")
def  open():
    print("打开浏览器")
    yield

    print("执行teardown操作")
    print("关闭浏览器")

def  test_search1(open):
    print("test_search1")
    pass

def  test_search2(open):
    print("test_search2")
    pass

def  test_search3(open):
    print("test_search3")
    pass

if __name__ == "__main__":
    pytest.main("-v -s")