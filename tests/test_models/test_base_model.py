#!/usr/bin/python3
"""
Test file for the base_mode class
"""
import unittest
from models.base_model import BaseModel


class TestClass(unittest.TestCase):

    def test_create_istance(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_assign_attribute(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertIs(my_model.name, "Holberton")
        self.assertIs(my_model.my_number, 89)

if __name__ == '__main__':
    unittest.main()
