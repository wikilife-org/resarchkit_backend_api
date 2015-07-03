
from ws.rest.base_handler import BaseHandler
from ws.utils.oauth import authenticated, userless, catch_exceptions

class TasksHandler(BaseHandler):
    @userless
    @catch_exceptions
    def get(self):
        result = {}
        self.success(response=result)