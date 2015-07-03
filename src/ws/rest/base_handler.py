# coding=utf-8

import tornado
from tornado.web import RequestHandler
from utils.parsers.json_parser import JSONParser
from utils.parsers.date_parser import DateParser


class BaseHandler(RequestHandler):

    _logger = None
    _services = None

    def initialize(self, services):
        RequestHandler.initialize(self)
        #super(BaseHandler, self).initialize()
        self._logger = self.settings['logger']
        self._services = services

    def get_user_by_token(self, token):
        return self._services["user"].get_user_by_token(token)

    def get_user_by_token_and_client_id(self, token, client_id):
        return self._services["user"].\
            get_user_by_token_and_client_id(token, client_id)
    
    def set_default_headers(self):
        self.set_header("Server", "MoodsyAPI tornado/{}".\
                        format(tornado.version))
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods",\
                         "GET,PUT,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Max-Age", 86400)

    def get_source(self, headers):
        source = "client.unknown"

        if "User-Agent" in headers:
            user_agent = str(headers["User-Agent"]).lower()
        else:
            source = "client.other: %s" % user_agent

        return source

    def sanitize_raw_data(self, raw_data):
        tmp = str(raw_data).replace('\\"', '')
        return str(tmp).replace("\\", "")

    def _json(self, status_code, message, data):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        response = JSONParser.to_json({"status": status_code,
                                       "message": message, "data": data})
        self.write(response)

    def get_params(self):
        arguments = self.request.arguments
        params = {}
        for key in arguments:
            params[key] = arguments[key][0]

        return params

    def get_str_params(self):
        arguments = self.request.arguments
        params = {}
        for key in arguments:
            params[key] = str(arguments[key][0])

        return params

    def get_date_param(self, name, required=False):
        if required:
            param = self.get_argument(name, strip=True)
        else:
            param = self.get_argument(name, default=None, strip=True)

        return DateParser.from_date(param) if param else None

    def success(self, response=None, status_code=200, user_message=None,
                 dev_message=None):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        if user_message is not None:
            self.set_header("X-User-Message", user_message)
        if dev_message is not None:
            self.set_header("X-Dev-Message", dev_message)
        self.write(JSONParser.to_json(response))

    def error(self, error="", user_message=None,
               dev_message=None, status_code=500):
        self._logger.error(error)

        if user_message is not None:
            self.set_header("X-User-Message", user_message)
        if dev_message is not None:
            self.set_header("X-Dev-Message", dev_message)
        self.set_status(status_code)

    def _on_response(self, result, error):
        if error:
           self.error(error=error)
        else:
            self.success(response=result)
        self.finish()