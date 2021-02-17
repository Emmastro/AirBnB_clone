#!/usr/bin/python3
"""
Test file for the base_mode class
"""

import unittest
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del(self.model)
        return super().tearDown()

    def test_create_istance(self):
        """ Test case init instance"""

        self.assertIsInstance(self.model, BaseModel)

    def test_assign_attribute(self):
        """ Test new attribute"""
        self.model.name = "Holberton"
        self.model.my_number = 89
        self.assertIs(self.model.name, "Holberton")
        self.assertIs(self.model.my_number, 89)

    def test_create_instance_from_dict(self):
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

    def test_to_dict_success(self):

        self.model.name = "Holberton"
        self.model.my_number = 89
        my_model_json = self.model.to_dict()

        self.assertDictEqual(my_model_json, {
            'id': self.model.id,
            'created_at': self.model.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.model.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'name': self.model.name,
            'my_number': self.model.my_number,
            '__class__': BaseModel.__name__})


if __name__ == '__main__':
    unittest.main()
