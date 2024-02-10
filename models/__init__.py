#!/usr/bin/python3
"""
In this file we will create an instance of FileStorage and use it\
in our BaseModels class
"""


from .engine.file_storage import FileStorage


# Initiate FileStorage  object to interact with the file system
storage: FileStorage = FileStorage()
# Use reload method
storage.reload()


