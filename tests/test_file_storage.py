#  !/ust/bin/python3
"""
A file for testing file_storage module, a module for all storage \
        purpose and retrievals
"""
import os
import unittest
from unittest.mock import Mock
from typing import Dict
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test class for testing the functionality of Filestorage attributes \
            and methods
    """

    def setup(self):
        '''
        sets up all resources required to test
        '''
        try:
            os.rename("file.json", "temp.json")
        except Exception:
            pass

    def teardown(self):
        '''
        releases all resources before exiting test; hence usually \
                called at last
        '''
        try:
            #  remove used file
            os.remove("file.json")
        except Exception:
            pass

        try:
            #  replace org content
            os.rename("temp.json", "file.json")
        except Exception:
            pass

    def test_all(self) -> None:
        '''
        tests all method in file_storage file
        '''
        #  instantiate class
        store: FileStorage = FileStorage()
        #  test
        self.assertEqual(dict, type(store.all()))

    def test_with_args(self) -> None:
        '''
        tests all method in file_storage file with arg
        '''
        #  instantiate class
        store: FileStorage = FileStorage()
        #  test
        with self.assertRaises(TypeError):
            store.all(None)

    def test_new_no_arg(self) -> None:
        '''
        tests new method with args in file_storage file
        '''
        #  instantiate class
        store: FileStorage = FileStorage()
        #  test
        with self.assertRaises(AttributeError):
            store.new(None)

    def test_save(self) -> None:
        '''
        tests save method in file_storage file
        '''
        #  instantiate class
        store: FileStorage = FileStorage()
        common_model: BaseModel = BaseModel()

        #  perform a save action
        common_model.save()

        #  perform a save action
        json_str = ""
        with open("file.json", "r") as f:
            #  get saved text and read to json_str
            json_str = f.read()
        #  test
        self.assertIsInstance(json_str, str)

    def test_reload(self) -> None:
        '''
        tests save method in file_storage file
        '''
        #  instantiate class
        store: FileStorage = FileStorage()
        common_model: BaseModel = BaseModel()
        #  perform a reload()
        store.reload()

        #  with name mangling access attribute dict
        test_obj = store.all()

        #  test
        self.assertIsInstance(test_obj, dict)
        self.assertIn("BaseModel." + common_model.id, test_obj)


if __name__ == "__main__":
    unittest.main()
