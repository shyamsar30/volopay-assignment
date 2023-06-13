from marshmallow import Schema, ValidationError, validates
from marshmallow.fields import Date, String, Integer


class TotalItemsValidator(Schema):
    start_date = Date(required=True, allow_none=False)
    end_date = Date(required=True, allow_none=False)
    department = String(required=True, allow_none=False)

class DepartmentWiseSoldItemsValidator(Schema):
    start_date = Date(required=True, allow_none=False)
    end_date = Date(required=True, allow_none=False)

class NthMostTotalItemsValidator(Schema):
    start_date = Date(required=True, allow_none=False)
    end_date = Date(required=True, allow_none=False)
    n = Integer(required=True, allow_none=False)
    item_by = String(required=True, allow_none=False)

    @validates("item_by")
    def validate_item_by(self, val, *args, **kwargs):
        if val == "quantity" or val == "price":
            pass
        else:
            raise ValidationError("Item By should one of the following: quantity || price")
        
class MonthlySalesValidator(Schema):
    year = Integer(required=True, allow_none=False)
    product = String(required=True, allow_none=False)