#!/usr/bin/python3
"""Test City"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City module"""

    def test_class(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel))
