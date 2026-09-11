class Flower:

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
            return self._petals

    def get_price(self):
            return self._price

Rose = Flower("Rose", 12, 5.99)
Tulip = Flower("Tulip", 6, 2.99)

print(f"Flower: {Rose.get_name()}")
print(f"Petals: {Rose.get_petals()}")
print(f"Price: {Rose.get_price()}")
print(f"\n")
print(f"Flower: {Tulip.get_name()}")
print(f"Petals: {Tulip.get_petals()}")
print(f"Price: {Tulip.get_price()}")