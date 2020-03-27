import pytest
import yaml


# 使用mark.paramtrize的方式
class TestData1:
    # @pytest.mark.parametrize("a,b", [(12, 10),(15,20),(52,31)])
    # @pytest.mark.parametrize(('a','b'), [(12, 10), (15, 20), (52, 31)])  #通过元组的方式，可以调用元组的方法
    @pytest.mark.parametrize(['a', 'b'], [(12, 10), (15, 20), (52, 31)])  # 通过列表的方式，可以调用元组的方法
    def test_data1(self, a, b):
        print(a + b)


# 使用yaml文件的方式
class TestData2:
    @pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yaml")))
    # @pytest.mark.parametrize(('a','b'), yaml.safe_load(open("./data.yaml")))  #通过元组的方式，可以调用元组的方法
    # @pytest.mark.parametrize(['a','b'],yaml.safe_load(open("./data.yaml")))    #通过列表的方式，可以调用元组的方法
    def test_data2(self, a, b):
        print(a + b)


if __name__ == "__main__":
    pytest.main(['-v', '-s'])
