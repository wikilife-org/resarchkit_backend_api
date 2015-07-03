# coding=utf-8

from ws.rest.authorization import SignUpHandler, SignInHandler, ConsentHandler
from ws.rest.tasks import TasksHandler
from ws.rest.dummy import DummyHandler

import tornado.web



def setup_app(settings):
    # intialize tornado instance

    routes = []
    routes.append(('/1/dummy/', DummyHandler))
    routes.append(('/api/v1/auth/signUp/', SignUpHandler))
    routes.append(('/api/v1/auth/signIn/', SignInHandler))
    routes.append(('/api/v1/consent/', ConsentHandler))
    routes.append(('/api/v1/tasks/', TasksHandler))

    settings["TORNADO"]['logger'] = settings["LOGGER"]
    app = tornado.web.Application(routes, **settings["TORNADO"])

    return app
