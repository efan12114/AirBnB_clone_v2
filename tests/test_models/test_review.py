#!/usr/bin/python3
""" Module for testing review """
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test Review model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        review = Review()
        self.assertIsInstance(review.place_id, str)
