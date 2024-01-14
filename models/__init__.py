#!/usr/bin/python3
"""set up storage"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
