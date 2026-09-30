#!/usr/bin/python3
""" Module for testing city """
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """ Test City model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        city = City()
        self.assertIsInstance(city.state_id, str)
