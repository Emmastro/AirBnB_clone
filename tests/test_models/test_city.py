#!/usr/bin/python3
"""
Test file for city class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        new_city = City()
        self.assertIsInstance(new_city, City)

    def test_create_istance2(self):
        """check if it's instance of parent"""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_class_attribut(self):
        """initialze class attribute"""
        new_city = City()
        new_city.name = "kigali"
        self.assertNotEqual(City.name, new_city.name)

    def test_parent_of_city(self):
        """check if city is parent of BaseModel"""
        new_city = City()
        self.assertEqual(isinstance(new_city, BaseModel), True)

if __name__ == '__main__':
    unittest.main()
