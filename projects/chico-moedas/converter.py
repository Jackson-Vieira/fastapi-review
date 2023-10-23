import os

import aiohttp
from fastapi import HTTPException

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

"""
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "USD",
        "2. From_Currency Name": "United States Dollar",
        "3. To_Currency Code": "JPY",
        "4. To_Currency Name": "Japanese Yen",
        "5. Exchange Rate": "149.83100000",
        "6. Last Refreshed": "2023-10-21 03:02:01",
        "7. Time Zone": "UTC",
        "8. Bid Price": "149.82770000",
        "9. Ask Price": "149.83570000"
    }
}
"""

async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_API_KEY}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)

    # Throttling error
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=500, detail='Realtime Currency not in the response')
    
    exchange_data = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    return {to_currency: exchange_data * price} 