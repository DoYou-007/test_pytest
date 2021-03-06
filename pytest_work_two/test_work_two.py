"""
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""

import pytest
import yaml
from pytest_work_two.Calculator import  Calculator
import os


#读取yaml文件中的数据
with open('/Users/xieguojun/Hogwarts/python_pytest/test_pytest/pytest_work_one/datas.yaml', 'r') as f:
    value = yaml.safe_load(f)
    print(value)

# #通过fixture的方式来控制打印"开始计算"和"结束计算"
# @pytest.fixture(scope="function")
# def print_news():
#     print("开始计算")
#     yield
#     print("结束计算")


class TestCalc:

    def setup_class(self):
        #实例化类，生成实例化对象
        self.calc = Calculator()

    #使用参数化生成用例
    """
    a,b的值可能是：整数，零，负数，特殊字符，中文
    """
    # @pytest.mark.run(order=0)  #也可以通过序号的形式指定运行顺序
    @pytest.mark.first
    @pytest.mark.parametrize("a,b,expecter",value['values_add'])
    def test_add(self,a,b,expecter,print_news):
        #调用calculator中的add方法，将结果保存到result中
        try:
            result = self.calc.add(a,b)
            if isinstance(result,float):
                result =round(result,3)
            print(result)
            #将结果和预期值进行对比
            assert result == expecter
        except TypeError:
            print('这是a,b值不是整数类型的case')

    # @pytest.mark.run(order=3)
    @pytest.mark.foure
    @pytest.mark.parametrize("a,b,expecter",value['values_div'])
    def test_div(self,a,b,expecter,print_news):
        # 调用calculator中的div方法，将结果保存到result中
        try:
            result = self.calc.div(a, b)
            print(result)
            # 将结果和预期值进行对比
            assert result == expecter
        except ZeroDivisionError:
            print('这是当除数为零的case')

    # @pytest.mark.run(order=1)
    @pytest.mark.second
    @pytest.mark.parametrize("a,b,expecter", value['values_sub'])
    def test_sub(self, a, b, expecter,print_news):
        # 调用calculator中的div方法，将结果保存到result中
        try:
            result = self.calc.sub(a, b)
            print(result)
            # 将结果和预期值进行对比
            assert result == expecter
        except ZeroDivisionError:
            print('这是当除数为零的case')

    # @pytest.mark.run(order=2)
    @pytest.mark.third
    @pytest.mark.parametrize("a,b,expecter", value['values_mul'])
    def test_mul(self, a, b, expecter,print_news):
        # 调用calculator中的div方法，将结果保存到result中
        try:
            result = self.calc.mul(a, b)
            print(result)
            # 将结果和预期值进行对比
            assert result == expecter
        except ZeroDivisionError:
            print('这是当除数为零的case')

if __name__ == "__main__":
    pytest.main('-v -s ')
