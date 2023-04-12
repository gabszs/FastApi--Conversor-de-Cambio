from fastapi import APIRouter
from converter import Converter
from os import getenv

API_KEY = getenv("ALPHAVANTAGE_APIKEY")
router = APIRouter(prefix='/converter')




#url-> /converter/{from_currency}?/to_currencies=USD,JPN,GBP&price=5.19
@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: list[str], price: float):
    to_currencies = to_currencies.split(",")
    results = dict()
    converter = Converter(api_key=API_KEY)
    
    print(to_currencies)
    for currency in to_currencies:
        exchange = converter.sync_converter(from_currency=from_currency, to_currency=currency, value=price)
        results[f"${price} {from_currency} to {currency}"] = exchange

    return results


@router.get('/async/{from_currency}')
async def async_converter_router(from_currency: str, to_currencies: list[str], price: float):
    to_currencies = to_currencies.split(",")
    result = dict()

    for currency in to_currencies:
        
