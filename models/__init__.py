#!/usr/bin/python3
"""
File that initiates an instance of file_storage
"""


from .engine.file_storage import FileStorage

# intiate FileStorage instance
storage: FileStorage = FileStorage()
# Reload
storage.reload()
