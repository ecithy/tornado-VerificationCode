# tornado-VerificationCode
验证码
### 介绍

check_code.py文件：生成验证码   
Monaco.ttf：check_code.py文件用到的字体文件

### 前端如何使用
在前端模板中嵌入下面代码
```
<p>  
	<input name='code' type="text" placeholder="验证码" />  
	<img src="/check_code" onclick='ChangeCode();' id='imgCode'>  
</p>
```


```
<script type="text/javascript">
	function ChangeCode() {
		var code = document.getElementById('imgCode');
		code.src += '?';
	}
</script>
```

### 后端如何使用

```
application = tornado.web.Application([
    (r"/check_code", CheckCodeHandler),
], **settings)
```

```
from tornado.web import RequestHandler
import io
from utils import check_code

CODE = ''  # 存储验证码


# 生成一张验证码，并把验证码保存CODE变量
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

    # 登录时，验证表单验证码
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
```
