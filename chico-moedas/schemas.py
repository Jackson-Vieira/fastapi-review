from typing import List

from pydantic import BaseModel


class ConverterOutput(BaseModel):
    message: str
    data: List[dict]