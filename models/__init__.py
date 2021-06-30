#!/usr/bin/python3
"""
    init, import FileStorage class, asign to variable storage and reload
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
