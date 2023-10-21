import pytest

from app.db.connection import Session
from app.db.models import Category as CategoryModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture
def factory_categories(db_session):
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


@pytest.fixture
def factory_category(db_session):
    category = CategoryModel(name="Test", slug="test")
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)
    yield category