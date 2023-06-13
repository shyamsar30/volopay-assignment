from flask import g
from sqlalchemy import extract, func


from backend.database.models import Data
from backend.database.schemas import DataSchema


db_session = None

def init_db_session(session):
    global db_session
    db_session = session

class GenericDao:
    model = None
    schema = None

class DataDao(GenericDao):
    model = Data
    schema = DataSchema

    def get_total_items(self, start_data, end_date, department):
        return g.db_session.query(
            self.model
        ).filter(
            extract('quarter', self.model.date) == 3,
            self.model.date.between(start_data, end_date),
            self.model.department == department
        ).group_by(
            extract('year', self.model.date)
        ).with_entities(
            func.sum(self.model.seats).label('tatal_count')
        ).first()

data_dao = DataDao()