from tornado.web import RequestHandler
import io
from utils import check_code
import json


class CheckCodeHandler(RequestHandler):
    def get(self):
        mstream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(mstream, "GIF")

        code_dict = {}
        code_dict['key_code'] = code
        with open('code.json', 'w') as f:
            json.dump(code_dict, f)
        self.write(mstream.getvalue())


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        login_user = self.get_secure_cookie("login_user",)
        if login_user:
            self.write('您已登录')
            return
        self.render('login.html', msg="")

    def post(self, *args, **kwargs):
        with open('code.json', 'r') as f:
            json_code = json.load(f)
        user = self.get_argument('user')
        code = self.get_argument('code')
        print(code, json_code['key_code'])

        pwd = self.get_argument('pwd')
        if user == 'hy' and pwd == '123' and code == json_code['key_code']:
            import time
            v = time.time() + 5
            self.set_secure_cookie('login_user', user+pwd, expires=v)
            self.redirect('/seed.html')
        else:
            if not user and not pwd:
                self.render('login.html', msg="请输入用户名和密码")
                return
            self.render('login.html', msg="用户名或密码错误")
