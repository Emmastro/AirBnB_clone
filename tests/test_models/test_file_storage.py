#!/usr/bin/python3
"""
Test file for the base_mode class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_is_instance(self):
        """isInstance"""
        new_st = FileStorage()
        self.assertIsInstance(new_st, FileStorage)

    def test_new_method(self):
        """new"""
        pass

    def test_save_method(self):
        """save method"""
        pass

    def test_reload_function(self):
        """reload function"""
        pass

    def test_functtion_all(self):
        """all functions"""
        pass

if __name__ == '__main__':
    unittest.main()
