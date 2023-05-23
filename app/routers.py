from fastapi import APIRouter, Path, Query
from asyncio import gather
from converter import Converter
from os import getenv
from schemes import ConverterBody, ConverterOutput

API_KEY = getenv("ALPHAVANTAGE_APIKEY")
router = APIRouter(prefix='/converter')


#url-> /converter/{from_currency}?to_currencies=USD,JPN,GBP&price=5.19
@router.get('/{from_currency}')
def converter(
    from_currency: str = Path(max_length=3, regex='^[a-zA-Z]{3}$'),
    to_currencies: str = Query(max_length=50, regex='^[a-zA-Z]{3}(,[a-zA-Z]{3})*$'),
    price: float = Query(gt=0)
) -> dict:
    """
    Path parameter named from_currency: It represents the currency code (3 letters) to be converted. This parameter is required.

    Query parameter named to_currencies: It represents a comma-separated list of currency codes (3 letters) to which the from_currency should be converted. This parameter is required.

    Query parameter named price: It represents the amount of money to be converted. This parameter is required.

    Path parameter named to_currency: It represents the currency code (3 letters) to which the from_currency should be converted. This parameter is required.

    Description for from_currency: This parameter represents the currency code that the user wants to convert. It must be a 3-letter code that identifies a currency. This code can be in lowercase or uppercase and must not contain any numbers.

    Description for to_currency: This parameter represents the currency code that the user wants to convert the from_currency into. It must be a 3-letter code that identifies a currency. This code can be in lowercase or uppercase and must not contain any numbers.\
    """
    
    from_currency = from_currency.upper()
    to_currencies = to_currencies.upper().split(",")
    print(to_currencies)

    results = {"message": "success", "data": list()}
    converter = Converter(api_key=API_KEY)
    
    for currency in to_currencies:
        exchange = converter.sync_converter(from_currency=from_currency, to_currency=currency, value=price)
        # results[f"${price} {from_currency} to {currency}"] = exchange
        results["data"].append(exchange)

    return results


@router.get('/async/{from_currency}')
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex='^[a-zA-Z]{3}$'),
    to_currencies: str = Query(max_length=50, regex='^[a-zA-Z]{3}(,[a-zA-Z]{3})*$'),
    price: float = Query(gt=0)
) :
    """
    Path parameter named from_currency: It represents the currency code (3 letters) to be converted. This parameter is required.

    Query parameter named to_currencies: It represents a comma-separated list of currency codes (3 letters) to which the from_currency should be converted. This parameter is required.

    Query parameter named price: It represents the amount of money to be converted. This parameter is required.

    Path parameter named to_currency: It represents the currency code (3 letters) to which the from_currency should be converted. This parameter is required.

    Description for from_currency: This parameter represents the currency code that the user wants to convert. It must be a 3-letter code that identifies a currency. This code can be in lowercase or uppercase and must not contain any numbers.

    Description for to_currency: This parameter represents the currency code that the user wants to convert the from_currency into. It must be a 3-letter code that identifies a currency. This code can be in lowercase or uppercase and must not contain any numbers.\
    """
    
    from_currency = from_currency.upper()
    to_currencies = to_currencies.split(",")
    converter = Converter(api_key=API_KEY)
    corroutines = list()
    result = dict()

    for currency in to_currencies:
        coro = converter.async_converter(from_currency=from_currency, to_currency=currency, value=price)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    result = {f"${price} {from_currency} to {currency}": gather_result[count] for count, currency in enumerate(to_currencies)}

    return result



@router.post('/async/v2/{from_currency}', response_model=ConverterOutput)
async def async_v2_converter_router(
    body: ConverterBody,
    from_currency: str = Path(max_length=3, regex='^[a-zA-Z]{3}$'),
):
    """
    This function is an async HTTP POST endpoint that receives a JSON payload body with the fields price and to_currencies, and a string from_currency that represents the source currency for the conversion.

    The price field represents the amount to be converted, and to_currencies is a list of strings that contains the target currencies for the conversion, represented as 3-letter codes (e.g. "USD").

    The function uses the Converter class to perform the currency conversion asynchronously for each currency in to_currencies, and returns a JSON response with the results in a list of dictionaries.
    """
    
    from_currency = from_currency.upper()

    to_currencies = body.to_currencies
    price = body.price
    
    converter = Converter(api_key=API_KEY)
    
    corroutines = list()
    result = dict()

    for currency in to_currencies:
        currency = currency.upper()
        coro = converter.async_converter(from_currency=from_currency, to_currency=currency, value=price)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    result = {f"${price} {from_currency} to {currency}": gather_result[count] for count, currency in enumerate(to_currencies)}

    return ConverterOutput(
        message="Success",
        data=gather_result
    )