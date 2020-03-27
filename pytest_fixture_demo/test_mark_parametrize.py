#mark提供一个参数传递的方法
import sys

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


# 方法名进行传输
test_user_data = ['Tome', 'Jerry']


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"打开首页准备登录，登录用户：{user}")
    return user


# @pytest.mark.skip("此次不执行登录")   #增加跳过操作
# @pytest.mark.skipif(sys.platform =="windows",reason="不在macos上不执行")   #增加注释如：系统版本为darwin则跳过
@pytest.mark.xfail  # 当已知用例失败时可以通过xfail跳过
# indirect=True 可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login1(login_r):
    a = login_r
    print(f"测试用例中login的返回值；{a}")
    assert a != ""
