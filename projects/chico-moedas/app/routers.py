import logging
from asyncio import gather

from fastapi import APIRouter, Path, Query

from app.converter import async_converter
from app.schemas import ConverterOutput

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/health-check")
def health_check():
    return {"pai": "On"}


@router.get("/converter/{from_currency}", response_model=ConverterOutput)
async def async_converter_router(
    from_currency: str = Path(max_length=3),
    to_currencies: str = Query(max_length=50),
    price: float = Query(gt=0),
):
    logger.info("start async converter")
    batch = []

    to_currencies_list = to_currencies.split(",")
    for currency in to_currencies_list:
        batch.append(
            async_converter(
                from_currency=from_currency, to_currency=currency, price=price
            )
        )

    result = await gather(*batch)
    return ConverterOutput(message="sucess", data=result)
