#fixture提供了一个参数传递的方法但是视频中讲的不全需要自己查看文档

import pytest


# @pytest.fixture(params=[1, 2, 3, 'linda'])
# def test_data(request):
#     return request.param


# @pytest.fixture(params=[(1,3), (4,5)])   #params输入的是列表是需要进行索引取值，
# def test_data(request):
#     return request.param

@pytest.fixture(params=[{'a': 1, "b": 2}, {"name": 'Jerry', "age": 23}])  # params参数组合，执行失败
def test_data(request):
    print(request.param)
    return request.param

def test_one(test_data):
    print('test_data1 :%s' % test_data.values[0])
