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
    response  = client.post('/category', json=body)
    assert response.status_code == status.HTTP_201_CREATED
    
    category_on_db = db_session.query(CategoryModel).all()

    assert len(category_on_db) == 1
    assert category_on_db[0].name == 'Roupa'
    assert category_on_db[0].slug == 'roupa'
    
    db_session.delete(category_on_db[0])
    db_session.commit() 
