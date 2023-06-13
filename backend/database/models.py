from sqlalchemy import Column, Integer, String, DateTime


from .connector import Base, db_engine


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    user = Column(String)
    department = Column(String)
    software = Column(String)
    seats = Column(Integer)
    amount = Column(Integer)

# Create all the tables in database
if __name__ == "__main__":
    Base.metadata.create_all(db_engine)