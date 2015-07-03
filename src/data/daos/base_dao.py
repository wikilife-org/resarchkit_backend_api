# coding=utf-8
from bson.objectid import ObjectId


class BaseDAO(object):

    _logger = None
    _db = None

    def __init__(self, logger, db):
        self._logger = logger
        self._db = db
        self._initialize()

    #protected
    def _initialize(self):
        pass

    def get_db(self):
        return self._db

    def get_logger(self):
        return self._logger

    def _get_object_id(self, str_id):
        try:
            return ObjectId(str_id)
        except:
            return None

    def _str_id(self, item, id_field="id", del__id=False):
        """
        Add String "id" to item
        """
        if not item:
            return None

        item[id_field] = str(item["_id"])

        if del__id:
            del item["_id"]

        return item
    