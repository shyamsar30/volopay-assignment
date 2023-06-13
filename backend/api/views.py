from backend.api.responses import respond
from backend.database.dao import data_dao

def get_total_items(data):
    result = data_dao.get_total_items(
        start_date=data.get('start_date'),
        end_date=data.get('end_date'),
        department=data.get('department')
    )

    if not result:
        return 0
    return result[0]

def get_nth_most_total_item(data):

    item_by = data.get('item_by')

    if item_by == 'quantity':
        result = data_dao.get_nth_most_sold_item_by_quantity(
            start_date=data.get('start_date'),
            end_date=data.get('end_date')
        )

        n = data.get('n')

        if not result or len(result) < n - 1:
            return "NO FOUND"

        return result[n-1][1]
    
    else:
        result = data_dao.get_nth_most_sold_item_by_price(
            start_date=data.get('start_date'),
            end_date=data.get('end_date')
        )

        n = data.get('n')

        if not result or len(result) < n - 1:
            return "NO FOUND"

        return result[n-1][1]
    

def get_department_wise_sold_items(data):
    result = data_dao.get_department_wise_sold_items(
        start_date=data.get('start_date'),
        end_date=data.get('end_date')
    )

    response = {}

    for data in result:
        response[data.department] = "%.2f" % data.percentage

    return respond(200, "Success", payload=response)