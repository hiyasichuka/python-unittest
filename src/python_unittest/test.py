import unittest

from calc import Calc

sut = Calc()


class CalcTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sut.add(1, 2), 3)

    def test_minus(self):
        self.assertEqual(sut.minus(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(sut.multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(sut.divide(8, 2), 4)

    def foo(self):
        print("foo!!")
