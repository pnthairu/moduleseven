# Start Program
"""
""
Program: test_basic_list.py
Author: Paul Thairu
Last date modified: 06/019/2020

Unit testing user input of three numbers then saving them in  a list.

"""
import unittest
from unittest.mock import patch
import fun_with_collection.basic


class TestList(unittest.TestCase):
    @patch('fun_with_collection.basic.get_input', return_value='3')
    def test_make_list(self, input):
        self.assertEqual(fun_with_collection.basic.make_list(), [3, 3, 3])


# End program
