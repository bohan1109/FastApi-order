import pytest
from model.order import Order
from services.order_validator_impl import OrderValidatorImpl

#測試訂單驗證是否成功
def test_order_validator_success():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="1500",
        currency="TWD"
    )
    try:
        validator.validate(order)
    except ValueError:
        pytest.fail("Order validation failed unexpectedly!")

#測試訂單驗證價格格式錯誤
def test_order_validator_invalid_price():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="invalid",
        currency="TWD"
    )
    with pytest.raises(ValueError, match="Invalid price format"):
        validator.validate(order)

#測試訂單驗證不支援的貨幣
def test_order_validator_unsupported_currency():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="1500",
        currency="EUR"
    )
    with pytest.raises(ValueError, match="Currency format is wrong"):
        validator.validate(order)


#測試訂單驗證價格超過2000
def test_order_validator_price_over_limit():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="Melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="2500",
        currency="TWD"
    )
    with pytest.raises(ValueError, match="Price is over 2000"):
        validator.validate(order)

#測試訂單驗證名稱包含非英文
def test_order_validator_name_contains_non_english():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="Melody123",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="1500",
        currency="TWD"
    )
    with pytest.raises(ValueError, match="Name contains non-English characters or symbols"):
        validator.validate(order)

#測試訂單驗證名稱未大寫
def test_order_validator_name_not_capitalized():
    validator = OrderValidatorImpl()
    order = Order(
        id="A0000001",
        name="melody Holiday Inn",
        address={"city": "taipei-city", "district": "da-an-district", "street": "fuxing-south-road"},
        price="1500",
        currency="TWD"
    )
    with pytest.raises(ValueError, match="Name is not capitalized"):
        validator.validate(order)
