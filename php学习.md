

# php学习笔记

#### 基本语句：

```
<?php
// 或# 此处是 单句PHP 代码注释

/* 多句代码

多行注释

*/ ?>
```



#### 大小写敏感：

用户定义的函数、类和关键词（例如 if、else、echo 等等）都对大小写不敏感

比如echo

```
<?php
ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
```

所有变量都对大小写敏感。

> 非严格状态，数据类型不用声明，可以根据输入自动赋予类型

#### 变量

$a

**全局变量**：所有函数外部定义的变量，拥有全局作用域。除了函数外，全局变量可以被脚本中的任何部分访问。在函数内引用要 关键字global $a

全局变量和局部变量的例子：

```
<?php
$a=9.9;
function myTest2()
{ $b=5.5;
echo "<p>Test variables inside the function:<p>";
echo "Varial a is: $a";
echo "<br/>";
echo "Variable b is: $b";
}

myTest2();
echo "<p>Test variables outside the function:<p>"; 
echo "Variable a is: $a"; 
echo "<br>"; 
echo "Variable b is: $b";  ?>
```

输出结果为![1554392107475](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554392107475.png)

```
#全局变量的引用
<?php 
$x=5; 
$y=10; 

function myTest() 
{ 
global $x,$y; 
$y=$x+$y; 
} 

myTest(); 
echo $y; // 输出 15 
?>

```

PHP 将所有全局变量存储在一个名为 $GLOBALS[*index*] 的数组中。 *index* 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。

比如e

```
<?php 
$x=5; 
$y=10; 

function myTest() 
{ 
$GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y']; 
} 

myTest(); 
echo $y; //输出15
echo $GLOBALS['x'];//输出5
?>
```



#### 尝试

```
<?php
$color="red";
echo "My car is " . $color . "<br>";
echo "My house is " . $COLOR . "<br>";
echo "My boat is " . $coLOR . "<br>";
?>
```

```
<?php
echo "<h2>PHP 很有趣!</h2>";
echo "<ul><li>希望顺利<li><li>Hello world!<li></ul>";
echo "<footer>&copy;by olivialin</footer><br>";echo "这是一个", "字符串，", "hello", "world!";
?>
```

## PHP echo ,print 和 print_r 语句

 echo , print 和 print_r的区别: 

- echo   - 可以输出一个或多个字符串 echo 或 echo()都可以
- print   - 只能输出简单类型变量的值,如int,string
- print_r - 可以输出复杂类型变量的值,如数组,对象 

**提示：**echo输出的速度比print快,echo是PHP语句,没有返回值,print和print_r是PHP函数,函数有返回值。

​	print返回值为1(int类型),print_r返回值为true(bool类型)。

#### 数据类型

-----------------------------------------------------------------

var_dump() 会返回变量的数据类型和值：

```
<?php 
$x = 5985;
var_dump($x);
echo "<br>"; 
$x = -345; // 负数
var_dump($x);
echo "<br>"; 
$x = 0x8C; // 十六进制数
var_dump($x);
echo "<br>";
$x = 047; // 八进制数
var_dump($x);
?>
```

![1554514553077](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554514553077.png)

>  *.8E-5*是科学计数法方式 0.8*10^-5   
>
> 2.4e3   是指 *e3* 科学计数法中,*e3*就表示10的三次方



##### null：

- $apple = null; 
- 未声明变量null 
- unset($a);   $a被毁成null

```
<?php

$apple = null;//empty()可入一个变量。如果是false或null，返回true。
if(empty($apple)){
    echo '执行了真区间，凤姐，我爱你';
}else{
   echo '执行假区间，你想凤姐了';
}

$one = 10;
$two = false;
$three = 0;
$four = null;

$result = isset($one , $two , $three , $four);
//isset()只要有有一个变量为null，则返回false。否则，则返回true。
var_dump($result);

?>
```



#### 定义常量

-----------------------

