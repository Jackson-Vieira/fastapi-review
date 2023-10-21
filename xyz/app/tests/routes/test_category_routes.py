from fastapi import status
from fastapi.testclient import TestClient

from app.db.models import Category as CategoryModel
from app.main import app

client = TestClient(app)

def test_add_category_route(db_session):
    body = {
        "name": "Roupa",
        "slug": "roupa"
    }
    response  = client.post('/categories', json=body)
    assert response.status_code == status.HTTP_201_CREATED
    
    category_on_db = db_session.query(CategoryModel).all()

    assert len(category_on_db) == 1
    assert category_on_db[0].name == 'Roupa'
    assert category_on_db[0].slug == 'roupa'
    
    db_session.delete(category_on_db[0])
    db_session.commit() 

# make this better
def test_get_categories(db_session, factory_categories):
    response = client.get('/categories')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 3


def test_delete_category(db_session, factory_category):
    response = client.delete(f'/categories/{factory_category.id}')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert len(db_session.query(CategoryModel).all()) == 0

def test_delete_category_with_invalid_id(db_session, factory_category):
    response = client.delete(f'/categories/{99}')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert len(db_session.query(CategoryModel).all()) == 1
    
    db_session.delete(factory_category)
    db_session.commit()