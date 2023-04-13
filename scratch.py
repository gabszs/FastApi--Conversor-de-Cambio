dct = {'Realtime Currency Exchange Rate': {'1. From_Currency Code': 'BRL', '2. From_Currency Name': 'Brazilian Real', '3. To_Currency Code': 'USD', '4. To_Currency Name': 'United States Dollar', '5. Exchange Rate': '0.20231448', '6. Last Refreshed': '2023-04-12 19:25:22', '7. Time Zone': 'UTC', '8. Bid Price': '0.20230760', '9. Ask Price': '0.20231535'}}

print(dct.get('2. From_Currency Name'))



testelist = "a,b,c,d"
testelist = testelist.upper().split(",")
print(testelist)


from pydantic import BaseModel, Field, validator
from typing import List

class ConverterBody(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]