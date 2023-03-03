from unittest.mock import MagicMock
import pytest as pytest

from app.dao.director import DirectorDAO
from app.dao.model.director import Director
from app.service.director import DirectorService
from app.setup_db import db


@pytest.fixture
def director_dao_func():
    director = DirectorDAO(db.session)
    d1 = Director(id=1, name='Джеймс Пи Салливан')
    d2 = Director(id=2, name='Майкл Вазовски')
    d3 = Director(id=3, name='Бу')

    director.get_one = MagicMock(return_value=d1)
    director.get_all = MagicMock(return_value=[d1, d2, d3])
    director.create = MagicMock()
    director.update = MagicMock()
    director.delete = MagicMock(return_value=Director(id=2))
    return director


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_func):
        self.director_service = DirectorService(dao=director_dao_func)

    def test_get_one(self):
        director = self.director_service.get_one(2)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_data = {"name": "Снежный человек"}
        director = self.director_service.create(director_data)

        assert director.id is not None

    def test_update(self):
        director_data = {"id": 4, "name": "Генри Джей Водоног III"}
        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(1)