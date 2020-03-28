import allure


@allure.link("www.baidu.com", name="链接")
def test_link():
    print("这是一条加了连接的用例")
    pass


# --allrue-link-pattern=issue:http://www.mytestracker.com/issue/
@allure.issue('10', "这是一个issue")
def test_link_issue():
    pass


TESKCASE = "https://github.com/XFbeibei/test_pytest"


@allure.link(TESKCASE, '用例地址')
def test_testcase_link():
    print("这是一条加了链接的测试用例")
    pass
