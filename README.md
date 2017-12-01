# tornado-VerificationCode
验证码
### 介绍

check_code.py文件：生成验证码   
Monaco.ttf：check_code.py文件用到的字体文件

### 如何使用
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