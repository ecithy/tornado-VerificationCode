# coding:utf-8 
__author__ = 'hy'

import tornado.ioloop
import tornado.web


from views.account import LoginHandler, CheckCodeHandler
from views.seed import SeedHandler



settings = {
    'template_path': 'templates',
    'static_path': 'static',
    "xsrf_cookies": True,
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login.html',   # 加@authenticated的view,如果未登录自动跳转到login_url
}

application = tornado.web.Application([
    (r"/login.html", LoginHandler,),
    (r"/seed.html", SeedHandler),
    (r"/check_code", CheckCodeHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

