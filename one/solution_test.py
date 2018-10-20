import unittest
import solution

class OneTest(unittest.TestCase):
    def test_oneValue(self):
        self.assertEqual("2002", solution.seq(2000,2005))

    def test_twoValues(self):
        self.assertEqual("2002,2009", solution.seq(2000, 2010))

    def test_threeValues(self):
        self.assertEqual("2002,2009,2016", solution.seq(2000, 2020))