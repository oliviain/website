# mysql学习笔记



## 基本概念

---------------------

1. **数据定义语言**(DDL ，Data Defintion Language)语句：数据定义语句，用于定义不同的数据段、数据库、表、列、索引等。常用的语句关键字包括create、drop、alter等。
2. **数据操作语言**(DML ， Data Manipulation Language)语句：数据操纵语句，用于添加、删除、更新和查询数据库记录，并检查数据的完整性。常用的语句关键字主要包括insert、delete、update和select等。
3. **数据控制语言**(DCL， Data Control Language)语句：数据控制语句，用于控制不同数据段直接的许可和访问级别的语句。这些语句定义了数据库、表、字段、用户的访问权限和安全级别。主要的语句关键字包括grant、revoke等。

## Tips

输入**\c**来取消前边的输入

**\p**来打印前边的命令，再复制（在命令行客户端右键，选择标记，就可以选择带复制的内容，选择好后，按Enter，即可将选择的内容复制到剪切板），接着输入\c，再粘贴，修改，执行命令。![img](https://img-blog.csdn.net/20150313095307862?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2lsbGV5ag==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



## mysql提示符

---------------

![1554792737055](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554792737055.png)



## 操作笔记

|          | **CREATE DATABASE PHP;**        |
| -------- | ------------------------------- |
| 示例说明 | 创建一个数库，数据库的名字为PHP |

示例：

> mysql> CREATE DATABASE PHP;
>    Query OK, 1 row affected (0.00 sec)

“Query OK” 表示上面的命令执行成功，所有的 DDL 和 DML(不包 括 SELECT)操作执行成功后都显示“Query OK”，这里理解为执行成功就可以了；“1 row affected” 表示操作只影响了数据库中一行的记录，“0.00 sec”则记录了操作执行的时间。

如果已经存在这个数据库，系统会?示:

> mysql> CREATE DATABASE PHP;
>    ERROR 1007 (HY000): Can't create database 'PHP'; database exists





|      | show databases;            |
| ---- | -------------------------- |
| 示例 | 查看当前服务器的所有数据库 |

示例：

> mysql> SHOW DATABASES;
>    +--------------------+
>    | Database           |
>    +--------------------+
>    | information_schema |
>    | mysql              |
>    | performance_schema |
>    | user               |
>    +--------------------+
>    4 rows in set (0.00 sec)





|          | **use PHP**   |
| -------- | ------------- |
| 示例说明 | 使用数据库PHP |

注意：
use 是指使用；
库名 是存在当前数据库系统中的具体的数据库的名称；

> mysql> use PHP;
>  Database changed







进入到库后我们可以看这个库里面有多少个数据表。

| 类别     | 详细解示                 |
| -------- | ------------------------ |
| 基本语法 | **show tables;**         |
| 示例说明 | 显示当前数据库下所有的表 |





| 类别     | 详细解示                             |
| -------- | ------------------------------------ |
| 基本语法 | **DROP DATABASE 库名;**              |
| 示例     | **DROP DATABASE  PHP;**              |
| 示例说明 | 删除一个数库，数据库的名字为liwenkai |

注意：
drop 是汉语可以翻译为指掉下来，不要了的意思
database 是指库
库名 是指要删掉的库的名称

示例：

> mysql> DROP DATABASE  PHP;
>    Query OK, 0 rows affected (0.01 sec)



| 别       | 详细解示                                                     |
| -------- | ------------------------------------------------------------ |
| 基本语法 | CREATE TABLE表名(字段名1 字段类型,....字段名n 字段类型n);    |
| 示例     | CREATE TABLE user(username varchar(20),password varchar(32)); |
| 示例说明 | 创建一个表名叫user的表，第一个字段为username、表的字段类型为varchar长度为32个长度。第二个字段为password，类型也为varchar，长度也为32个长度。 |

> mysql> CREATE TABLE emp( 
>    ename varchar(10), 
>    hiredate date, 
>    sal float(10,2), 
>    deptno int(2) 
>    );
>    Query OK, 0 rows affected (0.63 sec)







| 类别     | 详细解示          |
| -------- | ----------------- |
| 基本语法 | desc 表名;        |
| 示例     | desc emp          |
| 示例说明 | 查看emp表的表结构 |

![1554794846144](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554794846144.png)



删除表/数据库 drop table 表名；或drop database 数据库名；

删除schedule表的phone字段（不要加类型 int(10))  alter table schedule drop phone;

