from unittest.mock import MagicMock
import pytest as pytest

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.service.movie import MovieService
from app.setup_db import db


@pytest.fixture
def movie_dao_func():
    movie = MovieDAO(db.session)
    m1 = Movie(id=1, title='Кот в сапогах 2', description='...', trailer='1', year=2022, rating=9.2, genre_id=9,
               director_id=9)
    m2 = Movie(id=2, title='Чебурашка', description='...', trailer='1', year=2022, rating=9.2, genre_id=9,
               director_id=9)
    m3 = Movie(id=3, title='Аватар 2: Путь воды', description='...', trailer='1', year=2022, rating=9.1, genre_id=9,
               director_id=9)

    movie.get_one = MagicMock(return_value=m3)
    movie.get_all = MagicMock(return_value=[m1, m2, m3])
    movie.create = MagicMock()
    movie.update = MagicMock()
    movie.delete = MagicMock(return_value=Movie(id=3))
    return movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_func):
        self.movie_service = MovieService(dao=movie_dao_func)

    def test_get_one(self):
        movie = self.movie_service.get_one(3)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {"name": "Человек-паук: Нет пути"}
        movie = self.movie_service.create(movie_data)

        assert movie.id is not None

    def test_update(self):
        movie_data = {"id": 4, "name": "1+1"}
        self.movie_service.update(movie_data)

    def test_delete(self):
        self.movie_service.delete(2)
