import os
from typing import Dict
from aiohttp import ClientSession


class CurrencyConverter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        return cls._instance

    async def fetch_response_data(self, from_currency: str, to_currency: str) -> Dict:
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey="
        try:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
        except Exception as error:
            raise CurrencyConverterError(detail=str(error))

        # Throttling error
        if "Realtime Currency Exchange Rate" not in data:
            raise CurrencyConverterError(detail="Realtime Currency not in the response")

        return data

    def get_exchange_data(self, data) -> float:
        return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    def convert_to_currency(self, to_currency, exchange_data, price) -> Dict:
        """
        @return to currency final value rounded with two decimal places
        """
        return {to_currency: round(exchange_data * price, 2)}


class CurrencyConverterError(Exception):
    def __init__(
        self, status_code: int = 400, detail: str = "Currency conversion error"
    ):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code)


async def async_converter(from_currency: str, to_currency: str, price: float):
    converter = CurrencyConverter()
    data = await converter.fetch_response_data(from_currency, to_currency)
    return converter.convert_to_currency(
        to_currency, converter.get_exchange_data(data), price
    )
