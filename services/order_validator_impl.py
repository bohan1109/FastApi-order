from interfaces.order_validator import OrderValidator
from model.order import Order
import re

class OrderValidatorImpl(OrderValidator):
    def validate(self, order: Order):
        if order.currency not in ["TWD", "USD"]:
            raise ValueError("Currency format is wrong")
        
        if not order.price.isdigit():
            raise ValueError("Invalid price format")
        
        price = int(order.price)
        if price > 2000:
            raise ValueError("Price is over 2000")
        
        if not re.match("^[A-Za-z ]+$", order.name):
            raise ValueError("Name contains non-English characters or symbols")
        
        if not order.name[0].isupper():
            raise ValueError("Name is not capitalized")
