import pytest

from app.schemas.category import Category


def test_category_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.model_dump() == {
        "name": "Roupa",
        "slug": "roupa"
    }

def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='roupa de cama'
        )

    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='FL$'
        )

    with pytest.raises(ValueError):
        Category(
            name='Roupa',
            slug='Roupa'
        )

    
        

    # with pytest.raises(Exception):
    #     Category(
    #         name='Roupa',
    #         slug='comida'
    #     ) 

    # with pytest.raises(Exception):
    #      Category(
    #         name='Roupa',
    #         slug='Roupa'
    #     ) 
