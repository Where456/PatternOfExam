from dao.models.note import Note


class NoteDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, rid):
        """
            Retrieves a single record from the database based on the given ID.

            Arguments:
            - rid: The ID of the record to retrieve.

            Returns:
            - An instance of the Note object corresponding to the given ID, or None if the record is not found.
        """
        return self.session.query(Note).get(rid)

    def get_all(self):
        """
            Retrieves all records from the database.

            Returns:
            - A list of Note objects representing all the records in the database.
        """
        return self.session.query(Note).all()

    def create(self, note_d):
        """
            Creates a new record in the database based on the provided data.

            Arguments:
            - note_d: A dictionary containing the data for the new note.

            Returns:
            - An instance of the Note object representing the newly created record.
        """
        ent = Note(**note_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
            Deletes a record from the database based on the provided ID.

            Arguments:
            - rid: The ID of the record to be deleted.

            Returns:
            - None
        """
        note = self.get_one(rid)
        self.session.delete(note)
        self.session.commit()

    def update(self, note_d):
        """
            Updates a record in the database based on the provided data.

            Arguments:
            - note_d: A dictionary containing the updated data for the note.

            Returns:
            - None
        """
        note = self.get_one(note_d.get("id"))
        note.text = note_d.get("text")

        self.session.add(note)
        self.session.commit()

