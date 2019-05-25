include 和 require 语句是相同的，除了错误处理方面：

  

- require 会生成致命错误（E_COMPILE_ERROR）并停止脚本
- include 只生成警告（E_WARNING），并且脚本会继续



php可以include html文件

```
//changed_info.php
<?php

include 'update_schedule_info.html';

echo "<h2>您修改的信息为:</h2>";
echo $name;
echo "<br>";
echo $time;
echo "<br>";
echo $item;
echo "<br>";
echo $note;
echo "<br>";
echo $place;

?>
```

html文件里post到本地$_SERVER['PHP_SELF']  ，在localhost/update_schedule_info.html一直未成功

但是，被include 到changed_info.php里，成功