字段增加和修改语句（add/change/modify）-（增条目/改字段名/改字段类型）中，最后都可以加一个可选项 first|after。

alter table schedule add tel int(20);(可以加一个可选项 first|after)

alter table schedule change only_id id varchar(64); //only_id旧字段名——id新字段名

alter table schedule modify tel varchar(60) after id;新字段类型









# 数据类型

1. 数值类型（整型、浮点）
2. 字符串类型
3. 日期时间类型
4. 复合类型
5. 空间类型（非科学性工作基本不用，不做讲解）

## 整型

| MySQL数据类型 | 所占字节 | 值范围                     |
| ------------- | -------- | -------------------------- |
| tinyint       | 1字节    | -128~127                   |
| smallint      | 2字节    | -32768~32767               |
| mediumint     | 3字节    | -8388608~8388607           |
| int           | 4字节    | 范围-2147483648~2147483647 |
| bigint        | 8字节    | +-9.22*10的18次方          |

整型的长度不同，在实际使用过程也就不同。

MySQL 以一个可选的显示宽度指示器的形式对 SQL 标准进行扩展，这样当从数据库检索一个值时，可以把这个值加长到指定的长度。例如，指定一个字段的类型为 INT(6)，
就可以保证所包含数字少于 6 个的值从数据库中检索出来时能够自动地用空格填充。需要注意的是，使用一个宽度指示器不会影响字段的大小和它可以存储的值的范围。

注意：

1. 在创建表字段时，性别我们可以使用无符号的微小整型（tinyint）来表示。用0表示女、用1表示男。用2表示未知。
2. 同样人类年龄也是，在创建表字段时可用用无符号的整型。因为人类的年龄还没有负数
3. 在实际使用过程中。我们业务中最大需要存储多大的数值。我们创建表时，就选择什么样的类型来存储这样的值。

## 浮点类型

| MySQL数据类型 | 所占字节 | 值范围                         |
| ------------- | -------- | ------------------------------ |
| float(m, d)   | 4字节    | 单精度浮点型，m总个数，d小数位 |
| double(m, d)  | 8字节    | 双精度浮点型，m总个数，d小数位 |
| decimal(m, d) |          | decimal是存储为字符串的浮点数  |

注意：

1. 浮点是非精确值，会存在不太准确的情况
2. 而decimal叫做定点数。在MySQL内部，本质上是用字符串存储的。实际使用过程中如果存在金额、钱精度要求比较高的浮点数存储，建议使用decimal（定点数）这个类型。

## 字符类型

| MySQL数据类型 | 所占字节                        | 值范围                          |
| ------------- | ------------------------------- | ------------------------------- |
| CHAR          | 0-255字节                       | 定长字符串                      |
| VARCHAR       | 0-255字节                       | 变长字符串                      |
| TINYBLOB      | 0-255字节                       | 不超过255个字符的二进制字符串   |
| TINYTEXT      | 0-255字节                       | 短文本字符串                    |
| BLOB          | 0-65535字节                     | 二进制形式的长文本数据          |
| TEXT          | 0-65535字节                     | 长文本数据                      |
| MEDIUMBLOB    | 0-16 777 215字节                | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT    | 0-16 777 215字节                | 中等长度文本数据                |
| LOGNGBLOB     | 0-4 294 967 295字节             | 二进制形式的极大文本数据        |
| LONGTEXT      | 0-4 294 967 295字节             | 极大文本数据                    |
| VARBINARY(M)  | 允许长度0-M个字节的定长字节符串 | 值的长度+1个字节                |
| BINARY(M)     | M                               | 允许长度0-M个字节的定长字节符串 |

