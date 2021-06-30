#!/usr/bin/python3
"""Test user"""
import unittest
from models.base_model import BaseModel
from models.user import User



class Test_user(unittest.TestCase):
    """Tests the user module"""

    def test_class(self):
        """Test class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
        self.assertTrue(isinstance(new_user, BaseModel))
