#某些场景需要登录，某些则不需要
import pytest

@pytest.fixture()
def login():
    print("这是个登录的方法")

def  test_case1(login):
    print("test_case1需要登录")
    pass

def  test_case2():
    print("test_case2不需要登录")
    pass

def  test_case3(login):
    print("test_case1需要登录")
    pass

if __name__ == "__main__":
    pytest.main()