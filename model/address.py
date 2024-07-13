from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str = Field(...)  
    district: str = Field(...)  
    street: str = Field(...)  