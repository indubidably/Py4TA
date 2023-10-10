from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///films_db.db")
Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

film1 = Film(title="Mars of Destruction", director="Johnson", release_year=2020)
film2 = Film(title="The Madagascar Escape", director="Schrodinger", release_year=2018)
film3 = Film(title="Oktoberfest", director="Mikael Gustafson", release_year=2022)

session.add_all([film1, film2, film3])
session.commit()

film_to_update = session.query(Film).filter_by(title="Mars of Destruction").first()
if film_to_update:
    film_to_update.release_year = 2021
    session.commit()

films = session.query(Film).all()
for film in films:
    print(f"Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}")

session.query(Film).delete()
session.commit()

session.close()
