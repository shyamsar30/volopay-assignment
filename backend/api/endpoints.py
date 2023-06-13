from flask import request
from flask_restx import Namespace, Resource, fields

from backend.api.validators import NthMostTotalItemsValidator, TotalItemsValidator
from backend.api.views import get_total_items, get_nth_most_total_item


namespace = Namespace("My Namespace", "All Data", path="")

@namespace.route("/total_items")
class TotalItemsView(Resource):
    POST_DOC_MODEL = namespace.model(
        "TotalItemsInQ3",
        {
            "start_date": fields.String(example="2022-2-23", description="Starting Date"),
            "end_date": fields.String(example="2022-12-26", description="Ending Date"),
            "department": fields.String(example="Marketting", description="Department Name as in data")
        }
    )

    @namespace.expect(POST_DOC_MODEL)
    def post(self):
        """
        Total item (total seats) sold in <Department> for last in q3 of the year.
        """
        validated_json = TotalItemsValidator().load(request.json)
        return get_total_items(validated_json)
    

@namespace.route("/nth_most_total_item")
class NthMostTotalItemView(Resource):
    POST_DOC_MODEL = namespace.model(
        "NthMostTotalItems",
        {
            "start_date": fields.String(example="2022-2-23", description="Starting Date"),
            "end_date": fields.String(example="2022-12-26", description="Ending Date"),
            "n": fields.Integer(example="2", description="Nth Most Total Item"),
            "item_by": fields.String(example="quantity || price", description="Filter by quantity or price")
        }
    )

    @namespace.expect(POST_DOC_MODEL)
    def post(self):
        """
        Total item (total seats) sold in <Department> for last in q3 of the year.
        """
        validated_json = NthMostTotalItemsValidator().load(request.json)
        return get_nth_most_total_item(validated_json)
