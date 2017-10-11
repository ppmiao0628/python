# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from webhello import application

httpd = make_server('', 9097, application)
print('server on port 9097...')
httpd.serve_forever()
