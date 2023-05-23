from requests import get
from fastapi import HTTPException
from os import getenv
import aiohttp

class Converter:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def sync_converter(self, from_currency: str, to_currency: str, value: float) -> float:
        api_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={self.api_key}"

        try:
            request = get(url=api_url)
            data = request.json()
        except Exception as error:
            raise HTTPException(status_code=400, detail=data)
        
        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=400, detail=data)
         
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

        return {to_currency: exchange_rate * value}
    

    async def async_converter(self, from_currency: str, to_currency: str, value: float) -> float:
        api_url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={self.api_key}"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=api_url) as response:
                    data = await response.json()
        except Exception as error:
            raise HTTPException(status_code=400, detail=error)
        
        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=400, detail="Currency exchange rate not in the data")
         
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

        return {to_currency: exchange_rate * value}



if __name__ == "__main__":
    API_KEY = getenv("ALPHAVANTAGE_APIKEY")
    converter = Converter(api_key=API_KEY)

    data = converter.sync_converter(from_currency="BRL", to_currency="USD", value=5.5)
    print(data)





