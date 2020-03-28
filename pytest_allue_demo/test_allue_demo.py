import pytest


@pytest.mark.search
def test_search1():
    print("test_search1")
    pass


@pytest.mark.search
def test_search2():
    print("test_search2")
    pass


@pytest.mark.login
def test_login1():
    print("test_login1")
    pass


@pytest.mark.login
def test_login2():
    print("test_login2")
    pass


if __name__ == "__main__":
    pytest.main("-v -s")
