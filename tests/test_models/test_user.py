#!/usr/bin/python3
""" Module for testing user """
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """ Test User model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