```
<?php
// 区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com");
echo GREETING;    // 输出 "欢迎访问 Runoob.com"
echo '<br>';
echo greeting;   // 输出 "greeting"
?>
```

```
<?php
// 不区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com", true);
echo greeting;  // 输出 "欢迎访问 Runoob.com"
?>
```



####  字符串变量

----------------------------------

```
<?php
echo strlen("Hello world!");//返回字符串的长度，输出12，表示12个字符
echo "<br>";
echo str_word_count("Hello world!"); //对字符串中的单词进行计数, 输出2，2个单词
echo str_replace("Hello","你好，","Hello world!")//字符串替换字符串，输出你好， world!
echo strrev("Hello world!"); // 输出 !dlrow olleH
echo strpos("Hello world!","wo"); //查找一个字符或一段指定的文本，匹配返回第一个匹配的字符位置，输出6。如果未找到匹配，则返回 FALSE或无输出
?>
```

> strlen() 常用于循环和其他函数，在确定字符串何时结束很重要



#### PHP 赋值运算符

---------------

![1554520124042](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554520124042.png)

![1554520166090](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554520166090.png)

```
<?php
$x=17; 
echo ++$x; // 前递增，输出 18

$y=17; 
echo $y++; // 后递增，输出 17

$z=17;
echo --$z; // 前递减，输出 16

$i=17;
echo $i--; // 后递减，输出 17
?>
```



#### 比较运算符 

----------------------

特别在 === 全等（数值、类型） ！==(如果 $x 不等于 $y，或它们类型不相同，则返回 true。) !=(如果 $x 不等于 $y, 则返回 true)



![1554520586969](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554520586969.png)

![1554520642101](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554520642101.png)

```
<?php
$x = array("a" => "apple", "b" => "banana");  
$y = array("c" => "orange", "d" => "peach");  
$z = $x + $y; // $x 与 $y 的联合 
 
var_dump($z);//输出array(4) { ["a"]=> string(5) "apple" ["b"]=> string(6) "banana" ["c"]=> string(6) "orange" ["d"]=> string(5) "peach" }

echo "<br>";
var_dump($x == $y);//bool(false) 

echo "<br>";
var_dump($x === $y);//bool(false) 

echo "<br>";
var_dump($x != $y);//bool(true)
echo "<br>";
var_dump($x <> $y);//bool(true)
echo "<br>";
var_dump($x !== $y);//bool(true) 
?>   
```

#### 条件语句

```
<?php  
 
$t=date("H:i:s");
if ($t<"10:10:10") 
{  
    echo "time to get up";
}
elseif ($t<"18:18:18")//表示"10:10:10"<$t<"18:18:18", 不可以直接放到函数里
{   
    echo "do you have dinner?";
}
 
elseif ($t<"20:20:20")  
{  
    echo "Have you done your job?";  
}  
else  
{  
    echo "Have a good night!";  
}  
?>  
```



#### do while

------------------

```
//while
<?php 
$x=1; 
while($x<=5) {
echo "这个数字是：$x <br>";
$x++;
} 
?>

//do格式上把while ($x<=5)放到最后，加符号;

<?php 
$x=1; //提示do 先执行语句，后判断，如果此处$x=1000,会输出1000

do {
  echo "这个数字是：$x <br>";
  $x++;
} while ($x<=5);
?>
```

#### PHP for 循环

```
for (init counter; test counter; increment counter) {
  code to be executed;
}
```

```
<?php
for ($a=0;$a<=5;$a++){ //注意for(;;)是分号分隔
echo "爱你$a"."次<br>";//"爱你$a次"不能显示，$a后不可以直接加字符“次"
}
?>
/*输出
爱你0次
爱你1次
爱你2次
爱你3次
爱你4次
爱你5次*/
```

####  PHP foreach 循环

 foreach 循环只适用于数组，并用于遍历数组中的每个键/值对。

