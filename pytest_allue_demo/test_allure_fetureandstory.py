# @allure.feature在模块前加入表示测试哪个功能的用例
# @allure.story 在case前加入表示子模块的场景
# with allure.step("点击用户名"): 用于指点测试的具体步骤
import allure
import pytest


@allure.feature("登录")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录成功的测试用例")
        pass

    @allure.story("登录失败")
    def test_login_success_a(self):
        print("这是登录失败的测试用例")
        pass

    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("这是用户名缺失的测试用例")
        pass

    # 如下case表明了测试步骤
    @allure.story("密码缺失")
    def test_login_failure_a(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass

    @allure.story("登录失败")
    def test_login_failure_b(self):
        print("这是登录失败的测试用例")
        pass


@allure.feature("搜索")
class TestSearch:
    @allure.story("第一次")
    def test_search1(self):
        print("第一次搜索")
        pass

    @allure.story("第二次")
    def test_search2(self):
        print("第二次搜索")
        pass


if __name__ == "__main__":
    pytest.main(['-v', '-s'])
