from flask import request
from flask_restx import Resource, Namespace

from dao.models.note import NoteSchema
from implemented import note_service

notes_ns = Namespace('notes')


@notes_ns.route('/')
class NotesView(Resource):
    def get(self):
        all_movies = note_service.get_all()
        res = NoteSchema(many=True).dump(all_movies)
        return res, 200

    def post(self):
        req_json = request.json
        note = note_service.create(req_json)
        return f"Note has been created.", 201


@notes_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        b = note_service.get_one(bid)
        sm_d = NoteSchema().dump(b)
        return sm_d, 200

    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        note = note_service.update(req_json)
        return f"Note with ID {bid} has been updated.", 204

    def delete(self, bid):
        note = note_service.delete(bid)
        return f"Note with ID {bid} has been deleted.", 204
