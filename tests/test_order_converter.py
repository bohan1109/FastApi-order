import pytest
from model.order import Order
from services.order_converter_impl import OrderConverterImpl

#測試轉換後的價格是否超過2000
def test_order_converter_usd_to_twd_exceed_limit():
    converter = OrderConverterImpl()
    order = Order(
        id="A0000002",
        name="Expensive Item",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="100", 
        currency="USD"
    )
    with pytest.raises(ValueError, match="Converted price is over 2000"):
        converter.convert(order)

#測試轉換後的價格是否正確
def test_order_converter_usd_to_twd():
    converter = OrderConverterImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="60", 
        currency="USD"
    )
    converted_order = converter.convert(order)
    assert converted_order["order_price"] == 60 * 31
    assert converted_order["order_currency"] == "TWD"

#測試轉換後的價格是否正確
def test_order_converter_twd():
    converter = OrderConverterImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="1500",
        currency="TWD"
    )
    converted_order = converter.convert(order)
    assert converted_order["order_price"] == 1500
    assert converted_order["order_currency"] == "TWD"
