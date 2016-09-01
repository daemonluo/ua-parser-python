#coding=utf8
from base import UA

__name__ = 'ua'

def detect(ua_string):
    ua = UA(ua_string).detect()
    return ua
