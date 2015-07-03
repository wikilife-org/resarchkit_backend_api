# coding=utf-8

import functools
from biz.services.biz_service import BizServiceException


def catch_exceptions(method):
    """Decorate RequestHandler methods with this to catch any exceptions and return an informative JSON."""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)

        except BizServiceException, bse:
            self.error(status_code=400, error=bse.message, dev_message=bse.message)


        """
        except Exception, e:
            self.error(e)
        """

    return wrapper
