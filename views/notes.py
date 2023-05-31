from flask import request
from flask_restx import Resource, Namespace

from dao.models.note import NoteSchema
from implemented import note_service

notes_schema = NoteSchema(many=True)
note_schema = NoteSchema()
notes_ns = Namespace('notes')


@notes_ns.route('/')
class NotesView(Resource):
    def get(self):
        notes = note_service.get_all()
        return notes_schema.dump(notes), 200

    def post(self):
        req_json = request.json
        note = note_service.create(req_json)
        return f"Note has been created.", 201, {"location": f"/notes/{note.id}"}



@notes_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        note = note_service.get_one(bid)
        return note_schema.dump(note), 200

    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        note_service.update(req_json)
        return "", 204

    def delete(self, bid):
        note_service.delete(bid)
        return "", 204
