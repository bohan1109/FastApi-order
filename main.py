from typing import Union
from model.order import Order
from fastapi import FastAPI, HTTPException, Depends
from interfaces.order_validator import OrderValidator
from interfaces.order_converter import OrderConverter
from dependencies import get_order_validator, get_order_converter

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/orders")
async def create_order(
    order: Order,
    order_validator: OrderValidator = Depends(get_order_validator),
    order_converter: OrderConverter = Depends(get_order_converter),
):
    try:
        order_validator.validate(order)
        converted_order = order_converter.convert(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Order processed successfully", "order": converted_order}