**CHAR **类型用于定长字符串，并且必须在圆括号内用一个大小修饰符来定义。这个大小修饰符的范围从 0-255。比指定长度大的值将被截短，而比指定长度小的值将会用空格作填补。
**VARCHAR  **把这个大小视为值的大小，不长度不足的情况下就用空格补足。而 VARCHAR 类型把它视为最大值并且只使用存储字符串实际需要的长度
  类型不会被空格填补，但长于指示器的值仍然会被截短。
因为 VARCHAR 类型可以根据实际内容动态改变存储值的长度，所以在不能确定字段需要多少字符时使用 VARCHAR 类型可以大大地节约磁盘空间、提高存储效率。

**text类型与blob类型**对于字段长度要求超过 255 个的情况下，MySQL 提供了 TEXT 和 BLOB 两种类型。根据存储数据的大小，它们都有不同的子类型。这些大型的数据用于存储文本块或图像、
声音文件等二进制数据类型。
TEXT 和 BLOB 类型在分类和比较上存在区别。BLOB 类型区分大小写，而 TEXT 不区分大小写。大小修饰符不用于各种 BLOB 和 TEXT 子类型。

## 时间类型

| MySQL数据类型 | 所占字节 | 值范围                              |
| ------------- | -------- | ----------------------------------- |
| date          | 3字节    | 日期，格式：2014-09-18              |
| time          | 3字节    | 时间，格式：08:42:30                |
| datetime      | 8字节    | 日期时间，格式：2014-09-18 08:42:30 |
| timestamp     | 4字节    | 自动存储记录修改的时间              |
| year          | 1字节    | 年份                                |

注意：

1. 时间类型在web系统中用的比较少，很多时候很多人喜欢使用int来存储时间。插入时插入的是unix时间戳，因为这种方式更方便计算。在前端业务中用date类型的函数，再将unix时间戳转成人们可识别的时间。
2. 上面的类型你可以根据实际情况实际进行选择
3. 有些人为了在数据库管理中方便查看，也有人使用datetime类型来存储时间。

## 复合类型

| MySQL数据类型 | 说明     | 举例                                        |
| ------------- | -------- | ------------------------------------------- |
| set           | 集合类型 | set(“member”, “member2″, … “member64″)      |
| enum          | 枚举类型 | enum(“member1″, “member2″, … “member65535″) |

一个 ENUM 类型只允许从一个集合中取得一个值；而 SET 类型允许从一个集合中取得任意多个值。

**ENUM 类型**

ENUM 类型因为只允许在集合中取得一个值，有点类似于单选项。在处理相互排拆的数据时容易让人理解，比如人类的性别。ENUM 类型字段可以从集合中取得一个值或使用null值，除此之外的输入将会使 MySQL 在这个字段中插入一个空字符串。另外如果插入值的大小写与集合中值的大小写不匹配，MySQL会自动使用插入值的大小写转换成与集合中大小写一致的值。

ENUM 类型在系统内部可以存储为数字，并且从1开始用数字做索引。一个 ENUM 类型最多可以包含 65536 个元素，其中一个元素被 MySQL 保留，用来存储错误信息，这个错误值用索引 0 或者一个空字符串表示。

MySQL 认为 ENUM 类型集合中出现的值是合法输入，除此之外其它任何输入都将失败。这说明通过搜索包含空字符串或对应数字索引为 0 的行就可以很容易地找到错误记录的位置。

**SET 类型**SET 类型与 ENUM 类型相似但不相同。SET类型可以从预定义的集合中取得任意数量的值。并且与 ENUM 类型相同的是任何试图在 SET 类型字段中插入非预定义的值都会使MySQL插入一个空字符串。如果插入一个即有合法的元素又有非法的元素的记录，MySQL 将会保留合法的元素，除去非法的元素。

