import os
from fastapi.testclient import TestClient

from app.main import app

from aioresponses import aioresponses

client = TestClient(app)

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def test_converter_route_sucess_state():
    with aioresponses() as m:
        m.get(
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=",
            payload={
                "Realtime Currency Exchange Rate": {"5. Exchange Rate": "149.83100000"}
            },
        )

        response = client.get("/converter/USD?to_currencies=JPY&price=100")
        data = response.json()
        assert response.status_code == 200
        assert data["message"] == "sucess"
        assert data["data"][0]["JPY"] == 14983.10
