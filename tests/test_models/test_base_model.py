#!/usr/bin/python3
'''                                                                            Test File for the BaseModel class, a class that defines all common \
        attributes/methods for other classes
'''

import unittest
from models.base_model import BaseModel
from typing import Dict

class TestBaseModel(unittest.TestCase):
    '''
    Test class for the functoinality of BaseModel class
    '''
    def test_init(self):
        '''
        Test to assert attributes are properly initialized
        '''
        # Initiate Class instance
        common_model: BaseModel = BaseModel()
        # Tests
        self.assertIsNotNone(common_model.id)
        self.assertIsNotNone(common_model.created_at)
        self.assertIsNotNone(common_model.updated_at)

    def test_str(self):
        '''
        Test string representation of object
        '''
        # Initiate class instance
        common_model: BaseModel = BaseModel()
        # Test
        self.assertTrue(str(common_model).startswith('[BaseModel]'))
        self.assertIn(common_model.id, str(common_model))
        self.assertIn(str(common_model.__dict__), str(common_model))

    def test_save(self):
        '''
        Test that all necessary data are up-to-date
        '''
        # Initiate instances
        common_model: BaseModel = BaseModel()

        prev_updated_at = common_model.updated_at
        current_updated_at = common_model.save()
        # Tests
        self.assertNotEqual(prev_updated_at, current_updated_at)

    def test_todict(self):
        '''
        Test to-dict() the getter method of BaseModel
        '''
        # Initiate an instance
        common_model: BaseModel = BaseModel()
        # Convert instance to dictionary using method to_dict
        common_model_dict: Dict = common_model.to_dict()

        # Tests
        self.assertIsInstance(common_model_dict, dict)
        self.assertEqual(common_model_dict['__class__'], 'BaseModel')
        self.assertEqual(common_model_dict['id'], common_model.id)
        self.assertEqual(common_model_dict['created_at'], common_model.created_at.isoformat())
        self.assertEqual(common_model_dict['updated_at'], common_model.updated_at.isoformat())

if __name__=="__main__":
    unittest.main()
