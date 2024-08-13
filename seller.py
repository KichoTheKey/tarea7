from ownable import Ownable
from user import User

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.set_owner(self)