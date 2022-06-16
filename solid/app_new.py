from solid.script import Order, Place_order, PlaceOrderPaypal

obj = Order("calculator", 20, 500)

payment = Place_order(obj)

print(payment.price)

payment.place_order_to_buy(20)

pay_pal = PlaceOrderPaypal(obj)

pay_pal.place_order_to_buy(37)

pay_pal.place_order_to_buy_pypal(45, "e-mail")