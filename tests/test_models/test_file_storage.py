#!/usr/bin/python3
"""
Test file for the base_mode class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestClass(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del(self.storage)
        del(self.model)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_is_instance(self):
        """isInstance"""

        self.assertIsInstance(self.storage, FileStorage)

    def test_find_object_success(self):

        self.storage.new(self.model)
        self.assertIs(
            self.storage.find('BaseModel', self.model.id), self.model
            )

    def test_find_object_not_found(self):

        self.storage.new(self.model)
        self.assertRaisesRegex(
            Exception,
            'no instance found',
            self.storage.find,
            'BaseModel',
            'does-not-exist')

    def test_reset(self):
        """reset"""
        pass

    def test_new_method(self):
        """new"""
        pass

    def test_save_method(self):
        """save method"""
        pass

    def test_reload_function(self):
        """reload function"""
        pass

    def test_function_all(self):
        """all functions"""
        pass


if __name__ == '__main__':
    unittest.main()
