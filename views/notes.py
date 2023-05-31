from flask import request
from flask_restx import Resource, Namespace

from dao.models.note import NoteSchema
from dao.note import NoteDAO
from service.note import NoteService
from setup_db import db

notes_ns = Namespace('notes')
note_service = NoteService(dao=NoteDAO(session=db.session))



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
        note_service.update(req_json)
        return "", 204

    def delete(self, bid):
        note_service.delete(bid)
        return "", 204
