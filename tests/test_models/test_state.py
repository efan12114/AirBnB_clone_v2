#!/usr/bin/python3
""" Module for testing state """
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """ Test State model """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage defaults')
    def test_attribute_types(self):
        """ Test attribute types for file storage """
        state = State()
        self.assertIsInstance(state.name, str)
