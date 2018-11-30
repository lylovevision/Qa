# -*- coding: utf-8 -*-
import os 
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from django.core.wsgi import get_wsgi_application

'''
tornado是优秀的Web故武器框架，这篇代码是让django使用tornado的
wsgi服务器
'''


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'pythonqa.settings' #设置模块的路径
    application = get_wsgi_application()
    container = tornado.wsgi.WsgiContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    port = 8003
    host = '0.0.0.0'
    print('visit by : http://{0}:{1}/'.format(host, port))
    http_server.listen(port, address=host)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()