from tornado.web import RequestHandler
from tornado.web import authenticated


class AuthRequestHandler(object):
    def get_current_user(self):
        return self.get_secure_cookie('login_user')


class SeedHandler(AuthRequestHandler, RequestHandler):
    @authenticated
    def get(self, *args, **kwargs):
        seed_list = [
            {"title": '小麦', 'price': 2},
            {"title": '大麦', 'price': 21},
            {"title": '大桥', 'price': 22},
            {"title": '未久', 'price': 220},
        ]
        self.render('seed.html', seed_list=seed_list)
