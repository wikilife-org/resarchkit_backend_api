# coding=utf-8

from datetime import datetime
import dateutil.parser
import time


class DateParser(object):

    @staticmethod
    def from_datetime_utc(str_value):
        return DateParser.from_datetime(str_value)

    @staticmethod
    def from_datetime(str_value):
        """
        str_value: String formatted datetime
        Returns: Date
        """
        return dateutil.parser.parse(str_value)

    @staticmethod
    def from_timestamp(str_value):
        """
        str_value: String number
        Returns: Date
        """
        return datetime.fromtimestamp(int(str_value))

    @staticmethod
    def from_date(str_value):
        struct = time.strptime(str_value, "%Y-%m-%d")
        dt = datetime.fromtimestamp(time.mktime(struct))
        return dt

    @staticmethod
    def from_time(str_value):
        pass
