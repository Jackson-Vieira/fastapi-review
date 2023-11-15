import pytest
import os
from aioresponses import aioresponses
from converter import async_converter, CurrencyConverterError

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


@pytest.mark.asyncio
async def test_async_converter():
    with aioresponses() as mock_responses:
        # Mock response data
        mock_responses.get(
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=",
            payload={
                "Realtime Currency Exchange Rate": {"5. Exchange Rate": "149.83100000"}
            },
        )

        result = await async_converter("USD", "JPY", 100)
        assert result == {"JPY": 14983.10}


@pytest.mark.asyncio
async def test_async_converter_error_handling():
    with aioresponses() as mock_responses:
        # Mock an exception during the request
        mock_responses.get(
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=",
            exception=Exception("Mocked exception"),
        )

        with pytest.raises(CurrencyConverterError):
            await async_converter("USD", "JPY", 100)

        # Mock a response without "Realtime Currency Exchange Rate"
        mock_responses.get(
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=",
            payload={},
        )

        with pytest.raises(CurrencyConverterError):
            await async_converter("USD", "JPY", 100)
