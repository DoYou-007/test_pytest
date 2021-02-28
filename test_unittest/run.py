import unittest

if __name__ == "__main__":
    test_dir = './test_case/'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    unittest.TextTestRunner().run(discover)