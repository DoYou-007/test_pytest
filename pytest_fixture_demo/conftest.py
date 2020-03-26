import pytest

# 不带参数的fixure默认参数为scope=function
@pytest.fixture()
def login():
    print("这是个登录的方法")


def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
