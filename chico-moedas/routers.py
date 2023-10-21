from fastapi import APIRouter

from converter import sync_converter

router = APIRouter()

# path param
# router.get('/convert/from_currency')

# query param 
# only add in functions params

#/converter/?to_currencies=USD,EUR&price=5.55

@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")

    result = {
        from_currency: {}
    }

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result[from_currency][currency] = response

    return result