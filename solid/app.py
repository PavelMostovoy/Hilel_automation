from solid.script import Order

obj = Order("Apple", 100 , 10)

obj_1 = Order("Carrot", 2, 2007896)

# obj.place_order_to_buy(300)
#
# obj.income_order(2356, 300)

print(obj.full_price() )

print(obj_1.full_price())
