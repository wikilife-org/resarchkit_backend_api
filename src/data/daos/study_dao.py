# coding=utf-8

from data.daos.base_dao import BaseDAO
from pymongo import DESCENDING, ASCENDING
from bson.objectid import ObjectId


class StudyDaoException(Exception):
    pass


class StudyDAO():

    _collection = None

    def _initialize(self):
        self._collection = self._db.study
        self._collection.ensure_index([("created_datetime", DESCENDING)])

    def get(self, study_id):
        return self._collection.findOne({"id": ObjectId(study_id)})