from abc import ABC 
# create an abstract base class from where other class can inherit 
class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
