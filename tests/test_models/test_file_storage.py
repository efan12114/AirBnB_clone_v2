#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'not testing file storage')
class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            del storage.all()[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        bm = BaseModel()
        storage.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, storage.all())

    def test_save_and_reload(self):
        """ Save and reload objects """
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        storage.reload()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, storage.all())
