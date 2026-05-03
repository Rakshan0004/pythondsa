class InventoryItem:
    """a class to demonstrate operator overloading for inventory management"""

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"


    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        else:
            raise Exception("Invalid inventory items") 

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity

    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        else:
            raise Exception("Invalid inventory items")