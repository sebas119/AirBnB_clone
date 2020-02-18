#!/usr/bin/python3

"""
    Defines a class TestBaseModel.
"""

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
