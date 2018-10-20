class My_Class():
    def __init__(self):
        self.input_string = ''

    def get_string(self):
        self.input_string = input()

    def print_string(self):
        return self.input_string.upper()

import unittest
class My_Test(unittest.TestCase):
    def setUp(self):
        self.obj = My_Class() # Assemble
    def test_print_string(self):
        self.obj.get_string() #Act
        self.assertEqual("HELLO", self.obj.print_string()) #Assert