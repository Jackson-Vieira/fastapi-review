from sqlalchemy.orm import Session

from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput


class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_sesion = db_session

    def create_category(self, category: Category):
        category_model = CategoryModel(**category.model_dump())
        self.db_sesion.add(category_model)
        self.db_sesion.commit()
    
    def get_all(self):
        categories_on_db = self.db_sesion.query(CategoryModel).all()
        return [self.serialize_category(category) for category in categories_on_db]
    
    def serialize_category(self, category_model: CategoryModel):
        return CategoryOutput(**category_model.__dict__) 