#!/usr/bin/python3
"""the class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """user project"""

    emai = ""
    password = ""
    first_name = ""
    last_name = ""
