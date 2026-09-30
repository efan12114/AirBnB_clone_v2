#!/usr/bin/python3
""" Module for testing amenity """
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test Amenity model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
