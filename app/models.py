# app/models.py
class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Patient:
    def __init__(self, id, name,details):
        self.id = id
        self.name = name
        self.details = details
