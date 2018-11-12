#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

"""code.py"""

from wsgiref.simple_server import make_server,demo_app
from application import simple_app as app

if __name__ == '__main__':

    httpd = make_server('', 8086, app)

    sa = httpd.socket.getsockname()

    print ('http://{0}:{1}/'.format(*sa) )
