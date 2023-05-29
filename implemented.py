
from dao.note import NoteDAO
from service.note import NoteService
from setup_db import db

note_dao = NoteDAO(session=db.session)

note_service = NoteService(dao=note_dao)
