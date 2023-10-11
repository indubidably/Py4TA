from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///films_db.db")
Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


Base.metadata.create_all(engine)


