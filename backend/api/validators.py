from marshmallow import Schema, ValidationError, validates
from marshmallow.fields import Date, String


class TotalItemsValidator(Schema):
    start_date = Date(required=True, allow_none=False)
    end_date = Date(required=True, allow_none=False)
    department = String(required=True, allow_none=False)