from flask import g
from sqlalchemy import extract, func, desc, text


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

    def get_total_items(self, start_date, end_date, department):
        return g.db_session.query(
            self.model
        ).filter(
            self.model.date.between(start_date, end_date),
            self.model.department == department
        ).with_entities(
            func.sum(self.model.seats).label('total_count')
        ).first()
    
    def get_nth_most_sold_item_by_quantity(self, start_date, end_date):
        return g.db_session.query(
            self.model
        ).filter(
            self.model.date.between(start_date, end_date)
        ).group_by(
            self.model.software
        ).with_entities(
            func.sum(self.model.seats).label('total_count'),
            self.model.software
        ).order_by(
            desc(text('total_count'))
        ).all()
    
    def get_nth_most_sold_item_by_price(self, start_date, end_date):
        return g.db_session.query(
            self.model
        ).filter(
            self.model.date.between(start_date, end_date)
        ).group_by(
            self.model.software
        ).with_entities(
            func.sum(self.model.amount).label('total_count'),
            self.model.software
        ).order_by(
            desc(text('total_count'))
        ).all()
    
    def get_department_wise_sold_items(self, start_date, end_date):

        sum = g.db_session.query(func.sum(self.model.seats)).scalar()

        return g.db_session.query(
            self.model
        ).with_entities(
            self.model.department,
            (func.sum(self.model.seats) * 100.0 / sum)
            .label('percentage')
        ).group_by(self.model.department).all()

data_dao = DataDao()