from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.errors.category import CategoryNotFoundError
from app.routes.deps import get_db_session
from app.schemas.category import Category
from app.use_cases.category import CategoryUseCases

router = APIRouter()

@router.post('/categories')
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session)
    uc.create_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/categories')
def list_categories(
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session)
    response = uc.get_all()
    return response

@router.delete('/categories/{category_id}')
def delete_category(
        category_id: int,
        db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session)
    try:
        uc.delete_by_id(category_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    # improve this with HTTPException
    except CategoryNotFoundError: 
        return Response(status_code=status.HTTP_404_NOT_FOUND)