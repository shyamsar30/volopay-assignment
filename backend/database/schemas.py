from backend.database.models import Data
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class DataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Data
        include_fk = True
        include_relationships = True
        load_instance = True