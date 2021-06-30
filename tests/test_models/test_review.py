#!/usr/bin/python3
"""Review Test"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review Class"""

    def test_review(self):
        """test the reviewclass"""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, Review))
