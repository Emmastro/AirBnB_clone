#!/usr/bin/python3
"""
Test file for the base_mode class
"""

import unittest
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """ Test case init instance"""
        new_model = BaseModel()
        self.assertIsInstance(new_model, BaseModel)

    def test_assign_attribute(self):
        """ Test new attribute"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertIs(my_model.name, "Holberton")
        self.assertIs(my_model.my_number, 89)

    def test_create_instance2(self):
        """create an instance using dictionary"""
        model_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                      'created_at': '2017-09-28T21:03:54.052298',
                      '__class__': 'BaseModel', 'my_number': 89,
                      'updated_at': '2017-09-28T21:03:54.052302',
                      'name': 'Holberton'}
        my_model = BaseModel(**model_dict)
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.id,
                         "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(my_model.name, "Holberton")


if __name__ == '__main__':
    unittest.main()
