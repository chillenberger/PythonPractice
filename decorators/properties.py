# @ property decorator 
# this is a pythonic way to use getters and setters in 
# object oriented programming. 

import unittest

class myClass:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('setting temperature')
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        print('deleting')
        del self._temperature

    def to_fahrenheit(self):
        rsp = (self.temperature*1.8) + 32
        return round(rsp, 1)


class TestmyClass(unittest.TestCase):
    def setUp(self):
        self.test_class = myClass(30)


    def test_to_fahrenheit(self):
        rsp = self.test_class.to_fahrenheit()
        print(rsp)
        self.assertEqual(rsp, 86)

    def test_change_temp(self):
        self.test_class.temperature = 37
        rsp = self.test_class.to_fahrenheit()
        print(rsp)
        self.assertEqual(rsp, 98.6)

    def test_delete(self):
        del self.test_class.temperature


if __name__ == '__main__':
    # unittest.main()
    test = myClass(20)
    del test.temperature