#!/usr/bin/python3
"""the review clss blueprint"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the class body"""
    place_id = ""
    user_id = ""
    text = ""
