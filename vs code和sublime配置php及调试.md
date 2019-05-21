### [使用vs code写php及调试](https://www.cnblogs.com/ashidamana/p/5459188.html)

- 下载vscode ([visual studio code](https://www.visualstudio.com/))。 
- 安装vscode 扩展 php-debug 
-  安装wampserver
-  确保apache的80 端口未占用，如果占用了修改httpd.conf 配置文件下的端口号
- 左键单击wampserver，打开php，修改php.ini 文件，在文末**查找（没有就添加）**修改以下两项： 

```
xdebug.remote_enable = on

xdebug.remote_autostart=on
```

问题是vscode 调试Php一直中文乱码

1. 确认了vscode界面右下角 是utf-8编码, 并用记事本另存为，验证了编码utf-8
2. 文件-首选项-设置，搜索框找到php.validate.executablePath，默认是null,  找到settings.json编辑模式，改php的执行路径

```
,"php.validate.executablePath": "C:/wamp64/bin/php/php7.2.14/php.exe"
一定注意，填写的时候:
最前面要有英文逗号,
路径不是\ 是/
点开并理解vscode自身的问题描述，比网上漫无目的查找，更有针对性
```

3. 更改电脑系统变量Path，不仅仅是用户变量Path

   注意点：

   更改path,路径名为C:\wamp64\bin\php\php7.2.14，没有php.exe, 也不准/

   改完不用重启，命令提示符输入php -v可以验证是否成功



[如何在sublime上运行php](https://www.cnblogs.com/sun-cloud/p/6558918.html)

sublime配置php就很容易

- 配置环境变量是一样的。更改电脑系统变量Path为C:\wamp64\bin\php\php7.2.14Path

- 配置sublime
   Tools -build system - new build system，在打开的页面中，输入以下代码
  { 
     "cmd": ["php", "$file"],
     "file_regex": "php$", 
     "selector": "source.php" 
  }
  保存在默认的目录下即可，
  修改文件名为 php.sublime-build

- 之后随便写个简单的PHP
  ctrl+b 就可以直接运行出来了

  > 缺点在出问题，给的提示没有vscode详细，对心手不友好