每进行一次循环迭代，当前数组元素的值就会被赋值给 $value 变量，并且数组指针会逐一地移动，直到到达最后一个数组元素。

```
foreach ($array as $value) {
  code to be executed;
}
```

```
<?php
$lovetype = array("solitude","crazy","safe","scary");
foreach ($lovetype as $value){
    echo "love can be $value <br>";//是赋值给了$value
}
?>
/*输出
love can be solitude 
love can be crazy 
love can be safe 
love can be scary */
```

#### 数组

--------------------------

自动分配 ID 键（ID 键总是从 0 开始）： 

 $cars=array("Volvo","BMW","Toyota");

  人工分配 ID 键： 

 $cars[0]="Volvo";
 $cars[1]="BMW";
 $cars[2]="Toyota"; 

例子：

```
<?php 
$cars=array("Volvo","BMW","Toyota"); 
echo "I like {$cars[0]}, " . $cars[1] . " and " . $cars[2] . "."; 
echo count($cars);//count（）数组长度，输出为3
?> 
```

```
<?php
$cars=array("Volvo","BMW","Toyota");
$arrlength=count($cars);
for($x=0;$x<$arrlength;$x++)
{
echo $cars[$x];
echo "<br>";
}
?>
```

##### 遍历数值数组

```
<?php
$cars=array("Volvo","BMW","Toyota");
$arrlength=count($cars);
for($x=0;$x<$arrlength;$x++)
{
echo $cars[$x];
echo "<br>";
}
?>
```



##### 遍历关联数组

用 foreach 循环，遍历并打印关联数组中的所有值，如下所示：

```
 <?php 
 $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");   
 foreach($age as $x=>$x_value) { 
 echo "Key=" . $x . ", Value=" . $x_value;
 echo "<br>";
 } 
 ?>
```

##### 数组排序

- sort() - 对数组进行升序排列

  ```
  <?php
  $cars=array("porsche","BMW","Volvo");
  	sort($cars);
  print_r($cars);
  ?>
  /*输出为
  Array
  (
      [0] => BMW
      [1] => Volvo
      [2] => porsche
  )*/
  
  ```

  

- rsort() - 对数组进行降序排列

- asort() - 根据关联数组的值，对数组进行升序排列

- ksort() - 根据关联数组的键，对数组进行升序排列

- arsort() - 根据关联数组的值，对数组进行降序排列

- krsort() - 根据关联数组的键，对数组进行降序排列

##### 超级全局变量

- $GLOBALS

- $_SERVER

  ```
  <?php 
  echo $_SERVER['PHP_SELF'];
  echo "<br>";
  echo $_SERVER['SERVER_NAME'];
  echo "<br>";
  echo $_SERVER['HTTP_HOST'];
  echo "<br>";
  echo $_SERVER['HTTP_REFERER'];
  echo "<br>";
  echo $_SERVER['HTTP_USER_AGENT'];
  echo "<br>";
  echo $_SERVER['SCRIPT_NAME'];
  ?>
  ```

  ![1554537283740](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554537283740.png)![1554537304751](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554537304751.png)

- $_REQUEST

  ```
  <html>
  <body>
  
  <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
  </form>
  
  <?php 
  $name = $_REQUEST['fname']; 
  echo $name; 
  ?>
  </body>
  </html>
  ```

  

- $_POST

  PHP $_POST 被广泛应用于收集表单数据，在HTML form标签的指定该属性："method="post"。

  ```
  <html>
  <body>
  
  <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
  </form>
  
  <?php 
  $name = $_POST['fname']; 
  echo $name; 
  ?>
  </body>
  </html>
  ```

  

- $_GET

PHP $_GET 同样被广泛应用于收集表单数据，在HTML form标签的指定该属性："method="get"。 

$_GET 也可以收集URL中发送的数据。假设我们有一张页面含有带参数的超链接：

  

```
<html>
<body>

<a href="test_get.php?subject=PHP&web=W3school.com.cn">测试 $GET</a>

</body>
</html>
```



