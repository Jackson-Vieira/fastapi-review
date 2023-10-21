from fastapi import APIRouter

router = APIRouter()

# path param
# router.get('/convert/from_currency')

# query param 
# only add in functions params

@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    return True