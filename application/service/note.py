from application.dao import NoteDAO


class NoteService:
    def __init__(self, dao: NoteDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        notes = self.dao.get_all()
        return notes

    def create(self, note_d):
        return self.dao.create(note_d)

    def update(self, note_d):
        self.dao.update(note_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
