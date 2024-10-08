from ownable import Ownable
from wallet import Wallet

class User(Ownable):
    from item_manager import show_items, items_list, pick_items, show_items

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.wallet = Wallet(self)
