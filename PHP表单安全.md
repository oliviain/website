用户提交表单时，我们将做以下两件事情：

 

1. 首先我们对用户所有提交的数据都通过 PHP 的 htmlspecialchars() 函数处理。

   ```
    // htmlspecialchars() 可以把<>转义为&lt;&gt;<script>location.href('http://www.runoob.com')</script>
   ```

    

   该代码将不会被执行，因为它会被保存为HTML转义代码，如下所示： 

   ```
   &lt;script&gt;location.href('http://www.runoob.com')&lt;/script&gt;
   ```

2. 使用 PHP trim() 函数去除用户输入数据中不必要的字符 (如：空格，tab，换行)。 

3. 使用PHP stripslashes()函数去除用户输入数据中的反斜杠 (\) 

   ---------------

   

接下来让我们将这些过滤的函数写在一个我们自己定义的函数中，这样可以大大提高代码的复用性。

 将函数命名为 test_input()。

 现在，我们可以通过test_input()函数来检测 $_POST 中的所有变量, 脚本代码如下所示：

```
//test_input()函数实例
<?php 
// 定义变量并默认设置为空值 
$name = $email = $gender = $comment = $website = "";   if ($_SERVER["REQUEST_METHOD"] == "POST") {  
$name = test_input($_POST["name"]);   
$email = test_input($_POST["email"]);
$website = test_input($_POST["website"]);
$comment = test_input($_POST["comment"]);
$gender = test_input($_POST["gender"]); 
}   
function test_input($data) { 
$data = trim($data);
$data = stripslashes($data);
$data = htmlspecialchars($data);
return $data; } ?>
```

```
//整体文件实例
<!DOCTYPE HTML> 
<html>
<head>
</head>
<body> 

<?php
// define variables and set to empty values
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $name = test_input($_POST["name"]);
   $email = test_input($_POST["email"]);
   $website = test_input($_POST["website"]);
   $comment = test_input($_POST["comment"]);
   $gender = test_input($_POST["gender"]);
}

function test_input($data) {
   $data = trim($data);
   $data = stripslashes($data);
   $data = htmlspecialchars($data);
   return $data;
}
?>

<h2>PHP 验证实例</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
   姓名：<input type="text" name="name">
   <br><br>
   电邮：<input type="text" name="email">
   <br><br>
   网址：<input type="text" name="website">
   <br><br>
   评论：<textarea name="comment" rows="5" cols="40"></textarea>
   <br><br>
   性别：
   <input type="radio" name="gender" value="female">女性
   <input type="radio" name="gender" value="male">男性
   <br><br>
   <input type="submit" name="submit" value="提交"> 
</form>

<?php
echo "<h2>您的输入：</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
?>

</body>
</html>
```

--------------



**什么是 htmlspecialchars()方法?** 

htmlspecialchars() 函数把一些预定义的字符转换为 HTML 实体。 

```
& （和号） 成为 &amp;
" （双引号） 成为 &quot;
' （单引号） 成为 &#039;
< （小于） 成为 &lt;
> （大于） 成为 &gt;
```

