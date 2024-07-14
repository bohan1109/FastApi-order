from services.order_validator_impl import OrderValidatorImpl
from services.order_converter_impl import OrderConverterImpl

def get_order_validator() -> OrderValidatorImpl:
    return OrderValidatorImpl()

def get_order_converter() -> OrderConverterImpl:
    return OrderConverterImpl()
