#!/usr/bin/python3
"""
class base model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    this class is blue print class
    initializes id, created_at, updated_at
    """

    def __init__(self, *args, **kwargs):
        """initialize id, created_at, updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """dictionary representation of the object"""
        obj = self.__dict__.copy()
        obj["__class__"] = self.__class__.__name__
        obj["created_at"] = obj["created_at"].isoformat()
        obj["updated_at"] = obj["updated_at"].isoformat()
        return obj

    def save(self):
        """save the object"""
        self.updated_at = datetime.now()
