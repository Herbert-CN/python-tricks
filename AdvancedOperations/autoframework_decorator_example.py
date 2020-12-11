# -*- coding:utf-8 -*-
# Author: Neal Li
# DateTime: 6/10/2020 9:02 AM
# File: exception_decorator
import functools
import os

import requests
import logging


class MyDecorator(object):

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(funcName)20s - %(message)s')

    def __init__(self, log_path=''):
        self.logger = logging.getLogger("exception_logger")
        self.logger.setLevel(logging.INFO)
        # create the logging file handler
        if log_path:
            log_file = os.path.join(log_path, 'test_log.txt')
            fh = logging.FileHandler(log_file)
        else:
            log_path = os.path.join(os.getcwd(), 'test_log')
            if not os.path.exists(log_path):
                os.mkdir(log_path)
            log_file = os.path.join(log_path, 'test_log.txt')
            fh = logging.FileHandler(log_file)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        # add handler to logger object
        self.logger.addHandler(fh)

    @staticmethod
    def log_debug(debug_info='debug'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                logging.debug("{0} - {1} - {2} - {3}".format(func.__name__, args, kwargs, debug_info))
                return func(*args, **kwargs)

            return wrapper()

        return decorator

    @staticmethod
    def log_info(log_info='info', *args, **kwargs):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*arg, **kwarg):
                logging.info("{0} - {1} - {2} - {3}".format(func.__name__, args, kwargs, log_info))
                return func(*arg, **kwarg)

            return wrapper()

        return decorator

    @staticmethod
    def log_error(error_info='error'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                logging.error("{0} - {1} - {2} - {3}".format(func.__name__, args, kwargs, error_info))
                return func(*args, **kwargs)

            return wrapper()

        return decorator

    @staticmethod
    def log_exception():
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                logging.exception("{0} - {1} - {2}".format(func.__name__, args, kwargs))
                return func(*args, **kwargs)

            return wrapper()

        return decorator

    def try_catch_exception(*args, **kwargs):
        """
        Using this decorator to catch API exception and add the message to test log
        :param args:
        :param kwargs:
        :return:
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*arg, **kwarg):
                try:
                    logging.debug("{0} - {1} - {2}".format(func.__name__, args, kwargs))
                    return func(*arg, **kwarg)
                except requests.HTTPError as http_err:
                    logging.exception(http_err)
                    raise Exception(f'HTTP error occurred: {http_err}')
                except requests.ConnectionError as conn_err:
                    logging.exception(conn_err)
                    raise Exception(f'HTTP connection error occurred: {conn_err}')
                except requests.RequestException as req_err:
                    logging.exception(req_err)
                    raise Exception(f'HTTP request error occurred: {req_err}')
                except Exception as ex:
                    logging.exception(ex)
                    raise Exception(f'Common Exception occurred: {ex}')

            return wrapper

        return decorator
