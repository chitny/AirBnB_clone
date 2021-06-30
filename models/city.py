#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        Creates a class named City that
        inherits from BaseModel
    """

    state_id = ""
    name = ""
