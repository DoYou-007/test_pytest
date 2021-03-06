import pytest


def setup_module():
    print("这是setup_module的方法")


def teardown_module():
    print("这是teardown_module的方法")


def setup_function():
    print("这是setup_function的方法")


def teardown_function():
    print("这是teardown_function的方法")


def test_login():
    print("这是一个外部的方法")


class TestDemo:
    def setup_class(self):
        print("这是setup_class方法")

    def setup_method(self):
        print("这是setup_method方法")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")

    def teardown_methon(self):
        print("teardown_methon")

    def test_two(self):
        print("开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_thrid(self):
        print("开始执行 test_thrid方法")
        x = 'hello'
        y = 'hello world'
        assert x in y


if __name__ == "__main__":
    # pytest.main("-v -s")
    pytest.main(['-v','-k','TestDemo'])