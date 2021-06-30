#!/usr/bin/python3
"""Test State"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """test State module"""

    def test_class(self):
        """test class"""
        self.assertEqual(State.name, "")
        self.assertTrue(State, BaseModel)
