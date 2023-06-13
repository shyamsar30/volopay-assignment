from backend.api.responses import respond
from backend.database.dao import data_dao

def get_total_items(data):
    result = data_dao.get_total_items(
        start_data=data.get('start_date'),
        end_date=data.get('end_date'),
        department=data.get('department')
    )

    if not result:
        return 0
    return result[0]