from .mongoengine_repository import MongoengineRepository
from .sqlalchemy_repository import SQLRepository
from ..models import MongoengineBaseUpload, SQLAlchemyModel
from ..exceptions import TusError


class Repo:
    ''' Repository factory '''

    def __init__(self, model, db):
        if isinstance(model(), MongoengineBaseUpload):
            self.__class__ = MongoengineRepository

        elif isinstance(model(), SQLAlchemyModel):
            self.__class__ = SQLRepository

        else:
            raise Exception

        self.__init__(model, db)
