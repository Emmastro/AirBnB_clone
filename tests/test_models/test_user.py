#!/usr/bin/python3
"""
Test file for user class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_create_istance2(self):
        """create a new instance"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)


if __name__ == '__main__':
    unittest.main()
