#!/usr/bin/python3
"""
Test file for user class
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        new_place = Place()
        self.assertIsInstance(new_place, Place)

    def test_create_istance2(self):
        """create a new instance"""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)


if __name__ == '__main__':
    unittest.main()
