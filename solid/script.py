from random import randint


class Order:

    def __init__(self, name, price, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    def full_price(self):
        return self.quantity * self.price


class Place_order:

    def __init__(self, obj: Order):
        self.name = obj.name
        self.price = obj.price

    def place_order_to_buy(self, quantity):
        self.order = randint(999, 9999)
        print(f"order placed to shop with number {self.order}")


class PlaceOrderPaypal(Place_order):

        def __init__(self, obj: Order):
            super().__init__(obj)

        def place_order_to_buy_pypal(self, quantity, type):
            self.order = randint(999, 9999)
            print(f"order placed to shop with number {self.order}"
                  f"by type{type}")



class Income_order:

    def __init__(self, obj: Order):
        self.name = obj.name
        self.price = obj.price
        self.quantity = obj.quantity

    def income_order(self, order_number: int, quantity: int):
        temp = quantity
        self.quantity += quantity
        print(
                f"added {temp} by numbrt{order_number} and result = "
                f"{self.quantity}")