一个 SET 类型最多可以包含 64 项元素。在 SET 元素中值被存储为一个分离的“位”序列，这些“位”表示与它相对应的元素。“位”是创建有序元素集合的一种简单而有效的方式。
并且它还去除了重复的元素，所以SET类型中不可能包含两个相同的元素。
希望从 SET 类型字段中找出非法的记录只需查找包含空字符串或二进制值为 0 的行。

## 类型使用

我们学习了这么多类型，在创建表的语句的时候使用对应的类型即可。

举例如下：

> CREATE TABLE IF NOT EXISTS `demo` (
>     `id` int(11) NOT NULL,
>     `username` varchar(50) NOT NULL,
>     `password` char(32) NOT NULL,
>     `content` longtext NOT NULL,
>     `createtime` datetime NOT NULL,
>     `sex` tinyint(4) NOT NULL
>    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

## 字段其他属性设置

**UNSIGNED（无符号）**主要用于整型和浮点类型，使用无符号。即，没有前面面的-（负号）。
存储位数更长。tinyint整型的取值区间为，-128~127。而使用无符号后可存储0-255个长度。

创建时在整型或浮点字段语句后接上：

> unsigned

**ZEROFILL（0填充）**0（不是空格）可以用来真补输出的值。使用这个修饰符可以阻止 MySQL 数据库存储负值。

创建时在整型或浮点字段语句后接上：

> zerofill

**default**default属性确保在没有任何值可用的情况下，赋予某个常量值，这个值必须是常量，因为MySQL不允许插入函数或表达式值。此外，此属性无法用于BLOB或TEXT列。如果已经为此列指定了NULL属性，没有指定默认值时默认值将为NULL，否则默认值将依赖于字段的数据类型。

创建时在整型或浮点字段语句后接上：

> default '值'

**not null**如果将一个列定义为not null，将不允许向该列插入null值。建议在重要情况下始终使用not null属性，因为它提供了一个基本验证，确保已经向查询传递了所有必要的值。

创建时在整型或浮点字段语句后接上：

> not null

**null**为列指定null属性时，该列可以保持为空，而不论行中其它列是否已经被填充。记住，null精确的说法是“无”，而不是空字符串或0。

创建时在整型或浮点字段语句后不要声明not null即可。



## SQL 语句

 **auto-increment** 

下列 SQL 语句把 "Persons" 表中的 "P_Id" 列定义为 **auto-increment** 主键：  

```
CREATE TABLE Persons
(
P_Id int NOT NULL AUTO_INCREMENT,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PRIMARY KEY (P_Id)
)
```

  

MySQL 使用 AUTO_INCREMENT 关键字来执行 auto-increment 任务。

  默认地，AUTO_INCREMENT 的开始值是 1，每条新记录递增 1。

  要让 AUTO_INCREMENT 序列以其他的值起始，请使用下列 SQL 语法：  

```
ALTER TABLE Persons AUTO_INCREMENT=100
```



**PRIMARY KEY** 约束唯一标识数据库表中的每条记录。

  主键必须包含唯一的值。

  主键列不能包含 NULL 值。

  每个表都应该有一个主键，并且每个表只能有一个主键。



mysql导入数据错误“ERROR 2006 (HY000): MySQL server has gone away”

mysql导入导出的命令

mysqldump -u root -p dbname > D:\exp.sql  --本地导出

mysqldump -u admin -p -h 192.168.50.59 -P 3306  dbname> D:\exp.sql --远程导出

source D:\exp.sql --导入

mysql -u admin -p -h 192.168.50.59 -P 3306 -D dbname --远程登录



作者：Java面试必修 
来源：CSDN 
原文：https://blog.csdn.net/ron03129596/article/details/53572737 
版权声明：本文为博主原创文章，转载请附上博文链接！