import pytest
from sqlalchemy.orm import Session

from app.db.models import Category as CategoryModel
from app.errors.category import CategoryNotFoundError
from app.schemas.category import Category, CategoryOutput
from app.use_cases.category import CategoryUseCases


@pytest.fixture
def factory_categories(db_session: Session):
    categories = [
            CategoryModel(name='Roupa', slug='roupa'),
            CategoryModel(name='Carro', slug='carro'),
            CategoryModel(name='Comida', slug='comida')
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()


def test_create_category_uc(db_session):
    uc = CategoryUseCases(db_session)

    category = Category(
        name='Roupa',
        slug='roupa'
    )

    uc.create_category(
        category=category
    )

    category_on_db = db_session.query(CategoryModel).all()

    assert len(category_on_db) == 1
    assert category_on_db[0].name == 'Roupa'
    assert category_on_db[0].slug == 'roupa'

    db_session.delete(category_on_db[0])
    db_session.commit()

def test_list_categories_uc(db_session, factory_categories):
    uc = CategoryUseCases(db_session)

    categories = uc.get_all()
    
    assert len(categories) == 3
    assert type(categories[0]) == CategoryOutput
    assert categories[0].name == factory_categories[0].name

def test_delete_category_uc(db_session, factory_categories):
    uc = CategoryUseCases(db_session)

    category = Category(
        name="Category test",
        slug="category-test"
    )

    category_on_db = uc.create_category(category)
    uc.delete_by_id(category_on_db.id)

    assert len(factory_categories) == 3

    categories_on_db = db_session.query(CategoryModel).all() 

    assert len(categories_on_db) == 3
    assert categories_on_db[-1].name == factory_categories[-1].name


def test_delete_with_invalid_category_id(db_session, factory_categories):
    uc = CategoryUseCases(db_session)

    with pytest.raises(CategoryNotFoundError):
        uc.delete_by_id(99)