当用户点击链接 "测试 $GET"，参数 "subject" 和 "web" 被发送到 "test_get.php"，然后您就能够通过 $_GET 在 "test_get.php" 中访问这些值了。

下面的例子是 "test_get.php" 中的代码：

```
<html>
<body>

<?php 
echo "在 " . $_GET['web'] . " 学习 " . $_GET['subject'];
?>

</body>
</html>
```



##### 函数

```
<?php
function test( $arg = 10){
   echo $arg;
}

test();//输出10

test(88);//输出88

?>
```

```
<?php
function test( $a , $b = 20 , $c = 30){

       echo $a + $b + $c;

}
test(1);//输出51
echo "<br>";
test( 1 , 2 , 3 );//输出6
?>
```

```
<?php

function test($x, $y=9, $z){// $z报错
    echo $x-($y+$z);
}

test(1, 3);//
echo "<br>";
test( 1 , 2 , 3 );
?>
<?php
function test( $c , $a = 20 , $b = 30){ //无默认值的参数放最前，可以

       echo $a + $b + $c;

}

test( 8 );//58
?>
```

函数调用可以在定义之前，定义之后。

同名函数不能重载

```
<?php

function demo(){

}

function demo(){

}
//试试报错
?>
```



**PHP** **魔术常量**

```
注意是双下划线，__  2个_
```

```
__LINE__
<?php
echo '这是第 " '  . __LINE__ . ' " 行';
?>
```

```
__FILE__//文件的完整路径和文件名。
<?php
echo '该文件位于 " '  . __FILE__ . ' " ';
?>
```

```
__DIR__//文件所在的目录。
<?php
echo '该文件位于 " '  . __DIR__ . ' " ';
?>
```

```
__FUNCTION__
函数名称（PHP 4.3.0 新加）。自 PHP 5 起本常量返回该函数被定义时的名字（区分大小写）
<?php
function test(){
    echo "function name is ".__FUNCTION__;
    
}
test();
?>
//输出function name is test

```

```
__CLASS__
类的名称（PHP 4.3.0 新加）。自 PHP 5 起本常量返回该类被定义时的名字（区分大小写）。
__NAMESPACE__
当前命名空间的名称（区分大小写）。此常量是在编译时定义的（PHP 5.3.0 新增）。
```

```
__METHOD__
类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）。
实例:
实例
<?php
function test() {
    echo  '函数名为：' . __METHOD__ ;
}
test();
?>
```

```
__TRAIT__
Trait 的名字（PHP 5.4.0 新加）。自 PHP 5.4.0 起，PHP 实现了代码复用的一个方法，称为 traits。
Trait 名包括其被声明的作用区域（例如 Foo\Bar）。
从基类继承的成员被插入的 SayWorld Trait 中的 MyHelloWorld 方法所覆盖。其行为 MyHelloWorld 类中定义的方法一致。优先顺序是当前类中的方法会覆盖 trait 方法，而 trait 方法又覆盖了基类中的方法。
实例
<?php
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}
 
trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}
 
class MyHelloWorld extends Base {
    use SayWorld;
}
 
$o = new MyHelloWorld();
$o->sayHello();
?>
```

#### foo bar baz

----------

- foo: first object oriented  第一个面向对象
- bar: binary arbitrary reason  任意二进制原因
- foo-bar-baz张三-李四-王五

#### 获取昨天的时间

```
<?phpecho date("Y-m-d H:i:s", strtotime("-1 day"));
echo "--------------";
echo date("Y-m-d H:i:s", strtotime("yesterday"));
?>
结果：2017-08-06 14:17:46--------------2017-08-06 00:00:00
```

作者：WilliamsWayne 
来源：CSDN 
原文：https://blog.csdn.net/williamswayne/article/details/76838447 
版权声明：本文为博主原创文章，转载请附上博文链接！