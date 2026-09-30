#!/usr/bin/python3
""" Module for testing base_model """
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel class """

    def setUp(self):
        """ Set up test environment """
        self.bm = BaseModel()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """ Test instantiation """
        self.assertIsInstance(self.bm, BaseModel)

    def test_save(self):
        """ Test save method """
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """ Test to_dict method """
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
