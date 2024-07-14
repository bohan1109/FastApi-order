from pydantic import BaseModel, Field
from model.address import Address

class Order(BaseModel):
    id: str = Field(...)  
    name: str = Field(...)  
    address: Address
    price: str = Field(...)  
    currency: str = Field(...)  