from unittest.mock import MagicMock
import pytest as pytest

from app.dao.genre import GenreDAO
from app.dao.model.genre import Genre
from app.service.genre import GenreService
from app.setup_db import db


@pytest.fixture
def genre_dao_func():
    genre = GenreDAO(db.session)
    g1 = Genre(id=1, name='Комедия')
    g2 = Genre(id=2, name='Фантастика')
    g3 = Genre(id=3, name='Фентези')

    genre.get_one = MagicMock(return_value=g2)
    genre.get_all = MagicMock(return_value=[g1, g2, g3])
    genre.create = MagicMock()
    genre.update = MagicMock()
    genre.delete = MagicMock(return_value=Genre(id=3))
    return genre


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_func):
        self.genre_service = GenreService(dao=genre_dao_func)

    def test_get_one(self):
        genre = self.genre_service.get_one(2)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_data = {"name": "Боевик"}
        genre = self.genre_service.create(genre_data)

        assert genre.id is not None

    def test_update(self):
        genre_data = {"id": 4, "name": "Триллер"}
        self.genre_service.update(genre_data)

    def test_delete(self):
        self.genre_service.delete(1)
