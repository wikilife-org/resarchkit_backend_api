# coding=utf-8

from dateutil.relativedelta import relativedelta
import datetime
import math
import pytz
import time


class DateUtils(object):
    
    @staticmethod
    def get_utc_datetime_str():
        date_value = datetime.datetime.now(tz=pytz.utc)
        return datetime.datetime.strftime(date_value, '%Y-%m-%d %H:%M:%S %z')
    
    @staticmethod
    def get_date(user_date):
        """
        TODO this method should not be here

        user_date: str
        Returns: date: "%Y-%m-%s" format
        """
        user_date = user_date[:19]
        date_obj = time.strptime(user_date, "%Y-%m-%d %H:%M:%S")
        date_info = time.strftime("%Y-%m-%d", date_obj)

        return date_info

    @staticmethod
    def get_time(user_date):

        """
        TODO this method should not be here

        get_time

        params:
            user_date: str

        return:
                - time: "%H:%M:%S" format.
        """
        user_date = user_date[:19]
        date_obj = time.strptime(user_date, "%Y-%m-%d %H:%M:%S")
        time_info = time.strftime("%H:%M:%S", date_obj)

        return time_info

    @staticmethod
    def create_datetime(year, month, day, hour=0, minutes=0, sec=0):
        return datetime.datetime(year, month, day, hour, minutes, sec)

    @staticmethod
    def get_zero_datetime():
        return datetime.datetime(1, 1, 1)

    @staticmethod
    def get_date_utc():
        d = DateUtils.get_datetime_utc()
        return datetime.datetime(d.year, d.month, d.day)

    @staticmethod
    def get_datetime_utc():
        return datetime.datetime.utcnow()

    @staticmethod
    def get_datetime_local(tz_name):
        return datetime.datetime.now(pytz.timezone(tz_name))

    @staticmethod
    def get_utc_offset_str(tz_name):
        return datetime.datetime.now(pytz.timezone(tz_name)).strftime('%z')

    @staticmethod
    def to_datetime_utc(local_datetime):
        """
        local_date_value: Date with TZ. Naive dates will crash.
        """
        utc_datetime = local_datetime.astimezone(pytz.utc)
        return datetime.datetime(utc_datetime.year, utc_datetime.month, utc_datetime.day, utc_datetime.hour, utc_datetime.minute, utc_datetime.second, utc_datetime.microsecond)

    @staticmethod
    def add_seconds(date_value, seconds_offset):
        """
        date_value: Date
        seconds_offset: Integer
        """
        return date_value + relativedelta(seconds=seconds_offset)

    @staticmethod
    def add_days(date_value, days_offset):
        """
        date_value: Date
        days_offset: Integer
        """
        return date_value + relativedelta(days=days_offset)

    @staticmethod
    def add_months(date_value, months_offset):
        """
        date_value: Date
        months_offset: Integer
        """
        return date_value + relativedelta(months=months_offset)

    @staticmethod
    def equals_datetime(d1, d2, sec_error=0):
        """
        d1: Date
        d2: Date
        sec_error: Float
        """
        td = d1 - d2
        return math.fabs(td.total_seconds()) <= sec_error
    
    @staticmethod
    def get_ISO_8601_date_str(date_value):
        "return YYYY-MM-DD Format"
        return datetime.datetime.strftime(date_value, '%Y-%m-%d')

    @staticmethod
    def get_ISO_8601_datetime_str(date_value):
        "return YYYY-MM-DD Format"
        return datetime.datetime.strftime(date_value, '%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def get_date_object(str_date):
        date_object = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        return date_object
