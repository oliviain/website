## mysql中engine=innodb和engine=myisam的区别 		



1/ISAM 

ISAM是一个定义明确且历经时间考验的数据表格管理方法，它在设计之时就考虑到数据库被查询的次数要远大于更新的次数。因此，ISAM执行读取操作的速度很快，而且不占用大量的内存和存储资源。ISAM的两个主要不足之处在于，它不支持事务处理，也不能够容错：如果你的硬盘崩溃了，那么数据文件就无法恢复了。如果你正在把ISAM用在关键任务应用程序里，那就必须经常备份你所有的实时数据，通过其复制特性，MySQL能够支持这样的备份应用程序。 

2/InnoDB 

它提供了事务控制能力功能，它确保一组命令全部执行成功，或者当任何一个命令出现错误时所有命令的结果都被回退，可以想像在电子银行中事务控制能力是非常重要的。支持COMMIT、ROLLBACK和其他事务特性。最新版本的Mysql已经计划移除对BDB的支持，转而全力发展InnoDB。 

MyIASM是IASM表的新版本，有如下扩展：  
二进制层次的可移植性。  
NULL列索引。  
对变长行比ISAM表有更少的碎片。  
支持大文件。  
更好的索引压缩。  
更好的键吗统计分布。  
更好和更快的auto_increment处理。 

以下是一些细节和具体实现的差别：

1.InnoDB不支持FULLTEXT类型的索引。
2.InnoDB中不保存表的 
具体行数，也就是说，执行select count(*) from 
table时，InnoDB要扫描一遍整个表来计算有多少行，但是MyISAM只要简单的读出保存好的行数即可。注意的是，当count(*)语句包含 
where条件时，两种表的操作是一样的。
3.对于AUTO_INCREMENT类型的字段，InnoDB中必须包含只有该字段的索引，但是在MyISAM表中，可以和其他字段一起建立联合索引。
4.DELETE 
FROM table时，InnoDB不会重新建立表，而是一行一行的删除。
5.LOAD TABLE FROM 
MASTER操作对InnoDB是不起作用的，解决方法是首先把InnoDB表改成MyISAM表，导入数据后再改成InnoDB表，但是对于使用的额外的InnoDB特性（例如外键）的表不适用。

另外，InnoDB表的行锁也不是绝对的，如果在执行一个SQL语句时MySQL不能确定要扫描的范围，InnoDB表同样会锁全表，例如update 
table set num=1 where name like “�a%”

任何一种表都不是万能的，只用恰当的针对业务类型来选择合适的表类型，才能最大的发挥MySQL的性能优势.

MySQL 
Administrator建数据库的时候，表缺省是InnoDB类型。

InnoDB，MyISAM 
两种类型有什么区别：MyISAM类型不支持事务处理等高级处理，而InnoDB类型支持。 
MyISAM类型的表强调的是性能，其执行数度比InnoDB类型更快，但是不提供事务支持，而InnoDB提供事务支持，外键等高级数据库功能。

MyISAM类型的二进制数据文件可以在不同操作系统中迁移。也就是可以直接从Windows系统拷贝到linux系统中使用。

修改表的引擎类型：

ALTER 
TABLE tablename ENGINE = MyISAM ；

MyISAM:,它是基于传统的ISAM类型,ISAM是Indexed 
Sequential Access Method (有索引的 顺序访问方法) 
的缩写,它是存储记录和文件的标准方法.与其他存储引擎比较,MyISAM具有检查和修复表格的大多数工具. 
MyISAM表格可以被压缩,而且它们支持全文搜索.它们不是事务安全的,而且也不支持外键。如果事物回滚将造成不完全回滚，不具有原子性。如果执行大量 
的SELECT，MyISAM是更好的选择。

InnoDB:这种类型是事务安全的.它与BDB类型具有相同的特性,它们还支持外键.InnoDB表格速度很快.具有比BDB还丰富的特性,因此如果需要一个事务安全的存储引擎,建议使用它.如果你的数据执行大量的INSERT或UPDATE,出于性能方面的考虑，应该使用InnoDB表,

对于支持事物的InnoDB类型的标，影响速度的主要原因是AUTOCOMMIT默认设置是打开的，而且程序没有显式调用BEGIN 
开始事务，导致每插入一条都自动Commit，严重影响了速度。可以在执行sql前调用begin，多条sql形成一个事物（即使autocommit打 
开也可以），将大大提高性能。

1.查看表信息，里面包括使用的引擎类型，字符编码，表结构等

使用这个命令

mysql> 
show create table t1;--t1是表名

2. 
可以执行以下命令来切换非事务表到事务（数据不会丢失），innodb表比myisam表更安全：
   alter table t1 
type=innodb;--t1是表名

3. 
innodb表不能用repair table命令和myisamchk -r table_name
但可以用check table 
t1，以及mysqlcheck [OPTIONS] database [tables]

4. 
启动mysql数据库的命令行中添加了以下参数可以使新发布的mysql数据表都默认为使用事务（
只影响到create语句。）
--default-table-type=InnoDB

5. 
临时改变默认表类型可以用：
set table_type=InnoDB;

MyISAM
优点：速度快，磁盘空间占用少；某个库或表的磁盘占用情况既可以通过操作系统查相应的文件（夹）的大小得知，也可以通过SQL语句SHOW TABLE STATUS查得
缺点：没有数据完整性机制，即不支持事务和外键

InnoDB
优点：支持事务和外键，数据完整性机制比较完备；可以用SHOW TABLE STATUS查得某个库或表的磁盘占用
缺点：速度超慢，磁盘空间占用多；所有库都存于一个（通常情况）或数个文件中，无法通过操作系统了解某个库或表的占用空间

BDB
优点：支持事务，不支持外键，由于在事务支持的基础上，外键可以在数据库的客户端（可能是最终客户的服务器端，例如php）间接实现，所以数据完整性仍然是有保障的；
缺点：速度慢，磁盘占用多；不能通过SHOW TABLE STATUS查询某个库或表的空间占用；用操作系统可了解库相应的文件夹，或表相应的文件的大小，但由于BDB表总是还要产生log文件，而实际的磁盘占用应该把log文件也包含在内，所以用操作系统查得某库或表的大小总是小于实际占用空间。