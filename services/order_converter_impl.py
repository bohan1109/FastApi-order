from interfaces.order_converter import OrderConverter
from model.order import Order

class OrderConverterImpl(OrderConverter):
    def convert(self, order: Order):
        if order.currency == "USD":
            converted_price = int(order.price) * 31
            if converted_price > 2000:
                raise ValueError("Converted price is over 2000")
            order.price = converted_price
            order.currency = "TWD"
        else:
            order.price = int(order.price)
        
        return {
            "order_id": order.id,
            "order_name": order.name,
            "order_address": order.address,
            "order_price": order.price,
            "order_currency": order.currency
        }
