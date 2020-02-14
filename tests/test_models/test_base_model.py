#!/usr/bin/python3
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    def test_init_id(self):

        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertNotEqual(bm1.id, bm2.id)
