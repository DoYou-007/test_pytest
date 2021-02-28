import unittest
from unittest import TestCase
from calculator import Calculator
from hamcrest import *

from unit.HTMLTestRunner_PY3 import HTMLTestRunner


class TestCalculator(TestCase):
    @classmethod
    def setUpClass(self):
        self.cal = Calculator()

    def setUp(self) -> None:
        print("开始计算")

    def tearDown(self) -> None:
        print("计算结束")

    def test_add(self):
        result = self.cal.add(10,30)
        print('相加的结果：',result)
        assert result == 40

    def test_mul(self):
        result = self.cal.mul(2,30)
        print('相乘的结果：', result)
        # assert_that(result,equal_to(60))
        self.assertEqual(result,60)

    def test_div(self):
        result = self.cal.div(40,2)
        print('除数的结果：', result)
        assert_that(result,close_to(20,21))

    def test_sub(self):
        result = self.cal.sub(40,12)
        print('相减的结果：', result)
        assert_that(result,equal_to(28))

class TestCalculator1(TestCase):
    @classmethod
    def setUpClass(self):
        self.cal = Calculator()

    def setUp(self) -> None:
        print("开始计算_1")

    def tearDown(self) -> None:
        print("计算结束_1")

    def test_add1(self):
        result = self.cal.add(10,30)
        print('相加的结果_1：',result)
        assert result == 40

    def test_mul1(self):
        result = self.cal.mul(2,30)
        print('相乘的结果_1：', result)
        # assert_that(result,equal_to(60))
        self.assertEqual(result,60)

    def test_div1(self):
        result = self.cal.div(40,2)
        print('除数的结果_1：', result)
        assert_that(result,close_to(20,21))

    def test_sub1(self):
        result = self.cal.sub(40,12)
        print('相减的结果_1：', result)
        assert_that(result,equal_to(28))

if __name__ == "__main__":
    #方法一：通过main的方式来进行运行
    # unittest.main()

    #方法二：通过测试套件的方式来进行运行
    # suite = unittest.TestSuite()
    # suite.addTest(TestCalculator('test_mul'))
    # suite.addTest(TestCalculator1('test_sub1'))
    # unittest.TextTestRunner().run(suite)

    #方法三：同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator1)
    suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suite)

    #生成测试报告
    report_file = 'calculator.html'
    report_title = '计算机的测试报告'
    desc = "用于展示HHTMLTestrunner的测试报告"

    # testsuite = unittest.TestSuite()
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))
    # # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCalculator1))

    with open(report_file,'wb') as report :
        runner = HTMLTestRunner(stream=report,title=report_title,description=desc)
        runner.run(suite)