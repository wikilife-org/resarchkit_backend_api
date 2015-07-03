# coding=utf-8

import functools


def authenticated(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        user = self.get_user_by_token(self.get_argument('token'))

        if not user:
            self.error(status_code=401, user_message="Authentication failed",
                        dev_message="Invalid token")
        else:
            return method(self, user=user, *args, **kwargs)
    return wrapper


def third_party_authenticated_read(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        token = self.get_argument('access_token')
        client_id = self.get_argument('client_id')
        user, client = self.get_user_by_token_and_client_id(token, client_id)

        if not user:
            self.error(status_code=401, user_message="Authentication failed",
                        dev_message="Invalid token or Client Id")
        elif not client.get("read", False):
            self.error(status_code=401, user_message="Authentication failed",
                        dev_message="No authorization to read. " +
                        "Check your app details in developers site.")
        else:
            return method(self, user=user, *args, **kwargs)
    return wrapper


def third_party_authenticated_write(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        token = self.get_argument('access_token')
        client_id = self.get_argument('client_id')
        user, client = self.get_user_by_token_and_client_id(token, client_id)

        if not user:
            self.error(status_code=401, user_message="Authentication failed",
                        dev_message="Invalid token or Client Id")
        elif not client.get("write", False):
            self.error(status_code=401, user_message="Authentication failed",
                        dev_message="No authorization to post. " +
                        "Check your app details in developers site.")
        else:
            return method(self, user=user, *args, **kwargs)
    return wrapper

def userless(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # TODO: make sure that client_id exists
        return method(self, *args, **kwargs)
    return wrapper
