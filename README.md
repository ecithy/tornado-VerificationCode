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


生成一张验证码，并把验证码保存CODE变量
```
class CheckCodeHandler(RequestHandler):
    def get(self):
        mstream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(mstream, "GIF")
        global CODE
        CODE = code
        self.write(mstream.getvalue())

```
登录时，验证表单验证码
```
class LoginHandler(RequestHandler):
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
```