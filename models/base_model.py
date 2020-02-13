#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):

        rep = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        dict_copy = self.__dict__.copy()
        dict_copy.update(rep)
        return dict_copy
