# content of test_sample.py
import pytest
def func(x):
    return x + 1

class TestDemo():
	def test_answer1(self):
		assert func(4) == 5
		
	def test_answer2(self):
		assert func(2) == 5
		
	def test_answer3(self):
		assert func(4) == 5
		
	def test_answer4(self):
		assert func(4) == 5
		
class TestDemo2():
	def test_one(self):
		print("开始执行 test_one方法")
		x = 'this' 
		assert 'h' in x
		
	def test_two(self):
		print("开始执行 test_two方法")
		x = 'hello' 
		assert 'e' in x
		
	def test_thrid(self):
		print("开始执行 test_thrid方法")
		x = 'hello'
		y = 'hello world'
		assert x in y
		
	def test_four(self):
		print("开始执行 test_four方法")
		x = 'one two three' 
		assert 'one' in x
		
		
if  __name__ == '__main__':
	pytest.main(['test_demo.py::TestDemo',"-v"])
	# pytest.main(['-v','-k','TestDemo1'])
	# pytest.main("-v -k TestDemo ")