# coding=utf-8

"""
Dummy services for testing
"""

from ws.rest.base_handler import BaseHandler
from ws.utils.oauth import authenticated, userless


class DummyHandler(BaseHandler):
    """
    """

    @userless
    def get(self):
        self.success("GET Dummy userless success")

    @userless
    def post(self):
        self.success("POST Dummy userless success")


class DummyAuthenticatedHandler(BaseHandler):
    """
    """

    @authenticated
    def get(self, user):
        self.success("GET Dummy authenticated success")

    @authenticated
    def post(self, user):
        self.success("POST Dummy authenticated success")

    @authenticated
    def delete(self, user):
        self.success("DELETE Dummy authenticated success")
