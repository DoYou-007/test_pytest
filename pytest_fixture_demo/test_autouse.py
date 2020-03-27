#fixture自动运行得测试demo：
import pytest

#autouse 默认为false，当改成true时每个测试用例均会调用这个方法
@pytest.fixture(autouse="True")
def  open():
    print("打开浏览器")

def  test_search1():
    print("test_search1")
    pass

def  test_search2():
    print("test_search2")
    pass

def  test_search3():
    print("test_search3")
    pass

if __name__ == "__main__":
    pytest.main("-v -s")