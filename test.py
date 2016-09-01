#coding=utf8
import sys, os

import time

from base import UA,UserAgent

def parse_line(line):
    sections = line.split(';')
    os = dict(map(lambda v: v.split('=', 1), sections[0].split(',')))
    engine = dict(map(lambda v: v.split('=', 1), sections[1].split(',')))
    browser = dict(map(lambda v: v.split('=', 1), sections[2].split(',')))
    device = dict(map(lambda v: v.split('=', 1), sections[3].split(',')))

    ua = UserAgent()
    ua.set_os(os)
    ua.set_engine(engine)
    ua.set_browser(browser)
    ua.set_device(device)
    return ua

def run():
    stime = time.time()
    ua = UA('')
    ua1 = None
    ua2 = None

    total = 0
    failures = 0
    with open('resources/ua_test_input') as stream:
        for (index, line) in enumerate(stream):
            if index % 2 == 0:
                ua.ua = line.strip('\n')
                ua1 = ua.detect()
            else:
                ua2 = parse_line(line.strip('\n'))
                try:
                    assert ua1.equals(ua2)
                except AssertionError, e:
                    print ua.ua
                    print 'detected: ', ua1
                    print 'right: ', ua2
                    failures += 1
                    break
                finally:
                    ua1 = None
                    ua2 = None
                    ua.reset()
                    total += 1

    print 'total %d case, failures %d' % (total, failures)

    etime = time.time()
    print 'total spent %dms' % ((int(etime - stime))*1000)

def single():
    useragent = 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-CN; GT-I9070 Build/GINGERBREAD) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.634 U3/0.8.0 Mobile Safari/534.30'

    #print parse_line('name=Android,version=4.1;name=WebKit,version=534.3;name=,version=,mode=;model=8190,type=mobile,manufacturer=Coolpad')
    print UA(useragent).detect()

if __name__ == '__main__':
    #single()
    run()
