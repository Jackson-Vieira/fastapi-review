from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.routes.deps import get_db_session
from app.schemas.category import Category
from app.use_cases.category import CategoryUseCases

router = APIRouter()

@router.post('/category')
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session)
    uc.create_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)