# website
## 易错点：
图片不显示
Psd格式的不显示，jpg,gif都可以
图片名称是中文不显示——改成英文
图片居中对齐，align="center"属性不好使，需要放在···<div align="center"></div>
<img src="images/timg.psd" alt="点我看《你的名字》" align="center"/> ···


另一种有局限的图片居中, 不能随着浏览器变化而居中:
···<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>图片居中</title>
<style type="text/css">
body{width:800px;}
div{ margin:0 auto;width:300px;/}
img{ margin:0 auto;}
</style>
</head>
<body>
<div>
    <img src="20151001200918.jpg" width="300" />
</div>
</body>
</html>···

设置文本中的图像的对齐方式：
<img src="/i/eg_cute.gif" align="middle" />···




显示特点：
···<blockquote></blockquote>··· 多句无双引号
···<q></q> ···单句带双引号
<strong><em>类似


待解决点：
框架上加文字，图片，链接，多媒体

