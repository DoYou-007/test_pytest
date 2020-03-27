#mark提供一个参数传递的方法
import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2/4",0.5),("5*7",30)])
def test_eval(test_input,expected):
    #eval 将字符串str当成有效的字符串进行运算并返回结果
    assert  eval(test_input) == expected


#参数进行组合

@pytest.mark.parametrize("x",(2,4))
@pytest.mark.parametrize("y",(7,9,10))
def  test_foo(x,y):
    print(f"测试数据的组合x:{x}, y:{y}")