# coding=utf-8

from data.daos.base_dao import BaseDAO
from pymongo import DESCENDING, ASCENDING
from bson.objectid import ObjectId


class UserDAOException(Exception):
    pass


class UserDAO():

    _collection = None

    def _initialize(self):
        self._collection = self._db.users
        self._collection.ensure_index([("studies.created_datetime", DESCENDING)])
        self._collection.ensure_index([("studies.username", DESCENDING)])
        self._collection.ensure_index([("studies.id", DESCENDING)])
        self._collection.ensure_index([("email", DESCENDING)])

    def count_users_in_study(self, study_id):
        return self._collection.find({"studies.id":study_id}).count()

    def create(self, username, email, password, study, created_datetime):
        user = {"email":email, "studies":[ {"username": username, "password":password, "id":study, "created_datetime": created_datetime} ]}
        self._collection.save(user)
        return self._collection.find_one({"email", email})
    
    def get_user_by_username(self, username):
        return self._collection.find({"studies.username": username})
    
    def get_user_by_email(self, email):
        return self._collection.find_one({"email": email})
    
    def save(self, userDTO):
        self._collection.save(userDTO)