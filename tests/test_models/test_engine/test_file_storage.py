#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
import json
import os

User = models.user.User
BaseModel = models.base_model.BaseModel
FileStorage = models.engine.file_storage.FileStorage
storage = models.storage
file = 'file.json'


class TestFileStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    def test_doc_file(self):
        """documentation for the file"""
        expected = ("Storage class")
        actual = models.engine.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """documentation for the class"""
        expected = 'Serializes instances and deserializes JSON file'
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)


class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()
        self.bm_obj = BaseModel()

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        os.remove(file)
        self.user.save()
        self.assertTrue(os.path.isfile(file))

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        u_id = self.user.id
        all_obj = storage.all()
        actual = 0
        for keys in all_obj.keys():
            if u_id in keys:
                actual = 1
        self.assertTrue(1 == actual)

    def test_obj_saved_to_file(self):
        """checks proper FileStorage instantiation"""
        os.remove(file)
        self.user.save()
        u_id = self.user.id
        actual = 0
        with open(file, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for keys in storage_dict.keys():
            if u_id in keys:
                actual = 1
        self.assertTrue(1 == actual)

    def test_reload(self):
        """checks proper usage of reload function"""
        os.remove(file)
        self.bm_obj.save()
        u_id = self.bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for keys in all_obj.keys():
            if u_id in keys:
                actual = 1
        self.assertTrue(1 == actual)


if __name__ == '__main__':
    unittest.main
