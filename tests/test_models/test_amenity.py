#!/usr/bin/python3
"""
Test file for user class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        new_state = Amenity()
        self.assertIsInstance(new_state, Amenity)

    def test_create_istance2(self):
        """create a new instance"""
        new_state = Amenity()
        self.assertIsInstance(new_state, BaseModel)


if __name__ == '__main__':
    unittest.main()
