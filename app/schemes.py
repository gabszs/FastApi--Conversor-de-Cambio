import re
from pydantic import (BaseModel, Field, validator)
from typing import List


class ConverterBody(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @validator('to_currencies')
    def validade_to_currencies(cls, value):
        for currency in value:
            if not re.match('^[a-zA-Z]{3}$', currency):
                raise ValueError(f"Invalid Currency: {currency}")
        return value
    

class ConverterOutput(BaseModel):
    message: str
    data: List[dict]