from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)
        self._collection = db["languages"]

    def to_dict(self):
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }
