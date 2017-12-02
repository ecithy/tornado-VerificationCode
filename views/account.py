from tornado.web import RequestHandler
import io
from utils import check_code

CODE = ''


class CheckCodeHandler(RequestHandler):
    def get(self):
        mstream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(mstream, "GIF")
        global CODE
        CODE = code
        self.write(mstream.getvalue())


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        login_user = self.get_secure_cookie("login_user",)
        if login_user:
            self.write('您已登录')
            return
        self.render('login.html', msg="")

    def post(self, *args, **kwargs):
        user = self.get_argument('user')
        code = self.get_argument('code')

        pwd = self.get_argument('pwd')
        if user == 'hy' and pwd == '123' and code == CODE:
            import time
            v = time.time() + 5
            self.set_secure_cookie('login_user', user+pwd, expires=v)
            self.redirect('/seed.html')
        else:
            if not user and not pwd:
                self.render('login.html', msg="请输入用户名和密码")
                return
            self.render('login.html', msg="用户名或密码错误")
