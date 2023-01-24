import unittest
from numpy_numeric.example import numeric




class Testing(unittest.TestCase):
    def test_add(self):
        a = 2
        b = 3
        operation = "+"
        result = numeric(a,b,operation).method()
        self.assertEqual(result, 5.0)

    def test_subtract(self):
        a = 5
        b = 2
        operation = "-"
        result = numeric(a,b,operation).method()
        self.assertEqual(result, 3.0)


def run():
    tests = unittest.TestLoader().loadTestsFromTestCase(Testing)
    # create a TextTestRunner
    runner = unittest.TextTestRunner()
    # run the test suite
    runner.run(tests)



