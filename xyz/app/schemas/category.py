import re

from pydantic import BaseModel, field_validator


class Category(BaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('invalid slug')
        return value
