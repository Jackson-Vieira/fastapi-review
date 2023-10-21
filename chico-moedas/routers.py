from asyncio import gather

from fastapi import APIRouter

from converter import async_converter, sync_converter

router = APIRouter(prefix='/converter')

# path param
# router.get('/convert/from_currency')

# query param 
# only add in functions params

#/converter/?to_currencies=USD,EUR&price=5.55

@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):

    result = {
        from_currency: {}
    }

    to_currencies = to_currencies.split(",")
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result[from_currency][currency] = response

    return result

@router.get('/async/{from_currency}')
async def async_converter_router(from_currency: str, to_currencies: str, price: float):
    batch = []
    result = {
        from_currency: {}
    }

    async def xyz(from_currency, to_currency, price):
        result = await async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        return to_currency, result

    to_currencies = to_currencies.split(",")
    for currency in to_currencies:
        batch.append(xyz(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        ))

    result[from_currency] = { to_currency:value for to_currency, value in await gather(*batch) }
    return result