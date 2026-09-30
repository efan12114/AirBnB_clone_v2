#!/usr/bin/python3
""" Module for testing place """
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test Place model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        place = Place()
        self.assertIsInstance(place.city_id, str)
