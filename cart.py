from ownable import Ownable

class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items
    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = [item.price for item in self.items]
        return sum(price_list) 

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("No tienes suficiente saldo para completar la compra.")
            return

        for item in self.items:
            self.owner.wallet.withdraw(item.price)
            item.owner.wallet.deposit(item.price)
            
            item.set_owner(self.owner)
        
        self.items.clear()

        print("Compra realizada con éxito.")
