"""
课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()

代码地址: https://github.com/EverythingWillFlow/lagou05.git 12
"""

#补全计算器（加法 除法）的测试用例
import pytest
import yaml
from test_pytest.pytest_work_one.calculaotr.calculator import Calculator

#读取yaml文件中的数据
with open('/Users/xieguojun/Hogwarts/python_pytest/test_pytest/pytest_work_one/datas.yaml', 'r') as f:
    value = yaml.safe_load(f)
    print(value)

class TestCalc:

    def setup_method(self):
        print('开始计算')

    def teardown_method(self):
        print('结束计算')

    def setup_class(self):
        #实例化类，生成实例化对象
        self.calc = Calculator()

    #使用参数化生成用例
    """
    a,b的值可能是：整数，零，负数，特殊字符，中文
    """
    @pytest.mark.parametrize("a,b,expect",value['values_add'])
    def test_add(self,a,b,expect):
        #调用calculator中的add方法，将结果保存到result中
        result = self.calc.add(a,b)
        print(result)
        #将结果和预期值进行对比
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",value['values_div'])
    def test_div(self,a,b,expect):
        # 调用calculator中的div方法，将结果保存到result中
        result = self.calc.add(a, b)
        print(result)
        # 将结果和预期值进行对比
        assert result == expect

if __name__ == "__main__":
    pytest.main('-v -s ')
