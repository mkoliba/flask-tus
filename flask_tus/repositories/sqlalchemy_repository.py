import os
import uuid
import datetime

from flask import current_app

from .base_repository import BaseRepository
from ..utilities import get_extension
from ..exceptions import TusError


class SQLRepository(BaseRepository):

    def __init__(self, model, db):
        super(SQLRepository, self).__init__(model, db)

    def create(self, length, metadata):
        if length:
            length = int(length)

        path = os.path.join(
            current_app.config['TUS_UPLOAD_DIR'], str(uuid.uuid4()))

        filename = ''

        if metadata and metadata.get('filename'):
            filename = metadata.get('filename')
            path += '.' + get_extension(filename)
            del metadata['filename']


        filename = ''

        # Instantiate model
        instance = self.model(length=length, path=path,
                              filename=filename, _metadata=metadata)

        # Add and commit model to db
        self.db.session.add(instance)
        self.db.session.commit()

        return instance

    def find_by(self, **kwargs):
        return self.db.session.query(self.model).filter(**kwargs)

    def find_by_id(self, id):
        return self.db.session.query(self.model).get(id)

    def delete_expired(self):
        self.db.session.query(self.model).filter(self.model.created_on <= datetime.datetime.now(
        ) - current_app.config['TUS_TIMEDELTA']).delete()

        self.db.session.commit()
