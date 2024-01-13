#!/usr/bin/python3
"""
class base model
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    this class is blue print class
    initializes id, created_at, updated_at
    """

    def __init__(self, *args, **kwargs):
        """initialize id, created_at, updated_at"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if (key == "created_at" or key == "updated_at"):
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
        storage.new(self)
        storage.save()
