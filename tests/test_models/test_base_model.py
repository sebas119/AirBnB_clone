#!/usr/bin/python3

"""
    Defines a class TestBaseModel.
"""

import models
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Represent a TestBaseModel."""

    def setUp(self):
        """SetUp method"""

        self.base_model = BaseModel()
        self.base_model.data = "Test data"

    def TearDown(self):
        """TearDown method."""

        del self.base_model

    def test_init_id(self):
        """Test different id per object created"""

        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, self.base_model.id)

    def test_copy_object(self):
        """Copy an object with the kwargs init from BaseModel"""

        my_model_dict = self.base_model.to_dict()
        bm1 = BaseModel(**my_model_dict)
        self.assertEqual(bm1.id, self.base_model.id)

    def test_id_type(self):
        """Test the id type from BaseModel"""

        self.assertIsInstance(self.base_model.id, str)

    def test_docstring(self):

        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def test_mod_to_dict(self):
        """Test dictionary representation in BaseModel"""

        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_type_object(self):
        """Test type object of BaseModel"""

        self.assertEqual(
            str(type(self.base_model)),
            "<class 'models.base_model.BaseModel'>")
